"""Prepare a portrait for the monochrome ASCII SVG pipeline.

Usage: python scripts/prep_photo.py source-photo.jpg
The output is source-prepped.png in the repository root.
"""
from pathlib import Path
import sys

from PIL import Image, ImageOps, ImageEnhance


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/prep_photo.py <photo>")
    source = Path(sys.argv[1])
    if not source.exists():
        raise SystemExit(f"Photo not found: {source}")

    image = Image.open(source).convert("RGBA")
    # A conservative local-only fallback: remove near-white background pixels.
    # For best results, install rembg and replace this step with its model output.
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if min(r, g, b) > 235:
                pixels[x, y] = (255, 255, 255, 0)

    background = Image.new("RGBA", image.size, "white")
    background.alpha_composite(image)
    gray = ImageOps.grayscale(background)
    gray = ImageOps.autocontrast(gray, cutoff=1)
    gray = ImageEnhance.Contrast(gray).enhance(1.35)
    gray.save("source-prepped.png")
    print("Wrote source-prepped.png")


if __name__ == "__main__":
    main()
