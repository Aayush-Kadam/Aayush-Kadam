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
    assert 'hits.sh/github.com/Aayush-Kadam.svg' in readme and 'extraCount=' not in readme
    assert readme.index('hits.sh/github.com/Aayush-Kadam.svg') < readme.index('## Selected engineering')
    assert 'assets/hero/observatory.svg' in readme
    assert 'assets/hero/observatory-mobile.svg' in readme
    assert 'PROFILE IMAGE REQUESTS' in readme and 'Profile%20image%20requests' in readme
    contact=readme.split('## Connect',1)[1]
    assert 'https://github.com/Aayush-Kadam' not in contact, 'Redundant GitHub contact link'
    assert not re.search(r'(?i)site/|github pages|webgl|three\.js|interactive portfolio|local preview', readme)
    assert not (ROOT/'site').exists() and not (ROOT/'.github/workflows/pages.yml').exists()
    assert not re.search(r'<(?:script|iframe|style)\b',readme)
    print(f'PASS: {len(targets)} links/image sources; {len(files)} safe accessible SVGs; {size:,} bytes; anchors and alt text.')

if __name__=='__main__':main()
