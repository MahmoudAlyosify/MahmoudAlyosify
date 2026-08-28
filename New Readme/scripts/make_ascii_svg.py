"""Generate avi-ascii.svg with row-by-row SVG clipping animation.

If source-prepped.png is present, it is converted to ASCII. Otherwise a
clean built-in terminal portrait is used so the repository always previews.
"""
from pathlib import Path
from html import escape
from PIL import Image, ImageOps

OUTPUT = Path("avi-ascii.svg")
RAMP = " .`:-=+*cs#%@"
WIDTH, HEIGHT = 62, 31
CELL_W, CELL_H = 5.55, 9.0

FALLBACK = [
"                         .-========-.                         ",
"                     .-##############-.                     ",
"                  .-####################-.                  ",
"                .##########################.                ",
"              .##############################.              ",
"             ##################################             ",
"            #######%%%%%%######%%%%%%#########             ",
"           ######%%%%%%%######%%%%%%%##########            ",
"           #####%%%%%%#########################            ",
"           ######%%%%#------##------#%#########            ",
"           ######%%%#        #        #%%######            ",
"           ######%%%#   ..   #   ..   #%%######            ",
"           ######%%%#        #        #%%######            ",
"           ##########     .  #  .     #########            ",
"           ###########.     ---     .##########            ",
"           #############..       ..############            ",
"            ###############################%###            ",
"             ######%%################%%######             ",
"              ######%%%############%%%######              ",
"                ######%%%%%%%%%%%%%%######                ",
"                  ######################                  ",
"                    ##################                    ",
"                      ##############                      ",
"                       ############                       ",
"                         ########                         ",
"             .------------------------------.             ",
"             |  MAHMOUD ALYOSIFY / AI ENG   |             ",
"             '------------------------------'             ",
"                                                              ",
"                    [ terminal portrait ]                    ",
"                                                              ",
]


def get_lines():
    source = Path("source-prepped.png")
    if not source.exists():
        return FALLBACK
    img = Image.open(source).convert("L")
    img = ImageOps.fit(img, (WIDTH, HEIGHT), method=Image.Resampling.LANCZOS)
    lines = []
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            value = img.getpixel((x, y))
            line += RAMP[int((255 - value) / 256 * len(RAMP))]
        lines.append(line.rstrip())
    return lines


def main():
    lines = get_lines()
    width = WIDTH * CELL_W + 24
    height = len(lines) * CELL_H + 44
    rows = []
    for i, line in enumerate(lines):
        y = 28 + i * CELL_H
        clip_id = f"row-{i}"
        rows.append(f'<clipPath id="{clip_id}"><rect x="0" y="{y-7:.1f}" width="0" height="10"><animate attributeName="width" from="0" to="{width}" dur="0.52s" begin="{i*0.055:.3f}s" fill="freeze"/></rect></clipPath>')
        rows.append(f'<text x="12" y="{y:.1f}" clip-path="url(#{clip_id})">{escape(line)}</text>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}" role="img" aria-label="Animated ASCII portrait">
<rect width="100%" height="100%" rx="12" fill="#0d1117" stroke="#30363d"/>
<text x="12" y="16" fill="#8b949e" font-family="monospace" font-size="9">./portrait --mode=monochrome</text>
<style>text{{font-family:monospace;font-size:8px;letter-spacing:1px;fill:#c9d1d9;white-space:pre}}</style>
{''.join(rows)}
</svg>'''
    OUTPUT.write_text(svg, encoding="utf-8")
    print(f"Wrote {OUTPUT}")

if __name__ == "__main__":
    main()
