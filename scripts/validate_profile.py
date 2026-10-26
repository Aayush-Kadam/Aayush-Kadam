"""Check local README links, image accessibility, SVG safety and asset budget."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]

def main():
    readme=(ROOT/'README.md').read_text(encoding='utf-8')
    targets=re.findall(r'(?:href|src|srcset)="([^"]+)"',readme)
    targets+=re.findall(r'\]\(([^\s)]+)\)',readme)
    headings={re.sub(r'[^\w -]','',h.lower()).replace(' ','-') for h in re.findall(r'^#+ (.+)$',readme,re.M)}
    for target in targets:
        if target.startswith('https://'): continue
        path,_,anchor=target.partition('#')
        if path: assert (ROOT/path).is_file(), f'Missing local target: {target}'
        elif anchor: assert anchor in headings, f'Missing README anchor: {anchor}'
    for img in re.findall(r'<img\b[^>]*>',readme):
        assert re.search(r'alt="[^"]{12,}"',img), f'Missing meaningful alt: {img}'
    ns='{http://www.w3.org/2000/svg}'
    files=list((ROOT/'assets').rglob('*.svg'))
    for path in files:
        content=path.read_text(encoding='utf-8')
        svg=ET.fromstring(content)
        assert svg.tag==ns+'svg' and svg.get('viewBox'),path
        assert svg.find(ns+'title') is not None and svg.find(ns+'desc') is not None,path
        assert not re.search(r'<(?:script|foreignObject|image|animate)\b|https?://(?!www.w3.org)|onload=',content),path
    size=sum(p.stat().st_size for p in files)
    assert size < 2_000_000,size
    assert 'username=Aayush-Kadam' in readme and '&base=' not in readme
    assert not re.search(r'<(?:script|iframe|style)\b',readme)
    print(f'PASS: {len(targets)} links/image sources; {len(files)} safe accessible SVGs; {size:,} bytes; anchors and alt text.')

if __name__=='__main__':main()
