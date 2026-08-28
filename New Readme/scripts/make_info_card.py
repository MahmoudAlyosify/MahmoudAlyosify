"""Generate the terminal-style profile card SVG."""
from pathlib import Path
import os

OUT = Path("info-card.svg")
STATIC = os.getenv("STATIC") == "1"
rows = [
    ("role", "AI / ML Engineer"),
    ("research", "Efficient LLM inference"),
    ("degree", "MSc AI @ Queen's University"),
    ("stack", "PyTorch · AWS · Docker · FastAPI"),
    ("building", "Agents · RAG · MLOps"),
    ("teaching", "10K+ learners · 700K+ views"),
    ("location", "New Cairo, Egypt / Canada"),
]
W, H = 490, 330
parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Mahmoud Alyosify profile information card">',
         '<rect width="490" height="330" rx="12" fill="#0d1117" stroke="#30363d"/>',
         '<rect x="1" y="1" width="488" height="35" rx="11" fill="#161b22"/>',
         '<circle cx="20" cy="18" r="5" fill="#ff7b72"/><circle cx="38" cy="18" r="5" fill="#d29922"/><circle cx="56" cy="18" r="5" fill="#3fb950"/>',
         '<text x="78" y="23" fill="#8b949e" font-family="monospace" font-size="13">mahmoud@github — neofetch</text>',
         '<text x="24" y="68" fill="#58a6ff" font-family="monospace" font-weight="bold" font-size="18">MAHMOUD ALYOSIFY</text>',
         '<text x="24" y="88" fill="#8b949e" font-family="monospace" font-size="11">AI &amp; MACHINE LEARNING ENGINEER</text>']
for i, (key, value) in enumerate(rows):
    y = 121 + i * 27
    delay = 0 if STATIC else i * 0.12
    animation = '' if STATIC else f'<animate attributeName="opacity" from="0" to="1" dur="0.35s" begin="{delay:.2f}s" fill="freeze"/><animateTransform attributeName="transform" type="translate" from="-8 0" to="0 0" dur="0.35s" begin="{delay:.2f}s" fill="freeze"/>'
    parts.append(f'<g opacity="{1 if STATIC else 0}">{animation}<text x="28" y="{y}" fill="#7ee787" font-family="monospace" font-size="12">{key:<10}</text><text x="145" y="{y}" fill="#c9d1d9" font-family="monospace" font-size="12">{value}</text></g>')
parts += ['<line x1="24" y1="302" x2="466" y2="302" stroke="#30363d"/>', '<text x="24" y="320" fill="#8b949e" font-family="monospace" font-size="10">[ available for ambitious AI systems ]</text>', '</svg>']
OUT.write_text("\n".join(parts), encoding="utf-8")
print(f"Wrote {OUT}")
