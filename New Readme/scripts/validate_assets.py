from pathlib import Path
import json
import xml.etree.ElementTree as ET

root = Path('.')
for script in Path('scripts').glob('*.py'):
    compile(script.read_text(encoding='utf-8'), str(script), 'exec')
json.loads(Path('data/contributions.json').read_text(encoding='utf-8'))
for svg in (Path('avi-ascii.svg'), Path('info-card.svg'), Path('contrib-heatmap.svg')):
    ET.parse(svg)
print('Validation passed: Python scripts, contributions JSON, and all SVG assets are valid.')
