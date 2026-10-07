import os
import sys
import numpy as np
import cv2
from PIL import Image, ImageSequence, UnidentifiedImageError

# ---------------------------------------------------------
# GENERATION SETTINGS
# ---------------------------------------------------------
WIDTH = 1200
HEIGHT = 300
TRANSITION_FRAMES = 18
HOLD_FRAMES = 12
FINAL_HOLD_FRAMES = 24
FPS = 15
BG_COLOR = (13, 17, 23) # #0d1117 README background

assets_dir = os.path.join(os.path.dirname(__file__), '..', 'assets')
gif_paths = [
    os.path.join(assets_dir, 'Geto.gif'),
    os.path.join(assets_dir, 'jujutsu-kaisen-jjk.gif'),
    os.path.join(assets_dir, 'geto-suguru.gif'),
    os.path.join(assets_dir, 'geto-suguru-yo.gif')
]

# (cx, cy, rx, ry) - Normalized coordinates inside the original GIF dimensions
# Protects dark character features (hair/clothes/face) from luminance extraction
CORES = [
    (0.8, 0.5, 0.25, 0.5), # Image 0: Geto (character on right)
    (0.4, 0.5, 0.3, 0.5),  # Image 1: JJK (character center-left)
    (0.5, 0.5, 0.35, 0.5), # Image 2: Geto Suguru (character center)
    (0.5, 0.5, 0.4, 0.5)   # Image 3: Geto Suguru Yo (character center)
]

if len(CORES) != len(gif_paths):
    raise ValueError(
        f"CORES has {len(CORES)} entries but gif_paths has {len(gif_paths)}; "
        "every source GIF needs matching core parameters"
    )

def smoothstep(edge0, edge1, x):
    x = np.clip((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return x * x * (3.0 - 2.0 * x)

def load_and_extract_alpha(path, core_params, num_target_frames):
    print(f"Loading and extracting alpha: {path}...")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Source GIF not found: {path}")
    try:
        gif = Image.open(path)
    except (UnidentifiedImageError, OSError) as exc:
        raise RuntimeError(f"Could not open source GIF {path}: {exc}") from exc
    frames = []

    for frame_number, frame in enumerate(ImageSequence.Iterator(gif)):
        try:
            frame = frame.convert('RGB')
            img = np.array(frame)
        except OSError as exc:
            raise RuntimeError(
                f"Failed to decode frame {frame_number} of {path}: {exc}"
            ) from exc
        h, w = img.shape[:2]
        
        # 1. Content-Aware Crop for Geto.gif (Remove massive black padding)
        non_black = np.any(img > 15, axis=-1)
        y_idx, x_idx = np.where(non_black)
        if len(y_idx) > 0:
            ymin, ymax = y_idx.min(), y_idx.max()
            xmin, xmax = x_idx.min(), x_idx.max()
            # If the crop is significantly smaller, apply it (Geto.gif)
            if (xmax - xmin) < w * 0.9:
                margin = 5
                ymin = max(0, ymin - margin); ymax = min(h-1, ymax + margin)
                xmin = max(0, xmin - margin); xmax = min(w-1, xmax + margin)
                img = img[ymin:ymax+1, xmin:xmax+1]
                h, w = img.shape[:2]
        
        # 2. Extract Luminance Alpha
        L = 0.299 * img[:,:,0] + 0.587 * img[:,:,1] + 0.114 * img[:,:,2]
        lum_alpha = smoothstep(15, 60, L)
        
        # 3. Apply Core Protection
        y, x = np.ogrid[:h, :w]
        cx, cy, rx, ry = core_params
        cx *= w; cy *= h; rx *= w; ry *= h
        core = 1.0 - ((x - cx)/rx)**4 - ((y - cy)/ry)**4
        core = np.clip(core, 0, 1)
        
        base_alpha = np.maximum(lum_alpha, core)
        base_alpha = cv2.GaussianBlur(base_alpha, (3, 3), 0)
        
        # 4. Scale to Canvas (Contain)
        scale = min(WIDTH / w, HEIGHT / h)
        new_w, new_h = int(w * scale), int(h * scale)
        
        out_rgba = np.zeros((h, w, 4), dtype=np.uint8)
        out_rgba[:,:,:3] = img
        out_rgba[:,:,3] = (base_alpha * 255).astype(np.uint8)
        
        fg_resized = Image.fromarray(out_rgba).resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Place on 1200x300 transparent canvas
        canvas = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        x_off = (WIDTH - new_w) // 2
        y_off = (HEIGHT - new_h) // 2
        canvas.paste(fg_resized, (x_off, y_off), fg_resized)
        
        frames.append(np.array(canvas).astype(float) / 255.0)

    if not frames:
        raise RuntimeError(f"No frames could be decoded from {path}")

    out_frames = []
    for i in range(num_target_frames):
        out_frames.append(frames[i % len(frames)])
    return out_frames

def create_transition():
    total_frames = HOLD_FRAMES * 3 + FINAL_HOLD_FRAMES + TRANSITION_FRAMES * 3
    print(f"Total frames to generate: {total_frames}")

    gifs_frames = [
        load_and_extract_alpha(path, core, total_frames)
        for path, core in zip(gif_paths, CORES)
    ]
    final_frames = []

    # Organic Liquid Wave Setup
    y_coords = np.arange(HEIGHT)
    x_coords = np.arange(WIDTH)
    xx, yy = np.meshgrid(x_coords, y_coords)

    # Multi-frequency organic wave
    wave_y1 = np.sin(yy / 30.0)
    wave_y2 = np.sin(yy / 70.0 + 1.5)
    wave_y3 = np.sin(yy / 15.0 + yy / 80.0)
    wave_x1 = np.sin(xx / 60.0)
    
    amplitude = 120.0
    wave_offset = amplitude * wave_y1 + (amplitude * 0.5) * wave_y2 + (amplitude * 0.3) * wave_y3
    wave_offset += 60.0 * wave_x1 * wave_y2

    base_T = xx - wave_offset

    def blend_frames(f1_rgba, f2_rgba, progress):
        # f1 and f2 are [H, W, 4] floats in 0..1
        boundary = progress * (WIDTH + 600) - 300
        
        # Wave mask: 1.0 (left, new frame), 0.0 (right, old frame)
        # Using a very soft feather (150px) for a liquid blend
        wave_mask = np.clip((boundary - base_T) / 150.0 + 0.5, 0, 1)
        wave_mask = wave_mask[:, :, np.newaxis]
        
        # Multiply source alphas by the wave
        a1 = f1_rgba[..., 3:] * (1.0 - wave_mask)
        a2 = f2_rgba[..., 3:] * wave_mask
        
        # Over operator (A over B) onto background
        bg_rgb = np.array(BG_COLOR, dtype=float).reshape(1, 1, 3) / 255.0
        
        # f1 over BG
        comp_f1_rgb = f1_rgba[..., :3] * a1 + bg_rgb * (1.0 - a1)
        # f2 over (f1 over BG)
        comp_final_rgb = f2_rgba[..., :3] * a2 + comp_f1_rgb * (1.0 - a2)
        
        return np.clip(comp_final_rgb * 255.0, 0, 255).astype(np.uint8)

    print("Generating frames...")
    for frame_idx in range(total_frames):
        if frame_idx < HOLD_FRAMES:
            # Still frame 0
            img = blend_frames(gifs_frames[0][frame_idx], gifs_frames[0][frame_idx], 0.0)
            
        elif frame_idx < HOLD_FRAMES + TRANSITION_FRAMES:
            progress = (frame_idx - HOLD_FRAMES) / (TRANSITION_FRAMES - 1)
            img = blend_frames(gifs_frames[0][frame_idx], gifs_frames[1][frame_idx], progress)
            
        elif frame_idx < HOLD_FRAMES * 2 + TRANSITION_FRAMES:
            # Still frame 1
            img = blend_frames(gifs_frames[1][frame_idx], gifs_frames[1][frame_idx], 0.0)
            
        elif frame_idx < HOLD_FRAMES * 2 + TRANSITION_FRAMES * 2:
            progress = (frame_idx - (HOLD_FRAMES * 2 + TRANSITION_FRAMES)) / (TRANSITION_FRAMES - 1)
            img = blend_frames(gifs_frames[1][frame_idx], gifs_frames[2][frame_idx], progress)
            
        elif frame_idx < HOLD_FRAMES * 3 + TRANSITION_FRAMES * 2:
            # Still frame 2
            img = blend_frames(gifs_frames[2][frame_idx], gifs_frames[2][frame_idx], 0.0)
            
        elif frame_idx < HOLD_FRAMES * 3 + TRANSITION_FRAMES * 3:
            progress = (frame_idx - (HOLD_FRAMES * 3 + TRANSITION_FRAMES * 2)) / (TRANSITION_FRAMES - 1)
            img = blend_frames(gifs_frames[2][frame_idx], gifs_frames[3][frame_idx], progress)
            
        else:
            # Still frame 3
            img = blend_frames(gifs_frames[3][frame_idx], gifs_frames[3][frame_idx], 0.0)

        final_frames.append(Image.fromarray(img))

    out_path = os.path.join(assets_dir, 'geto-transition.webp')
    print(f"Saving to {out_path}...")
    try:
        final_frames[0].save(
            out_path,
            format='WEBP',
            save_all=True,
            append_images=final_frames[1:],
            duration=1000//FPS,
            loop=0,
            quality=80,
            method=4
        )
    except OSError as exc:
        raise RuntimeError(f"Failed to write banner to {out_path}: {exc}") from exc
    print(f"Saved {out_path} with {len(final_frames)} frames.")

if __name__ == '__main__':
    try:
        create_transition()
    except (RuntimeError, OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
