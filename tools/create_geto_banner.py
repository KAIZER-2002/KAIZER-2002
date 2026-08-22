import os
import math
import numpy as np
from PIL import Image, ImageSequence

# Settings
WIDTH = 1200
HEIGHT = 300
TRANSITION_FRAMES = 18
HOLD_FRAMES = 10
FINAL_HOLD_FRAMES = 18
FPS = 15

assets_dir = os.path.join(os.path.dirname(__file__), '..', 'assets')
gif_paths = [
    os.path.join(assets_dir, 'Geto.gif'),
    os.path.join(assets_dir, 'jujutsu-kaisen-jjk.gif'),
    os.path.join(assets_dir, 'geto-suguru.gif'),
    os.path.join(assets_dir, 'geto-suguru-yo.gif')
]

def load_and_resize_gif(path, num_target_frames):
    print(f"Loading {path}...")
    gif = Image.open(path)
    frames = []
    for frame in ImageSequence.Iterator(gif):
        frame = frame.convert('RGB')
        # Crop to target aspect ratio
        w, h = frame.size
        target_aspect = WIDTH / HEIGHT
        aspect = w / h
        if aspect > target_aspect:
            # Crop width
            new_w = int(h * target_aspect)
            left = (w - new_w) // 2
            frame = frame.crop((left, 0, left + new_w, h))
        else:
            # Crop height
            new_h = int(w / target_aspect)
            top = (h - new_h) // 2
            frame = frame.crop((0, top, w, top + new_h))

        frame = frame.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
        frames.append(np.array(frame))

    # Loop or trim to match target frames
    out_frames = []
    for i in range(num_target_frames):
        out_frames.append(frames[i % len(frames)])
    return out_frames

def create_transition():
    total_frames = HOLD_FRAMES * 3 + FINAL_HOLD_FRAMES + TRANSITION_FRAMES * 3
    print(f"Total frames to generate: {total_frames}")

    # Load all 4 GIFs extended to total_frames
    gifs_frames = [load_and_resize_gif(path, total_frames) for path in gif_paths]

    final_frames = []

    # Generate a displacement map for the wave
    y_coords = np.arange(HEIGHT)
    x_coords = np.arange(WIDTH)
    xx, yy = np.meshgrid(x_coords, y_coords)

    # complex wave pattern
    wave_offset = 60 * np.sin(yy / 25.0) + 40 * np.sin(yy / 55.0 + 1.5) + 25 * np.sin(yy / 15.0 + yy / 60.0)

    print("Generating frames...")
    for frame_idx in range(total_frames):
        # Determine which transition we are in
        if frame_idx < HOLD_FRAMES:
            # Hold image 0
            img = gifs_frames[0][frame_idx]
        elif frame_idx < HOLD_FRAMES + TRANSITION_FRAMES:
            # Transition 0 -> 1
            progress = (frame_idx - HOLD_FRAMES) / TRANSITION_FRAMES
            img1 = gifs_frames[0][frame_idx]
            img2 = gifs_frames[1][frame_idx]

            boundary = progress * (WIDTH + 250) - 125
            dist = boundary + wave_offset - xx
            mask = np.clip(dist / 30.0 + 0.5, 0, 1) # smooth blend
            mask = mask[:, :, np.newaxis]

            img = img1 * (1 - mask) + img2 * mask
            img = img.astype(np.uint8)

        elif frame_idx < HOLD_FRAMES * 2 + TRANSITION_FRAMES:
            # Hold image 1
            img = gifs_frames[1][frame_idx]
        elif frame_idx < HOLD_FRAMES * 2 + TRANSITION_FRAMES * 2:
            # Transition 1 -> 2
            progress = (frame_idx - (HOLD_FRAMES * 2 + TRANSITION_FRAMES)) / TRANSITION_FRAMES
            img1 = gifs_frames[1][frame_idx]
            img2 = gifs_frames[2][frame_idx]

            boundary = progress * (WIDTH + 250) - 125
            dist = boundary + wave_offset - xx
            mask = np.clip(dist / 30.0 + 0.5, 0, 1)
            mask = mask[:, :, np.newaxis]

            img = img1 * (1 - mask) + img2 * mask
            img = img.astype(np.uint8)

        elif frame_idx < HOLD_FRAMES * 3 + TRANSITION_FRAMES * 2:
            # Hold image 2
            img = gifs_frames[2][frame_idx]
        elif frame_idx < HOLD_FRAMES * 3 + TRANSITION_FRAMES * 3:
            # Transition 2 -> 3
            progress = (frame_idx - (HOLD_FRAMES * 3 + TRANSITION_FRAMES * 2)) / TRANSITION_FRAMES
            img1 = gifs_frames[2][frame_idx]
            img2 = gifs_frames[3][frame_idx]

            boundary = progress * (WIDTH + 250) - 125
            dist = boundary + wave_offset - xx
            mask = np.clip(dist / 30.0 + 0.5, 0, 1)
            mask = mask[:, :, np.newaxis]

            img = img1 * (1 - mask) + img2 * mask
            img = img.astype(np.uint8)

        else:
            # Hold image 3
            img = gifs_frames[3][frame_idx]

        final_frames.append(Image.fromarray(img))

    out_path = os.path.join(assets_dir, 'geto-transition.webp')
    print(f"Saving to {out_path}...")
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
    print(f"Saved {out_path} with {len(final_frames)} frames.")

if __name__ == '__main__':
    create_transition()
