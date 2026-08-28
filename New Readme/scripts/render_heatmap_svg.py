"""Render 53 weeks of contribution data as a one-shot animated SVG."""
from pathlib import Path
import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
CELL, GAP, COLS, ROWS = 12, 3, 53, 7
X0, Y0 = 35, 43


def main():
    payload = json.loads(Path("data/contributions.json").read_text(encoding="utf-8"))
    by_date = {d["date"]: d for d in payload["days"]}
    days = payload["days"][-COLS * ROWS:]
    cells = []
    for index in range(COLS * ROWS):
        d = days[index] if index < len(days) else {"count": 0, "level": 0}
        col, row = index // ROWS, index % ROWS
        cells.append((col, row, d.get("level", 0), d.get("count", 0)))
    stats = payload["stats"]
    width, height = 860, 188
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="Animated GitHub contribution heatmap">',
             '<rect width="100%" height="100%" rx="12" fill="#0d1117" stroke="#30363d"/>',
             '<text x="35" y="23" fill="#c9d1d9" font-family="monospace" font-size="13">contributions / last 53 weeks</text>',
             '<text x="825" y="23" text-anchor="end" fill="#8b949e" font-family="monospace" font-size="11">refresh: daily</text>']
    for col, row, level, count in cells:
        x, y = X0 + col * (CELL + GAP), Y0 + row * (CELL + GAP)
        delay = 0.02 + (col + row) * 0.018
        parts.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" fill="{PALETTE[min(level, 5)]}" opacity="0"><title>{count} contributions</title><animate attributeName="opacity" from="0" to="1" dur="0.35s" begin="{delay:.3f}s" fill="freeze"/></rect>')
    parts += ['<text x="35" y="166" fill="#8b949e" font-family="monospace" font-size="11">less</text>']
    for i, color in enumerate(PALETTE):
        parts.append(f'<rect x="68" y="157" width="11" height="11" rx="2" fill="{color}"/>')
    parts += [f'<text x="140" y="166" fill="#8b949e" font-family="monospace" font-size="11">more</text>',
              f'<text x="825" y="166" text-anchor="end" fill="#7ee787" font-family="monospace" font-size="11">{stats["total"]:,} contributions · {stats["current_streak"]} day streak · best {stats["best_day"]}</text>', '</svg>']
    Path("contrib-heatmap.svg").write_text("\n".join(parts), encoding="utf-8")
    print("Wrote contrib-heatmap.svg")

if __name__ == "__main__": main()
