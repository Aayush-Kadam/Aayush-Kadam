"""Generate the GitHub-native Observatory hero (no external assets or runtime)."""

from itertools import combinations
from math import cos, sin, sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHI = (1 + sqrt(5)) / 2
VERTICES = ([(0, a, b * PHI) for a in (-1, 1) for b in (-1, 1)]
            + [(a, b * PHI, 0) for a in (-1, 1) for b in (-1, 1)]
            + [(a * PHI, 0, b) for a in (-1, 1) for b in (-1, 1)])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def face_indices():
    faces = []
    for trio in combinations(range(len(VERTICES)), 3):
        a, b, c = (VERTICES[i] for i in trio)
        normal = cross(sub(b, a), sub(c, a))
        signed = [dot(normal, sub(v, a)) for i, v in enumerate(VERTICES) if i not in trio]
        if all(x >= -1e-7 for x in signed) or all(x <= 1e-7 for x in signed):
            faces.append(trio)
    assert len(faces) == 20
    return faces


FACES = face_indices()


def rotated(v):
    x, y, z = v
    yaw, pitch, roll = .57, -.34, -.12
    x, z = x * cos(yaw) + z * sin(yaw), -x * sin(yaw) + z * cos(yaw)
    y, z = y * cos(pitch) - z * sin(pitch), y * sin(pitch) + z * cos(pitch)
    x, y = x * cos(roll) - y * sin(roll), x * sin(roll) + y * cos(roll)
    return x, y, z


def crystal(cx, cy, radius):
    verts = [rotated(v) for v in VERTICES]
    projected = [(cx + x * radius / PHI, cy - y * radius / PHI) for x, y, _ in verts]
    fragments = []
    for face in sorted(FACES, key=lambda ids: sum(verts[i][2] for i in ids)):
        points = ' '.join(f'{projected[i][0]:.1f},{projected[i][1]:.1f}' for i in face)
        depth = sum(verts[i][2] for i in face) / 3
        opacity = .19 if depth < 0 else .42 + .10 * depth
        fragments.append(f'<polygon points="{points}" fill="url(#facet)" fill-opacity="{opacity:.2f}" '
                         'stroke="#b7f7f4" stroke-opacity=".26" stroke-width="1.2"/>')
    for x, y in projected:
        fragments.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.1" fill="#c9fffa" opacity=".75"/>')
    fragments.append(f'<circle cx="{cx}" cy="{cy}" r="{radius*.29:.1f}" fill="url(#core)" opacity=".9"/>')
    fragments.append(f'<circle cx="{cx}" cy="{cy}" r="{radius*.115:.1f}" fill="#b7fff4" opacity=".37"/>')
    return ''.join(fragments)


def svg(mobile=False):
    w, h = (720, 850) if mobile else (1200, 560)
    cx, cy, r = (360, 300, 194) if mobile else (876, 280, 204)
    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title description">
<title id="title">Aayush Kadam — Ideas meet evidence</title>
<desc id="description">A luminous faceted three-dimensional instrument inside fine orbital rings, beside the words Ideas meet evidence. Original vector artwork for a GitHub profile.</desc>
<defs>
  <radialGradient id="glow"><stop stop-color="#2dabb0" stop-opacity=".28"/><stop offset=".52" stop-color="#173c4a" stop-opacity=".13"/><stop offset="1" stop-color="#071019" stop-opacity="0"/></radialGradient>
  <linearGradient id="facet" x1=".15" y1=".08" x2=".89" y2=".95"><stop stop-color="#d2fff5"/><stop offset=".33" stop-color="#60d5df"/><stop offset=".7" stop-color="#196e8a"/><stop offset="1" stop-color="#092b4b"/></linearGradient>
  <radialGradient id="core"><stop stop-color="#d9fff7" stop-opacity=".8"/><stop offset=".45" stop-color="#5fe7df" stop-opacity=".35"/><stop offset="1" stop-color="#12aabd" stop-opacity="0"/></radialGradient>
  <linearGradient id="rule"><stop stop-color="#76e8df" stop-opacity=".58"/><stop offset=".56" stop-color="#e4c48c" stop-opacity=".47"/><stop offset="1" stop-color="#76e8df" stop-opacity="0"/></linearGradient>
  <pattern id="mesh" width="38" height="38" patternUnits="userSpaceOnUse"><path d="M38 0H0V38" fill="none" stroke="#a0c6d3" stroke-opacity=".055"/></pattern>
</defs>
<style>
@keyframes orbit {{ to {{ stroke-dashoffset: -140; }} }}
@keyframes breathe {{ 50% {{ opacity: .5; }} }}
.orbit {{ animation: orbit 42s linear infinite; }}
.beacon {{ animation: breathe 5s ease-in-out infinite; }}
@media (prefers-reduced-motion: reduce) {{ .orbit, .beacon {{ animation: none; }} }}
</style>
<rect width="{w}" height="{h}" rx="18" fill="#071019"/>
<rect width="{w}" height="{h}" rx="18" fill="url(#mesh)"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="17" fill="none" stroke="#729bab" stroke-opacity=".28"/>
<circle cx="{cx}" cy="{cy}" r="{r*1.67:.1f}" fill="url(#glow)"/>
''']
    for i in range(68):
        x = (i * 173 + i * i * 29) % w
        y = (i * 97 + i * i * 13) % h
        if (x - cx) ** 2 + (y - cy) ** 2 < (r * 1.18) ** 2:
            continue
        parts.append(f'<circle cx="{x}" cy="{y}" r="{.55 if i%3 else .85}" fill="#c8ecec" opacity="{.12 if i%4 else .31}"/>')
    parts += [
        f'<ellipse cx="{cx}" cy="{cy}" rx="{r*1.30:.1f}" ry="{r*.39:.1f}" transform="rotate(-31 {cx} {cy})" fill="none" stroke="#88eeeb" stroke-opacity=".48" stroke-width="1.5"/>',
        f'<ellipse cx="{cx}" cy="{cy}" rx="{r*1.20:.1f}" ry="{r*.46:.1f}" transform="rotate(41 {cx} {cy})" fill="none" stroke="#dfc59d" stroke-opacity=".50" stroke-width="1.35"/>',
        f'<ellipse cx="{cx}" cy="{cy}" rx="{r*1.08:.1f}" ry="{r*.55:.1f}" transform="rotate(96 {cx} {cy})" fill="none" stroke="#779abd" stroke-opacity=".36" stroke-width="1.2"/>',
        f'<ellipse class="orbit" cx="{cx}" cy="{cy}" rx="{r*1.31:.1f}" ry="{r*.40:.1f}" transform="rotate(-31 {cx} {cy})" fill="none" stroke="#c5ffef" stroke-opacity=".72" stroke-width="2" stroke-dasharray="2 138"/>',
        crystal(cx, cy, r),
        f'<circle class="beacon" cx="{cx+r*1.00:.1f}" cy="{cy-r*.46:.1f}" r="5" fill="#eed6a2"/>',
        f'<circle cx="{cx-r*.98:.1f}" cy="{cy+r*.49:.1f}" r="3" fill="#8de7ee"/>',
    ]
    if mobile:
        parts += [
            '<text x="36" y="57" fill="#9fe5e3" font-family="Consolas,monospace" font-size="15" letter-spacing="2.6">A / K  ·  OBSERVATORY</text>',
            '<path d="M36 76H684" stroke="url(#rule)"/>',
            '<text x="36" y="604" fill="#f1f7f5" font-family="Segoe UI,Arial,sans-serif" font-size="62" font-weight="650" letter-spacing="-2.7">Ideas meet</text>',
            '<text x="36" y="680" fill="#9ce1df" font-family="Georgia,serif" font-size="73" font-style="italic" letter-spacing="-3">evidence.</text>',
            '<path d="M36 723H684" stroke="url(#rule)"/>',
            '<text x="36" y="767" fill="#bacad0" font-family="Consolas,monospace" font-size="14" letter-spacing="1.8">ENGINEERING / ECONOMICS / RESEARCH</text>',
            '<text x="36" y="810" fill="#d9e4e5" font-family="Segoe UI,Arial,sans-serif" font-size="18">Aayush Kadam</text>',
        ]
    else:
        parts += [
            '<text x="47" y="60" fill="#9fe5e3" font-family="Consolas,monospace" font-size="15" letter-spacing="2.7">A / K  ·  OBSERVATORY</text>',
            '<path d="M47 79H1153" stroke="url(#rule)"/>',
            '<text x="47" y="205" fill="#f1f7f5" font-family="Segoe UI,Arial,sans-serif" font-size="71" font-weight="650" letter-spacing="-3.3">Ideas meet</text>',
            '<text x="47" y="300" fill="#9ce1df" font-family="Georgia,serif" font-size="88" font-style="italic" letter-spacing="-4">evidence.</text>',
            '<path d="M47 341H458" stroke="url(#rule)"/>',
            '<text x="47" y="387" fill="#d2e0e2" font-family="Segoe UI,Arial,sans-serif" font-size="22">Aayush Kadam</text>',
            '<text x="47" y="420" fill="#aebfc7" font-family="Segoe UI,Arial,sans-serif" font-size="18">Engineering tools and computational research</text>',
            '<text x="47" y="455" fill="#aebfc7" font-family="Segoe UI,Arial,sans-serif" font-size="18">for claims that can be tested.</text>',
            '<path d="M47 493H1153" stroke="url(#rule)"/>',
            '<text x="47" y="527" fill="#94abb7" font-family="Consolas,monospace" font-size="13" letter-spacing="1.7">SOFTWARE  /  INCENTIVES  /  EVIDENCE</text>',
            '<text x="1043" y="527" fill="#94abb7" font-family="Consolas,monospace" font-size="13" letter-spacing="1.3">AK · 2026</text>',
        ]
    parts.append('</svg>')
    return ''.join(parts)


def main():
    out = ROOT / 'assets' / 'hero'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'observatory.svg').write_text(svg(), encoding='utf-8')
    (out / 'observatory-mobile.svg').write_text(svg(mobile=True), encoding='utf-8')
    print('Generated desktop and mobile README SVG heroes.')


if __name__ == '__main__':
    main()
