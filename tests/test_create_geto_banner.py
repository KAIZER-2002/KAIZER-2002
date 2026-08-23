import os
import sys

import numpy as np
import pytest
from PIL import Image

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools'))

import create_geto_banner as banner


def write_gif(path, frames):
    images = [Image.fromarray(f, mode='RGB') for f in frames]
    images[0].save(path, save_all=True, append_images=images[1:], duration=100, loop=0)
    return str(path)


def solid_frame(w, h, color):
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    frame[:, :] = color
    return frame


def padded_frame(w, h, color, box):
    """Bright box on black padding: exercises the content-aware crop."""
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    x0, y0, x1, y1 = box
    frame[y0:y1, x0:x1] = color
    return frame


class TestSmoothstep:
    def test_clamps_outside_edges(self):
        assert banner.smoothstep(10, 20, 5) == 0.0
        assert banner.smoothstep(10, 20, 10) == 0.0
        assert banner.smoothstep(10, 20, 20) == 1.0
        assert banner.smoothstep(10, 20, 25) == 1.0

    def test_midpoint_is_half(self):
        assert banner.smoothstep(0, 1, 0.5) == pytest.approx(0.5)

    def test_known_values(self):
        # x*x*(3-2x) for the normalized input
        assert banner.smoothstep(0, 1, 0.25) == pytest.approx(0.15625)
        assert banner.smoothstep(0, 1, 0.75) == pytest.approx(0.84375)

    def test_shifted_and_scaled_edges(self):
        assert banner.smoothstep(15, 60, 37.5) == pytest.approx(0.5)
        assert banner.smoothstep(15, 60, 15 + 0.25 * 45) == pytest.approx(0.15625)

    def test_monotonic_on_array_input(self):
        xs = np.linspace(-5, 15, 50)
        ys = banner.smoothstep(0, 10, xs)
        assert ys.shape == xs.shape
        assert np.all(np.diff(ys) >= 0)
        assert ys.min() == 0.0 and ys.max() == 1.0

    def test_derivative_vanishes_at_edges(self):
        eps = 1e-6
        left = banner.smoothstep(0, 1, eps) / eps
        right = (1.0 - banner.smoothstep(0, 1, 1 - eps)) / eps
        assert left < 1e-3
        assert right < 1e-3


class TestLoadAndExtractAlpha:
    core = (0.5, 0.5, 0.4, 0.5)

    @pytest.fixture
    def small_canvas(self, monkeypatch):
        monkeypatch.setattr(banner, 'WIDTH', 40)
        monkeypatch.setattr(banner, 'HEIGHT', 20)

    def test_returns_canvas_sized_normalized_rgba(self, tmp_path, small_canvas):
        path = write_gif(tmp_path / 'a.gif', [solid_frame(20, 20, (200, 200, 200))])
        frames = banner.load_and_extract_alpha(path, self.core, 3)
        assert len(frames) == 3
        for frame in frames:
            assert frame.shape == (20, 40, 4)
            assert frame.dtype == np.float64
            assert frame.min() >= 0.0 and frame.max() <= 1.0

    def test_cycles_source_frames_to_target_count(self, tmp_path, small_canvas):
        path = write_gif(
            tmp_path / 'b.gif',
            [solid_frame(20, 20, (255, 0, 0)), solid_frame(20, 20, (0, 255, 0))],
        )
        frames = banner.load_and_extract_alpha(path, self.core, 5)
        assert len(frames) == 5
        for i in range(2, 5):
            assert np.array_equal(frames[i], frames[i % 2])
        assert not np.array_equal(frames[0], frames[1])

    def test_bright_pixels_become_opaque(self, tmp_path, small_canvas):
        path = write_gif(tmp_path / 'c.gif', [solid_frame(20, 20, (255, 255, 255))])
        frame = banner.load_and_extract_alpha(path, self.core, 1)[0]
        # Square source contained in a 40x20 canvas -> 20x20 opaque block, centered
        assert frame[10, 20, 3] == pytest.approx(1.0)
        assert frame[10, 0, 3] == 0.0
        assert frame[10, 39, 3] == 0.0

    def test_core_protection_keeps_dark_center_opaque(self, tmp_path, small_canvas):
        # Fully black source: luminance alpha is 0 everywhere, only the core survives
        path = write_gif(tmp_path / 'd.gif', [solid_frame(20, 20, (0, 0, 0))])
        frame = banner.load_and_extract_alpha(path, self.core, 1)[0]
        assert frame[10, 20, 3] == pytest.approx(1.0, abs=0.02)
        # Outside the core ellipse (top edge of the placed image) stays transparent
        assert frame[0, 20, 3] < 0.1

    def test_content_aware_crop_removes_black_padding(self, tmp_path, small_canvas):
        # Bright 10x10 box inside a 100x20 frame; without cropping the scaled
        # content would be far smaller than the canvas height.
        path = write_gif(
            tmp_path / 'e.gif', [padded_frame(100, 20, (255, 255, 255), (45, 5, 55, 15))]
        )
        frame = banner.load_and_extract_alpha(path, self.core, 1)[0]
        opaque_rows = np.where(frame[:, :, 3].max(axis=1) > 0.5)[0]
        # The 10x10 box plus a 5px margin is cropped to 20x20 and scaled 1:1 into
        # the 20px-high canvas. Without the crop the 100x20 frame would scale to
        # 40x8, confining opaque content to rows 6..13.
        assert opaque_rows.min() < 6
        assert opaque_rows.max() > 13

    def test_wide_content_is_not_cropped(self, tmp_path, small_canvas):
        # Content spans >90% of the width, so the crop branch must be skipped
        path = write_gif(
            tmp_path / 'f.gif', [padded_frame(40, 20, (255, 255, 255), (0, 8, 40, 12))]
        )
        frame = banner.load_and_extract_alpha(path, self.core, 1)[0]
        alpha = frame[:, :, 3]
        assert alpha[0, 20] < 0.1
        assert alpha[10, 20] == pytest.approx(1.0, abs=0.02)

    def test_preserves_source_colors(self, tmp_path, small_canvas):
        path = write_gif(tmp_path / 'g.gif', [solid_frame(20, 20, (255, 0, 0))])
        frame = banner.load_and_extract_alpha(path, self.core, 1)[0]
        r, g, b = frame[10, 20, :3]
        assert r == pytest.approx(1.0, abs=0.02)
        assert g == pytest.approx(0.0, abs=0.02)
        assert b == pytest.approx(0.0, abs=0.02)

    def test_missing_file_raises(self, tmp_path, small_canvas):
        with pytest.raises(FileNotFoundError):
            banner.load_and_extract_alpha(str(tmp_path / 'missing.gif'), self.core, 1)


class TestCreateTransition:
    @pytest.fixture
    def tiny_run(self, tmp_path, monkeypatch):
        monkeypatch.setattr(banner, 'WIDTH', 40)
        monkeypatch.setattr(banner, 'HEIGHT', 20)
        monkeypatch.setattr(banner, 'HOLD_FRAMES', 1)
        monkeypatch.setattr(banner, 'FINAL_HOLD_FRAMES', 1)
        monkeypatch.setattr(banner, 'TRANSITION_FRAMES', 2)
        monkeypatch.setattr(banner, 'assets_dir', str(tmp_path))
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
        paths = [
            write_gif(tmp_path / f'src{i}.gif', [solid_frame(20, 20, c)])
            for i, c in enumerate(colors)
        ]
        monkeypatch.setattr(banner, 'gif_paths', paths)
        return tmp_path

    def test_writes_animated_webp_with_expected_frames(self, tiny_run):
        banner.create_transition()
        out_path = tiny_run / 'geto-transition.webp'
        assert out_path.exists()
        with Image.open(out_path) as out:
            assert out.size == (40, 20)
            # 1*3 + 1 hold + 2*3 transition frames are written; libwebp collapses
            # runs of identical frames, so only the distinct ones survive.
            assert 1 < out.n_frames <= 10

    def test_background_fills_transparent_regions(self, tiny_run):
        banner.create_transition()
        with Image.open(tiny_run / 'geto-transition.webp') as out:
            first = np.array(out.convert('RGB'))
        # Left/right canvas margins hold no content, so they show BG_COLOR
        for pixel in (first[0, 0], first[19, 39]):
            assert np.allclose(pixel, banner.BG_COLOR, atol=4)

    def test_hold_and_transition_frames_differ(self, tiny_run):
        banner.create_transition()
        frames = []
        with Image.open(tiny_run / 'geto-transition.webp') as out:
            for i in range(out.n_frames):
                out.seek(i)
                frames.append(np.array(out.convert('RGB')))
        assert not np.array_equal(frames[0], frames[-1])  # first vs last source
        # Mid-transition frame differs from the hold frame that precedes it
        assert not np.array_equal(frames[0], frames[1])
