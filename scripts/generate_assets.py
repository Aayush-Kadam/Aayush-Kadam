"""Original project and research artwork. Standard-library deterministic SVG."""
from pathlib import Path
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
<rect width="{w}" height="{h}" rx="20" fill="{BG}"/>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="20" fill="none" stroke="#2B3A50"/>
{body}</svg>'''

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
    files={'assets/projects/ghostframe.svg':project('ghost','01','GhostFrame','Change one observation. Inspect what follows.',CYAN),
           'assets/projects/epv.svg':project('epv','02','Economic Protocol Verifier','Small domains. Explicit assurance.',GOLD),
           'assets/projects/incentive-fuzzer.svg':project('fuzzer','03','Incentive Fuzzer','Give the rule an adversary.',VIOLET),
           'assets/graphics/research-atlas.svg':atlas()}
    for name,content in files.items():
        p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content,encoding='utf-8')
    print(f'Generated {len(files)} original SVGs; {sum(len(s.encode()) for s in files.values()):,} bytes.')

if __name__=='__main__': main()
