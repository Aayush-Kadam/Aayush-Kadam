"""Original Observatory artwork. Standard-library Python; deterministic SVG output."""
from pathlib import Path
import math
import random
from html import escape

ROOT = Path(__file__).resolve().parents[1]
BG, CYAN, GOLD, VIOLET, WHITE, MUTED = '#090D16', '#33E6F5', '#D9B36C', '#9575FF', '#F2F6FC', '#A8B8CE'

def text(x, y, value, size=16, color=MUTED, weight=400, spacing=0, mono=False):
    family = 'Consolas, monospace' if mono else 'Segoe UI, Arial, sans-serif'
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}">{escape(value)}</text>'

def line(x1,y1,x2,y2,color=CYAN,opacity=.4,width=1):
    return f'<path d="M{x1:.2f},{y1:.2f} L{x2:.2f},{y2:.2f}" stroke="{color}" opacity="{opacity}" stroke-width="{width}" fill="none"/>'

def circle(x,y,r,color=CYAN,opacity=1):
    return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{color}" opacity="{opacity}"/>'

def wrap(w,h,title,body,desc):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs>
<radialGradient id="aura"><stop stop-color="#174759" stop-opacity=".7"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></radialGradient>
<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{CYAN}" stop-opacity=".2"/><stop offset=".5" stop-color="#18344D" stop-opacity=".5"/><stop offset="1" stop-color="{VIOLET}" stop-opacity=".15"/></linearGradient>
<linearGradient id="edge"><stop stop-color="{CYAN}"/><stop offset=".55" stop-color="#80CCD8"/><stop offset="1" stop-color="{GOLD}"/></linearGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#23354B" stroke-width=".5"/></pattern>
</defs>
<style>
@keyframes orbital-trace {{ to {{ stroke-dashoffset: -480; }} }}
.orbital-trace {{ animation: orbital-trace 80s linear infinite; }}
@media (prefers-reduced-motion: reduce) {{ .orbital-trace {{ animation: none; }} }}
</style>
<rect width="{w}" height="{h}" rx="20" fill="{BG}"/>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="20" fill="none" stroke="#2B3A50"/>
{body}</svg>'''

def instrument(cx,cy,scale=1):
    # Orthographic projection of a cuboctahedral instrument, including depth order.
    out = [f'<g transform="translate({cx} {cy}) scale({scale})">', '<circle r="325" fill="url(#aura)"/>']
    rng = random.Random(41)
    for _ in range(58):
        x,y=rng.uniform(-265,265),rng.uniform(-235,235)
        out.append(circle(x,y,rng.choice([.7,1,1.5]),MUTED,.35))
    for rx,ry,rot,col in [(225,80,-24,CYAN),(214,86,43,GOLD),(210,92,91,VIOLET)]:
        out.append(f'<ellipse rx="{rx}" ry="{ry}" transform="rotate({rot})" fill="none" stroke="{col}" stroke-opacity=".3" stroke-width="1"/>')
        out.append(f'<ellipse class="orbital-trace" rx="{rx+8}" ry="{ry+5}" transform="rotate({rot})" fill="none" stroke="{col}" stroke-opacity=".12" stroke-dasharray="2 10"/>')
    for a in range(0,360,6):
        rad=math.radians(a)
        r1=245 if a%30 else 239
        out.append(line(math.cos(rad)*r1,math.sin(rad)*r1,math.cos(rad)*250,math.sin(rad)*250,MUTED,.25))
    out += ['<ellipse cy="195" rx="130" ry="24" fill="#132F3C" opacity=".35"/>', '<ellipse cy="195" rx="95" ry="12" fill="none" stroke="#33E6F5" opacity=".25"/>']
    verts = [(x,y,z) for x in [-1,1] for y in [-1,1] for z in [-1,1]]
    def proj(v):
        x,y,z=v
        return ((x-z)*77, (x+z)*36-y*92)
    faces = [(0,1,3,2),(0,2,6,4),(0,1,5,4),(4,5,7,6),(2,3,7,6),(1,3,7,5)]
    for face in faces:
        points=' '.join(f'{proj(verts[i])[0]},{proj(verts[i])[1]}' for i in face)
        out.append(f'<polygon points="{points}" fill="url(#glass)" stroke="url(#edge)" stroke-opacity=".5" stroke-width="1.1"/>')
    for i,v in enumerate(verts):
        x,y=proj(v)
        out += [circle(x,y,7,CYAN,.08),circle(x,y,2.4,CYAN if i%3 else GOLD,.9)]
    out += ['<path d="M0,-72 L56,0 0,72 -56,0Z" fill="url(#glass)" stroke="#33E6F5" stroke-width="1.6"/>',
            '<path d="M0,-72V72 M-56,0H56 M0,-72L20,0 0,72 -20,0Z" fill="none" stroke="#33E6F5" opacity=".45"/>',circle(0,0,23,CYAN,.06),circle(0,0,9,CYAN,.13),circle(0,0,3,WHITE)]
    for x,y,col in [(203,-72,CYAN),(-175,-119,GOLD),(109,167,VIOLET)]:
        out.extend([circle(x,y,9,col,.09),circle(x,y,3,col),line(x,y,x+34,y-20,col,.6)])
    out.append('</g>')
    return ''.join(out)

def hero(mobile=False):
    if mobile:
        w,h=720,910
        b = text(40,49,'AK / THE OBSERVATORY',17,CYAN,500,3,True)
        b += text(40,120,'Aayush Kadam',57,WHITE,650,-2)
        b += text(40,173,'Code. Incentives.',39,WHITE,600,-1)
        b += text(40,222,'Evidence.',39,CYAN,600,-1)
        b += text(40,269,'ENGINEERING / ECONOMICS / ENTREPRENEURSHIP',15,GOLD,400,1,True)
        b += instrument(360,560,.97)
        b += line(40,834,680,834,MUTED,.2)
        b += text(40,871,'BUILD → TEST → QUESTION → REPEAT',17,MUTED,400,1,True)
    else:
        w,h=1200,620
        b = '<rect x="620" y="30" width="550" height="550" fill="url(#grid)" opacity=".2"/>'
        b += text(48,54,'AK / THE OBSERVATORY',15,CYAN,500,3,True)
        b += text(48,152,'Aayush Kadam',58,WHITE,650,-2)
        b += text(48,226,'Code.',62,WHITE,600,-2)
        b += text(48,298,'Incentives.',62,WHITE,600,-2)
        b += text(48,370,'Evidence.',62,CYAN,600,-2)
        b += line(48,409,105,409,GOLD,1,2)
        b += text(48,449,'Engineering / Economics',21,MUTED)
        b += text(48,479,'Entrepreneurship',21,MUTED)
        b += instrument(893,305,.94)
        b += text(694,87,'01 / COMPUTATION',12,MUTED,400,1,True)
        b += text(990,506,'02 / INCENTIVES',12,GOLD,400,1,True)
        b += line(48,550,1152,550,MUTED,.2)
        b += text(48,585,'BUILD → TEST → QUESTION → REPEAT',13,MUTED,400,1.5,True)
        b += text(894,585,'@Aayush-Kadam',14,WHITE,400,1,True)
    return wrap(w,h,'Aayush Kadam — Code. Incentives. Evidence.',b,'Original isometric observatory: a cyan computational core inside glass geometry, precision orbital rings, and gold reference points. Engineering, economics, entrepreneurship.')

def project(kind,num,title,subtitle,color):
    b=text(42,45,f'{num} / SELECTED ENGINEERING',13,color,400,2,True)
    b+=text(42,115,title,45,WHITE,600,-1)
    b+=text(42,165,subtitle,21,MUTED)
    b+=line(42,218,620,218,MUTED,.2)
    b+=text(42,250,{'ghost':'RECORD / REPLAY / BRANCH','epv':'SPECIFY / CHECK / REPLAY','fuzzer':'SEARCH / WITNESS / REPAIR'}[kind],13,color,400,2,True)
    if kind=='ghost':
        for y in [86,136,186]: b+=line(770,y,1120,y,MUTED,.15)
        pts=[(780,136),(850,136),(920,136),(990,86),(1060,86),(990,186),(1060,186)]
        for i,j in [(0,1),(1,2),(2,3),(3,4),(2,5),(5,6)]: b+=line(*pts[i],*pts[j],color,.8,2)
        for x,y in pts: b+=circle(x,y,11,color,.1)+circle(x,y,4,color)
        b+=text(969,56,'BRANCH',11,color,400,1,True)
        b+=text(968,225,'ORIGINAL',11,MUTED,400,1,True)
    elif kind=='epv':
        for i in range(5):
            for j in range(4):
                x,y=811+i*55,61+j*46
                b+=f'<rect x="{x}" y="{y}" width="39" height="30" rx="4" fill="{color}" fill-opacity="{.06+(i+j)%3*.07}" stroke="{color}" stroke-opacity=".3"/>'
        b+='<path d="M855 132L900 172L1004 84" fill="none" stroke="#D9B36C" stroke-width="3"/>'
    else:
        for i in range(6):
            for j in range(4):
                x,y=800+i*53,65+j*45
                b+=line(x,y,x+30,y,color,.25)
                b+=circle(x,y,2,color,.6)
        b+=f'<circle cx="959" cy="155" r="55" fill="{color}" fill-opacity=".08" stroke="{color}"/>'
        b+=line(998,194,1040,236,color,.9,3)+circle(959,155,6,GOLD)
    return wrap(1200,280,title,b,'Conceptual diagram, not a screenshot or a measured result. '+subtitle)

def atlas():
    b=text(42,45,'RESEARCH ATLAS / QUESTIONS, WITH BOUNDARIES',14,GOLD,400,2,True)
    pts=[(145,155),(450,125),(740,165),(1060,125)]
    for a,c in zip(pts,pts[1:]): b+=line(*a,*c,MUTED,.4)
    for i,((x,y),label) in enumerate(zip(pts,['MATCHING','MEMORY','INFORMATION','MECHANISMS'])):
        b+=circle(x,y,28,CYAN if i%2==0 else GOLD,.07)+circle(x,y,6,CYAN if i%2==0 else GOLD)
        b+=text(x-58,y+62,label,13,WHITE,500,1,True)
    b+=text(42,277,'MODEL → COMPUTATION → REPRODUCTION → REVIEW',13,MUTED,400,1.5,True)
    return wrap(1200,315,'Research Atlas',b,'Four connected research themes: matching, memory, information, and mechanisms. Repository descriptions follow in accessible text.')

def main():
    files={'assets/hero/observatory.svg':hero(), 'assets/hero/observatory-mobile.svg':hero(True),
           'assets/projects/ghostframe.svg':project('ghost','01','GhostFrame','Change one observation. Inspect what follows.',CYAN),
           'assets/projects/epv.svg':project('epv','02','Economic Protocol Verifier','Small domains. Explicit assurance.',GOLD),
           'assets/projects/incentive-fuzzer.svg':project('fuzzer','03','Incentive Fuzzer','Give the rule an adversary.',VIOLET),
           'assets/graphics/research-atlas.svg':atlas()}
    for name,content in files.items():
        p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content,encoding='utf-8')
    print(f'Generated {len(files)} original SVGs; {sum(len(s.encode()) for s in files.values()):,} bytes.')

if __name__=='__main__': main()
