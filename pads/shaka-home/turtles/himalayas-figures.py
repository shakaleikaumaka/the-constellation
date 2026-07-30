#!/usr/bin/env python3
"""Generate figure SVGs for dormitory-shade.html (The Himalayas build guide).
Writes /workspace/tmp/him/figN-*.svg + preview.html.
Style: chunky filled shapes, dark night bg (page supplies bg), Turtle Ops palette.
Each SVG is standalone; marker ids are figure-suffixed to avoid collisions when inlined.
Label classes (.lbl .lbl2 .lblw .lblb .lbla .lblg .dim .ttl) come from page CSS.
"""
import os, math

OUT = "/workspace/tmp/him"
os.makedirs(OUT, exist_ok=True)

# palette
WOOD, WOOD_D = "#a07c50", "#7c5f3c"
STEEL, STEEL_D = "#cfd6dc", "#8b97a3"
ALU = "#9fb3c8"          # aluminet silver-blue
ALU_HI = "#c6d4e2"
ORANGE = "#eb5833"; GOLD = "#e5a14b"; AMBER = "#db9840"
AQUA = "#4dd4e8"; OK = "#69db7c"; WARN = "#ffd43b"; BAD = "#ff8787"
GROUND = "#241d16"; NIGHT2 = "#071123"

def svg(fid, vb, body):
    return (f'<svg viewBox="{vb}" role="img" aria-label="figure">\n<defs>\n'
            f'<marker id="ar-{fid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{AQUA}"/></marker>\n'
            f'<marker id="ard-{fid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="#8a7d75"/></marker>\n'
            f'</defs>\n{body}\n</svg>')

def T(x, y, s, cls="lbl", anchor="middle", extra=""):
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{extra}>{s}</text>'

def dim(fid, x1, y1, x2, y2, label, ly=None, lx=None, cls="dim"):
    lx = lx if lx is not None else (x1 + x2) / 2
    ly = ly if ly is not None else y1 - 7
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#8a7d75" stroke-width="1.4" '
            f'marker-start="url(#ard-{fid})" marker-end="url(#ard-{fid})"/>' + T(lx, ly, label, cls))

def arrow(fid, x1, y1, x2, y2, w=2.6, color=AQUA):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" '
            f'marker-end="url(#ar-{fid})"/>')

def human(x, ground_y, h=62, color=GOLD):
    """simple silhouette, feet at (x, ground_y)"""
    H = h
    hr = H * 0.09
    d = (f'M {x-H*0.10} {ground_y} L {x-H*0.055} {ground_y-H*0.44} L {x-H*0.085} {ground_y-H*0.60} '
         f'Q {x-H*0.09} {ground_y-H*0.75} {x-H*0.02} {ground_y-H*0.79} L {x+H*0.02} {ground_y-H*0.79} '
         f'Q {x+H*0.09} {ground_y-H*0.75} {x+H*0.085} {ground_y-H*0.60} L {x+H*0.055} {ground_y-H*0.44} '
         f'L {x+H*0.10} {ground_y} L {x+H*0.045} {ground_y} L {x} {ground_y-H*0.40} L {x-H*0.045} {ground_y} Z')
    return (f'<path d="{d}" fill="{color}"/>'
            f'<circle cx="{x}" cy="{ground_y-H*0.79-hr*1.2:.1f}" r="{hr:.1f}" fill="{color}"/>')

def stake(x, gy, length=34, angle=0, color=STEEL_D, head=True, orange_top=False, w=5):
    """driven stake: visible head above ground + buried dashes below. angle in deg from vertical."""
    a = math.radians(angle)
    dx, dy = math.sin(a), math.cos(a)
    x2, y2 = x + dx * length, gy + dy * length          # buried tip
    xh, yh = x - dx * 10, gy - dy * 10                   # head above ground
    out = [f'<line x1="{xh:.1f}" y1="{yh:.1f}" x2="{x}" y2="{gy}" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>',
           f'<line x1="{x}" y1="{gy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-dasharray="5 4" opacity=".65"/>']
    if head:
        out.append(f'<circle cx="{xh:.1f}" cy="{yh:.1f}" r="4.4" fill="{ORANGE if orange_top else color}"/>')
    return "".join(out)

def ratchet(x1, y1, x2, y2, color="#39424e", w=5):
    """strap line with a ratchet buckle near the low end"""
    mx, my = x1 + (x2 - x1) * 0.72, y1 + (y2 - y1) * 0.72
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<g transform="translate({mx:.1f},{my:.1f}) rotate({ang:.1f})">'
            f'<rect x="-11" y="-6" width="22" height="12" rx="3" fill="#1c232c" stroke="{STEEL_D}" stroke-width="1.6"/></g>')

def post_profile(x, gy, hpx, wpx=14):
    """4x4 wood post, base at (x,gy), eyebolts near top"""
    top = gy - hpx
    eb = top + hpx * 0.06
    return (f'<rect x="{x-wpx/2}" y="{top}" width="{wpx}" height="{hpx}" rx="2" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2"/>'
            f'<circle cx="{x-wpx/2-5}" cy="{eb}" r="5" fill="none" stroke="{STEEL}" stroke-width="3"/>'
            f'<circle cx="{x+wpx/2+5}" cy="{eb+7}" r="5" fill="none" stroke="{STEEL}" stroke-width="3"/>')

figs = {}

# ============================================================ FIG 1 · HERO
fid = "hero"
S = 6.0            # px per ft
GY = 196
def X(ft): return 40 + ft * S
b = []
b.append(f'<rect x="0" y="{GY}" width="920" height="40" fill="{GROUND}"/>')
# --- semi trailer (profile: 8 ft wide face, 13.5-14 ft tall) ---
sx0, sx1 = X(0), X(8)
stop = GY - 13.5 * S - 6
b.append(f'<rect x="{sx0}" y="{GY-8}" width="{sx1-sx0}" height="8" fill="#1c232c"/>')  # undercarriage
b.append(f'<circle cx="{sx0+14}" cy="{GY-4}" r="10" fill="#111a24" stroke="#39424e" stroke-width="3"/>')
b.append(f'<circle cx="{sx1-14}" cy="{GY-4}" r="10" fill="#111a24" stroke="#39424e" stroke-width="3"/>')
b.append(f'<rect x="{sx0}" y="{stop}" width="{sx1-sx0}" height="{GY-14-stop}" rx="3" fill="#39424e" stroke="#4a5563" stroke-width="2"/>')
for i in range(1, 4):
    yy = stop + (GY - 14 - stop) * i / 4
    b.append(f'<line x1="{sx0+3}" y1="{yy:.0f}" x2="{sx1-3}" y2="{yy:.0f}" stroke="#2e3641" stroke-width="2"/>')
b.append(T((sx0+sx1)/2, stop + 30, "SEMI", "lbl2"))
b.append(T((sx0+sx1)/2, stop + 46, "8×53 ft", "dim"))
# keder rail point
ky = GY - 13.5 * S
b.append(f'<circle cx="{sx1}" cy="{ky:.0f}" r="6" fill="{AQUA}"/>')
b.append(T(sx1 - 4, ky - 26, "KEDER RAIL", "lbla", "start"))
b.append(T(sx1 - 4, ky - 12, "@ 13–13.5 ft · installed ✅", "lbl2", "start"))
# --- poles at 75 ft downwind ---
px = X(8 + 75)
ptop = GY - 20 * S
b.append(f'<line x1="{px+7}" y1="{GY}" x2="{px+7}" y2="{ptop+10}" stroke="#5a646f" stroke-width="6" stroke-linecap="round"/>')  # 2nd pole hint
b.append(f'<line x1="{px}" y1="{GY}" x2="{px}" y2="{ptop}" stroke="{STEEL}" stroke-width="7" stroke-linecap="round"/>')
b.append(f'<polygon points="{px-16},{GY} {px+16},{GY} {px},{GY-13}" fill="{WARN}" stroke="#c9a227" stroke-width="1.5"/>')  # yellow base
b.append(stake(px - 26, GY, 26, 6, orange_top=True))
b.append(T(px, ptop - 24, "2× 20-FT ALUMINUM POLES", "lbl"))
b.append(T(px, ptop - 10, "(bought from David — he brings them)", "lbl2"))
# fabric: keder -> pole tops -> ground at 60°
gx = X(8 + 75 + 20)
b.append(f'<path d="M {sx1} {ky:.0f} Q {X(48)} {GY-16.5*S:.0f} {px} {ptop} L {gx:.0f} {GY}" '
         f'fill="none" stroke="{ALU}" stroke-width="7" stroke-linecap="round" opacity=".95"/>')
b.append(f'<path d="M {sx1} {ky+8:.0f} Q {X(48)} {GY-16*S+10:.0f} {px} {ptop+9}" fill="none" stroke="{ALU_HI}" stroke-width="2" opacity=".5"/>')
b.append(T(X(46), GY - 16.5 * S - 14, "shade fabric roof", "lbl2"))
# 60 deg wedge
b.append(f'<path d="M {gx:.0f} {GY} L {gx-34:.0f} {GY} A 34 34 0 0 1 {gx-34+34*math.cos(math.radians(60)):.0f} {GY-34*math.sin(math.radians(60)):.0f}" fill="none" stroke="{WARN}" stroke-width="2"/>')
b.append(T(gx - 48, GY - 14, "60°", "lblw"))
b.append(stake(gx + 12, GY, 22, 0, orange_top=True))
b.append(T(gx + 44, GY + 26, "fabric grounds ~20 ft past poles", "lbl2", "middle"))
# ALPS side post far right
apx = X(136)
b.append(post_profile(apx, GY, 7.5 * S + 10))
cabley = GY - 7.5 * S
b.append(f'<line x1="{gx+30:.0f}" y1="{cabley:.0f}" x2="{apx-12}" y2="{cabley:.0f}" stroke="{STEEL_D}" stroke-width="2.4" stroke-dasharray="8 5"/>')
b.append(ratchet(apx + 6, cabley + 4, apx + 62, GY - 4))
b.append(stake(apx + 62, GY, 26, 5))
b.append(T(apx + 10, cabley - 60, "ALPS-style guyed", "lbl2"))
b.append(T(apx + 10, cabley - 46, "4×4s + steel cable", "lbl2"))
b.append(T(apx + 10, cabley - 32, "carry the sides", "lbl2"))
# human
b.append(human(X(30), GY))
b.append(T(X(30) + 14, GY - 40, "you", "dim", "start"))
# dims
b.append(dim(fid, sx1, GY + 32, px, GY + 32, "75 ft downwind", GY + 46))
b.append(T(452, 30, "THE HIMALAYAS — SEMI-HYBRID PROFILE · dorm footprint 68×122 ft", "ttl"))
figs["fig1-hero"] = svg(fid, "0 0 920 250", "\n".join(b))

# ============================================================ FIG 2 · TRUCKER'S HITCH
fid = "hitch"
b = []
panels = [(20, "1 · SLIPKNOT"), (300, "2 · THROUGH & UP"), (580, "3 · PULL 3:1 + LOCK")]
for px0, ttl in panels:
    b.append(f'<rect x="{px0}" y="34" width="260" height="216" rx="12" fill="{NIGHT2}" stroke="#1f2a38"/>')
    b.append(T(px0 + 130, 56, ttl, "ttl"))
# P1: standing line with slipknot (bight through a loop)
x = 20 + 130
b.append(f'<path d="M {x} 66 L {x} 118" stroke="{GOLD}" stroke-width="5" stroke-linecap="round"/>')
b.append(f'<circle cx="{x}" cy="140" r="20" fill="none" stroke="{GOLD}" stroke-width="5"/>')  # loop
b.append(f'<path d="M {x-6} 128 Q {x-30} 118 {x-34} 140 Q {x-30} 160 {x-8} 152" fill="none" stroke="{AMBER}" stroke-width="5" stroke-linecap="round"/>')  # bight
b.append(f'<path d="M {x} 160 L {x} 232" stroke="{GOLD}" stroke-width="5" stroke-linecap="round"/>')
b.append(T(x - 44, 116, "pull a BIGHT", "lblw", "end"))
b.append(T(x - 44, 130, "through — not", "lbl2", "end"))
b.append(T(x - 44, 144, "the end (quick", "lbl2", "end"))
b.append(T(x - 44, 158, "release later)", "lbl2", "end"))
# P2: line goes around anchor and back up through the bight-loop
x = 300 + 110
b.append(f'<path d="M {x} 66 L {x} 118" stroke="{GOLD}" stroke-width="5" stroke-linecap="round"/>')
b.append(f'<circle cx="{x}" cy="140" r="18" fill="none" stroke="{GOLD}" stroke-width="5"/>')
b.append(f'<circle cx="{x-26}" cy="146" r="12" fill="none" stroke="{AMBER}" stroke-width="5"/>')  # hanging bight
b.append(f'<path d="M {x} 158 L {x} 226" stroke="{GOLD}" stroke-width="5" stroke-linecap="round"/>')
b.append(f'<circle cx="{x}" cy="232" r="8" fill="none" stroke="{STEEL}" stroke-width="4"/>')  # anchor ring
b.append(T(x, 250, "anchor / stake ring", "lbl2"))
b.append(f'<path d="M {x-6} 228 Q {x-52} 210 {x-40} 160 Q {x-38} 150 {x-34} 148" fill="none" stroke="{GOLD}" stroke-width="4.5" stroke-linecap="round"/>')  # working end up through bight
b.append(arrow(fid, x - 34, 148, x - 20, 120, 2.4))
b.append(T(x - 62, 120, "working end UP", "lbla", "end"))
b.append(T(x - 62, 134, "through the bight", "lbla", "end"))
# P3
x = 580 + 110
b.append(f'<path d="M {x} 66 L {x} 118" stroke="{GOLD}" stroke-width="5" stroke-linecap="round"/>')
b.append(f'<circle cx="{x}" cy="140" r="18" fill="none" stroke="{GOLD}" stroke-width="5"/>')
b.append(f'<circle cx="{x-26}" cy="146" r="12" fill="none" stroke="{AMBER}" stroke-width="5"/>')
b.append(f'<path d="M {x} 158 L {x} 226" stroke="{GOLD}" stroke-width="5" stroke-linecap="round"/>')
b.append(f'<circle cx="{x}" cy="232" r="8" fill="none" stroke="{STEEL}" stroke-width="4"/>')
b.append(f'<path d="M {x-6} 228 Q {x-52} 210 {x-40} 160 Q {x-36} 148 {x-30} 146" fill="none" stroke="{GOLD}" stroke-width="4.5" stroke-linecap="round"/>')
b.append(arrow(fid, x + 40, 150, x + 40, 210, 3.2, OK))
b.append(T(x + 48, 182, "PULL —", "lblg", "start"))
b.append(T(x + 48, 196, "3:1 advantage", "lblg", "start"))
b.append(f'<path d="M {x-30} 146 q -14 -8 -8 -20 q 12 -8 16 4" fill="none" stroke="{BAD}" stroke-width="4" stroke-linecap="round"/>')
b.append(f'<path d="M {x-24} 128 q -12 -10 -4 -20 q 12 -6 14 6" fill="none" stroke="{BAD}" stroke-width="4" stroke-linecap="round"/>')
b.append(T(x - 40, 100, "finish: 2 half-hitches", "lblb", "end"))
figs["fig2-hitch"] = svg(fid, "0 0 860 264", "\n".join(b))

# ============================================================ FIG 3 · PARTS STAGING
fid = "parts"
b = []
GY = 196
b.append(f'<rect x="0" y="{GY}" width="1160" height="72" fill="{GROUND}"/>')
def cap(x, l1, l2="", low=False):
    dy = 40 if low else 8
    s = T(x, GY + dy + 10, l1, "lbl2")
    if l2: s += T(x, GY + dy + 24, l2, "dim")
    return s
# post
b.append(post_profile(70, GY, 150, 15))
b.append(cap(70, "4×4×8 posts", "eye bolts @ 7'6\""))
# cable coil
b.append(f'<circle cx="205" cy="{GY-38}" r="30" fill="none" stroke="{STEEL}" stroke-width="7"/>')
b.append(f'<circle cx="205" cy="{GY-38}" r="19" fill="none" stroke="{STEEL_D}" stroke-width="5"/>')
b.append(cap(205, '3/16" 7×19 cable', "thimbles + swages", low=True))
# ratchet strap
b.append(f'<path d="M 310 {GY-8} q 20 -70 46 -84" fill="none" stroke="#39424e" stroke-width="7" stroke-linecap="round"/>')
b.append(f'<rect x="322" y="{GY-52}" width="26" height="15" rx="3" fill="#1c232c" stroke="{STEEL_D}" stroke-width="1.8"/>')
b.append(f'<circle cx="358" cy="{GY-94}" r="6" fill="none" stroke="{STEEL_D}" stroke-width="3.5"/>')
b.append(cap(336, '2" ratchet straps', "w/ loops · 16+"))
# circus stake
b.append(f'<line x1="445" y1="{GY-96}" x2="445" y2="{GY-4}" stroke="{STEEL_D}" stroke-width="7" stroke-linecap="round"/>')
b.append(f'<circle cx="445" cy="{GY-96}" r="6.5" fill="{STEEL}"/>')
b.append(f'<circle cx="445" cy="{GY-82}" r="5" fill="{STEEL}"/>')
b.append(cap(445, 'circus stakes 1"×40"', "2840DH · 30×", low=True))
# welded-washer stake
b.append(f'<line x1="560" y1="{GY-64}" x2="560" y2="{GY-4}" stroke="{STEEL_D}" stroke-width="6" stroke-linecap="round"/>')
b.append(f'<circle cx="560" cy="{GY-64}" r="5.5" fill="{ORANGE}"/>')
b.append(f'<rect x="546" y="{GY-58}" width="28" height="5" rx="2" fill="{STEEL}"/>')
b.append(T(560, GY - 78, "✅ done 7/21", "lblg"))
b.append(cap(560, "welded-washer stakes", "60 + ≥8 plain pins"))
# spring hook (carabiner-ish)
b.append(f'<path d="M 680 {GY-84} a 16 22 0 1 0 0.1 0" fill="none" stroke="{STEEL}" stroke-width="6"/>')
b.append(f'<line x1="667" y1="{GY-74}" x2="676" y2="{GY-56}" stroke="{GOLD}" stroke-width="4"/>')
b.append(cap(680, "spring hooks 3/16\"", "~1000 (!) + 50 big", low=True))
# aluminet bundle
b.append(f'<rect x="790" y="{GY-46}" width="88" height="14" rx="6" fill="{ALU}"/>')
b.append(f'<rect x="796" y="{GY-32}" width="76" height="14" rx="6" fill="{ALU_HI}"/>')
b.append(f'<rect x="790" y="{GY-18}" width="88" height="14" rx="6" fill="{ALU}"/>')
b.append(cap(834, "shade panels 52×52", "roofs + 52×8.5 sides"))
# pole segments
for i, xx in enumerate([944, 962, 980, 998]):
    b.append(f'<rect x="{xx}" y="{GY-78+i*4}" width="10" height="{72-i*4}" rx="4" fill="{STEEL}" stroke="{STEEL_D}" stroke-width="1.6"/>')
b.append(cap(974, "aluminum poles", "DAVID BRINGS 🎁", low=True))
# bowl assembly
b.append(f'<path d="M 1044 {GY-52} q 30 26 60 0 l -8 -18 q -22 16 -44 0 z" fill="{STEEL}" stroke="{STEEL_D}" stroke-width="2"/>')
b.append(f'<rect x="1068" y="{GY-34}" width="12" height="30" rx="3" fill="{STEEL_D}"/>')
b.append(cap(1074, "bowl pole-caps", "confirm w/ David ⚠️"))
figs["fig3-parts"] = svg(fid, "0 0 1160 276", "\n".join(b))

# ============================================================ FIG 4 · SURVEY & LAYOUT (plan)
fid = "layout"
b = []
# plan area: footprint rect
L, Tp, R, Bm = 130, 70, 760, 400   # not to strict scale
b.append(f'<rect x="{L}" y="{Tp}" width="{R-L}" height="{Bm-Tp}" fill="rgba(159,179,200,.07)" stroke="{ALU}" stroke-width="2" stroke-dasharray="10 6"/>')
# semi along top edge
sw = 280
sx = (L + R) / 2 - sw / 2
b.append(f'<rect x="{sx}" y="{Tp-34}" width="{sw}" height="30" rx="4" fill="#39424e" stroke="#4a5563" stroke-width="2"/>')
b.append(T((L+R)/2, Tp - 14, "SEMI 8×53 — keder edge", "lbl2"))
b.append(f'<line x1="{sx}" y1="{Tp-3}" x2="{sx+sw}" y2="{Tp-3}" stroke="{AQUA}" stroke-width="4"/>')
# pole marks
py = Tp + (Bm - Tp) * 0.66
for xx in ((L+R)/2 - 90, (L+R)/2 + 90):
    b.append(f'<circle cx="{xx}" cy="{py}" r="9" fill="none" stroke="{WARN}" stroke-width="3"/>')
    b.append(f'<line x1="{xx-6}" y1="{py-6}" x2="{xx+6}" y2="{py+6}" stroke="{WARN}" stroke-width="3"/>')
b.append(T((L+R)/2 + 40, py + 28, "pole positions — 75 ft downwind of semi", "lblw"))
# fabric ground line
gyl = Tp + (Bm - Tp) * 0.9
b.append(f'<line x1="{L+30}" y1="{gyl}" x2="{R-30}" y2="{gyl}" stroke="{ORANGE}" stroke-width="2.5" stroke-dasharray="4 6"/>')
b.append(T((L+R)/2, gyl + 18, "fabric-to-ground line (~20 ft past poles) — stake row", "lbl2"))
# corner + side posts
for (xx, yy) in [(L, Tp), (R, Tp), (L, py), (R, py), (L, (Tp+py)/2), (R, (Tp+py)/2)]:
    b.append(f'<rect x="{xx-7}" y="{yy-7}" width="14" height="14" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2"/>')
b.append(T(L - 14, (Tp+py)/2 + 4, "guyed 4×4s", "lbl2", "end"))
# paracord template overlay on left half square
tx0, ty0, tx1, ty1 = L, Tp, L + 230, Tp + 230
b.append(f'<polygon points="{tx0},{ty0} {tx1},{ty0} {tx1},{ty1} {tx0},{ty1}" fill="none" stroke="{GOLD}" stroke-width="2.2"/>')
b.append(f'<line x1="{tx0}" y1="{ty0}" x2="{tx1}" y2="{ty1}" stroke="{GOLD}" stroke-width="2.2" stroke-dasharray="7 5"/>')
b.append(f'<line x1="{tx1}" y1="{ty0}" x2="{tx0}" y2="{ty1}" stroke="{GOLD}" stroke-width="2.2" stroke-dasharray="7 5"/>')
b.append(T((tx0+tx1)/2, (ty0+ty1)/2 - 10, "paracord template", "lblw"))
b.append(T((tx0+tx1)/2, (ty0+ty1)/2 + 8, "diagonals EQUAL ±inches", "lbl2"))
# dims
b.append(dim(fid, L, Bm + 24, R, Bm + 24, "122 ft", Bm + 20))
b.append(dim(fid, R + 26, Tp, R + 26, Bm, "", lx=R+26))
b.append(T(R + 38, (Tp+Bm)/2, "68 ft", "dim", "start"))
b.append(T(445, 30, "PLAN VIEW — not to scale · final numbers from David's map on survey day", "ttl"))
figs["fig4-layout"] = svg(fid, "0 0 880 450", "\n".join(b))

# ============================================================ FIG 5 · SET POSTS (SAFETY)
fid = "posts"
b = []
GY = 268
SF = 14  # px/ft
b.append(f'<rect x="0" y="{GY}" width="920" height="40" fill="{GROUND}"/>')
cx = 300
# red no-stake zone ±10 ft
b.append(f'<rect x="{cx-10*SF}" y="{GY}" width="{20*SF}" height="16" fill="rgba(255,135,135,.28)"/>')
b.append(f'<line x1="{cx-10*SF}" y1="{GY}" x2="{cx-10*SF}" y2="{GY+16}" stroke="{BAD}" stroke-width="3"/>')
b.append(f'<line x1="{cx+10*SF}" y1="{GY}" x2="{cx+10*SF}" y2="{GY+16}" stroke="{BAD}" stroke-width="3"/>')
b.append(T(cx, GY + 34, "🚫 NO STAKES CLOSER THAN 10 FT — a camp at 6 ft CRACKED 3 POSTS", "lblb"))
# post
b.append(post_profile(cx, GY, 7.9 * SF, 16))
b.append(T(cx, GY - 7.9 * SF - 10, "4×4 post", "lbl2"))
ey = GY - 7.5 * SF
# straps to stakes at 12 ft
s_l = cx - 12 * SF
s_r = cx + 12 * SF
b.append(ratchet(cx - 8, ey, s_l, GY - 8))
b.append(ratchet(cx - 8, ey + 6, s_l + 34, GY - 6))
b.append(ratchet(cx + 8, ey, s_r, GY - 8))
b.append(stake(s_l, GY, 30, 4, orange_top=True))
b.append(stake(s_l + 34, GY, 30, 4, orange_top=True))
b.append(stake(s_r, GY, 30, -4, orange_top=True))
b.append(T(s_l - 6, GY - 44, "2 toward the", "lbl2", "end"))
b.append(T(s_l - 6, GY - 30, "cable lines", "lbl2", "end"))
b.append(T(s_r + 8, GY - 36, "1 through-post,", "lbl2", "start"))
b.append(T(s_r + 8, GY - 22, "to square center", "lbl2", "start"))
b.append(dim(fid, cx, GY - 116, s_r, GY - 116, "12 ft", GY - 122))
b.append(T(cx, 24, "3 STRAPS PER CORNER POST · STAKES ≥ 10–12 FT OUT", "ttl"))
# inset: stake angles
ix = 640
b.append(f'<rect x="{ix-40}" y="60" width="300" height="118" rx="12" fill="{NIGHT2}" stroke="#1f2a38"/>')
b.append(T(ix + 110, 82, "STAKE ANGLE", "ttl"))
b.append(f'<rect x="{ix-30}" y="158" width="280" height="8" rx="3" fill="{GROUND}"/>')
b.append(stake(ix + 10, 160, 40, 0, color=OK, w=6))
b.append(T(ix + 10, 116, "✅ vertical", "lblg"))
b.append(stake(ix + 105, 160, 40, 8, color=WARN, w=6))
b.append(T(ix + 105, 116, "ok ≤5–10°", "lblw"))
b.append(stake(ix + 205, 160, 40, 45, color=BAD, w=6))
b.append(T(ix + 205, 116, "✗ 45° NO", "lblb"))
# inset: eyebolt stack
b.append(f'<rect x="{ix-40}" y="192" width="300" height="112" rx="12" fill="{NIGHT2}" stroke="#1f2a38"/>')
b.append(T(ix + 110, 214, "EYE BOLT @ 7'6\"", "ttl"))
ey2 = 248
b.append(f'<circle cx="{ix-6}" cy="{ey2}" r="11" fill="none" stroke="{STEEL}" stroke-width="4"/>')
b.append(f'<rect x="{ix+6}" y="{ey2-3}" width="150" height="6" fill="{STEEL_D}"/>')
b.append(f'<rect x="{ix+22}" y="{ey2-16}" width="6" height="32" fill="{STEEL}"/>')
b.append(f'<rect x="{ix+30}" y="{ey2-26}" width="72" height="52" rx="3" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2"/>')
b.append(f'<rect x="{ix+104}" y="{ey2-16}" width="6" height="32" fill="{STEEL}"/>')
b.append(f'<circle cx="{ix+168}" cy="{ey2}" r="11" fill="none" stroke="{STEEL}" stroke-width="4"/>')
b.append(T(ix + 110, 284, "eye – washer – POST – washer – eye nut", "dim"))
b.append(T(ix + 110, 297, "all TIGHT, aligned so load cannot bend the bolt", "dim"))
figs["fig5-posts"] = svg(fid, "0 0 920 322", "\n".join(b))

# ============================================================ FIG 6 · CABLES + SQUARE CHECK (plan)
fid = "square"
b = []
L, Tp, R, Bm = 170, 100, 490, 320
pts4 = [(L, Tp), (R, Tp), (R, Bm), (L, Bm)]
for (x1, y1), (x2, y2) in zip(pts4, pts4[1:] + pts4[:1]):
    b.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{STEEL}" stroke-width="3.4"/>')
# diagonals
b.append(f'<line x1="{L}" y1="{Tp}" x2="{R}" y2="{Bm}" stroke="{AQUA}" stroke-width="2.4" stroke-dasharray="8 6" marker-start="url(#ar-{fid})" marker-end="url(#ar-{fid})"/>')
b.append(f'<line x1="{R}" y1="{Tp}" x2="{L}" y2="{Bm}" stroke="{AQUA}" stroke-width="2.4" stroke-dasharray="8 6" marker-start="url(#ar-{fid})" marker-end="url(#ar-{fid})"/>')
b.append(T((L+R)/2, (Tp+Bm)/2 - 14, "measure BOTH diagonals", "lbla"))
b.append(T((L+R)/2, (Tp+Bm)/2 + 6, "equal within a few inches = square", "lbl2"))
# posts + outward ratchets
guys = {(L, Tp): [(-1, -0.4), (-0.4, -1), (-1, -1)], (R, Tp): [(1, -0.4), (0.4, -1), (1, -1)],
        (R, Bm): [(1, 0.4), (0.4, 1), (1, 1)], (L, Bm): [(-1, 0.4), (-0.4, 1), (-1, 1)]}
for (xx, yy), ds in guys.items():
    for dxx, dyy in ds:
        n = math.hypot(dxx, dyy)
        ex, eyy = xx + dxx / n * 62, yy + dyy / n * 62
        b.append(f'<line x1="{xx}" y1="{yy}" x2="{ex:.0f}" y2="{eyy:.0f}" stroke="#39424e" stroke-width="4"/>')
        b.append(f'<circle cx="{ex:.0f}" cy="{eyy:.0f}" r="4.5" fill="{ORANGE}"/>')
    b.append(f'<rect x="{xx-8}" y="{yy-8}" width="16" height="16" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2"/>')
b.append(T((L+R)/2, Tp - 40, "cables @ 7'6\" · 51'7\" worked on recent builds", "lbl2"))
b.append(T((L+R)/2 + 60, Bm + 78, "ratchet until cables are pretty taut — re-check square AFTER tensioning", "lblw"))
# side note
b.append(T(640, 140, "our hybrid:", "lblw", "start"))
b.append(T(640, 162, "the semi's keder edge", "lbl2", "start"))
b.append(T(640, 180, "replaces one whole", "lbl2", "start"))
b.append(T(640, 198, "cable run — square", "lbl2", "start"))
b.append(T(640, 216, "the field off the rail", "lbl2", "start"))
figs["fig6-square"] = svg(fid, "0 0 880 420", "\n".join(b))

# ============================================================ FIG 7 · SPRING HOOKS / ROOF
fid = "hooks"
b = []
cy = 84
b.append(f'<line x1="40" y1="{cy}" x2="840" y2="{cy}" stroke="{STEEL}" stroke-width="4"/>')
b.append(T(52, cy - 16, "steel cable", "lbl2", "start"))
# aluminet sheet
b.append(f'<polygon points="60,{cy+26} 820,{cy+26} 800,220 80,220" fill="rgba(159,179,200,.16)" stroke="{ALU}" stroke-width="2"/>')
for i in range(6):
    xx = 120 + i * 120
    b.append(f'<line x1="{xx}" y1="{cy+34}" x2="{xx-12}" y2="212" stroke="{ALU_HI}" stroke-width="1" opacity=".4"/>')
b.append(T(400, 196, "52×52 roof panel — spread it out UNDER the square first", "lbl2"))
# grommets + hooks
for i in range(10):
    xx = 100 + i * 68
    if i >= 8:  # skip cornermost
        b.append(f'<circle cx="{xx}" cy="{cy+30}" r="6" fill="none" stroke="{STEEL_D}" stroke-width="2.5"/>')
        continue
    b.append(f'<circle cx="{xx}" cy="{cy+30}" r="6" fill="none" stroke="{GOLD}" stroke-width="3"/>')
    # hook: small oval from grommet to cable, gate at bottom
    b.append(f'<path d="M {xx} {cy+24} C {xx-9} {cy+12} {xx-9} {cy+2} {xx} {cy-4} C {xx+9} {cy+2} {xx+9} {cy+12} {xx} {cy+24}" fill="none" stroke="{STEEL}" stroke-width="3.4"/>')
    b.append(f'<line x1="{xx-5}" y1="{cy+16}" x2="{xx+1}" y2="{cy+22}" stroke="{WARN}" stroke-width="2.6"/>')
b.append(T(790, cy + 56, "✗ skip the cornermost few", "lblb", "end"))
b.append(T(790, cy + 72, "grommets if too tight —", "lbl2", "end"))
b.append(T(790, cy + 88, "corners carry too much stress", "lbl2", "end"))
b.append(T(240, 40, "ALL HOOKS SAME DIRECTION · OPENING FACING DOWN", "ttl", "middle"))
b.append(arrow(fid, 168, 52, 140, 96))
figs["fig7-hooks"] = svg(fid, "0 0 880 240", "\n".join(b))

# ============================================================ FIG 8 · SIDES
fid = "sides"
b = []
GY = 270
b.append(f'<rect x="0" y="{GY}" width="640 " height="30" fill="{GROUND}"/>')
b.append(post_profile(140, GY, 160, 15))
cy2 = GY - 150
b.append(f'<line x1="140" y1="{cy2}" x2="600" y2="{cy2}" stroke="{STEEL}" stroke-width="3.4"/>')
b.append(T(596, cy2 - 12, "cable @ 7'6\"", "lbl2", "end"))
# side panel slanting out
b.append(f'<polygon points="185,{cy2+6} 585,{cy2+6} 545,{GY-6} 145,{GY-6}" fill="rgba(159,179,200,.16)" stroke="{ALU}" stroke-width="2"/>')
for i in range(7):
    xx = 185 + i * 60
    b.append(f'<path d="M {xx} {cy2+8} C {xx-6} {cy2+60} {xx-14} {GY-60} {xx-38} {GY-8}" fill="none" stroke="{ALU_HI}" stroke-width="1" opacity=".45"/>')
b.append(T(385, (cy2+GY)/2, "52 × 8.5 ft side — hangs from cable, slants outward", "lbl2"))
# 3in offset arrow
b.append(arrow(fid, 150, cy2 - 34, 183, cy2 + 2))
b.append(T(150, cy2 - 44, 'start hooks 3" in from each end = a little slack', "lblw", "start"))
# unstaked bottom
b.append(f'<line x1="145" y1="{GY-4}" x2="545" y2="{GY-4}" stroke="{BAD}" stroke-width="2.4" stroke-dasharray="6 6"/>')
b.append(T(345, GY + 22, "bottom edge NOT staked yet — that comes after the roof is up", "lblb"))
figs["fig8-sides"] = svg(fid, "0 0 640 310", "\n".join(b))

# ============================================================ FIG 9 · RAISE THE ROOF
fid = "raise"
b = []
GY = 330
b.append(f'<rect x="0" y="{GY}" width="920" height="36" fill="{GROUND}"/>')
px = 430
ptop = GY - 250
# fabric bulge
b.append(f'<path d="M 60 {GY-140} Q {px} {ptop-58} 860 {GY-140}" fill="none" stroke="{ALU}" stroke-width="6" opacity=".9"/>')
b.append(T(760, GY - 176, "roof pushed up ~15 ft", "lbl2"))
# pole: 4 segments
seg = 250 / 4
for i in range(4):
    y0 = GY - (i + 1) * seg
    col = STEEL if i % 2 == 0 else "#aeb9c4"
    b.append(f'<rect x="{px-6}" y="{y0:.0f}" width="12" height="{seg:.0f}" rx="3" fill="{col}" stroke="{STEEL_D}" stroke-width="1.6"/>')
b.append(T(px + 20, GY - 120, "4 segments ≈ 15 ft", "lbl2", "start"))
# bowl on top
b.append(f'<path d="M {px-26} {ptop-6} q 26 20 52 0 l -7 -14 q -19 12 -38 0 z" fill="{STEEL}" stroke="{STEEL_D}" stroke-width="2"/>')
b.append(T(px, ptop - 30, "bowl assembly cap (confirm w/ David)", "lbl2"))
# guy ring + harness
ry = GY - 158
b.append(f'<circle cx="{px}" cy="{ry}" r="12" fill="none" stroke="{GOLD}" stroke-width="4.5"/>')
b.append(T(px - 20, ry + 4, "guy ring", "lblw", "end"))
# lines: 28' to neighbor ring (left), 2x20' to side cables, 17' corner
b.append(f'<line x1="{px-12}" y1="{ry}" x2="120" y2="{ry+6}" stroke="{GOLD}" stroke-width="2.6"/>')
b.append(f'<circle cx="112" cy="{ry+6}" r="10" fill="none" stroke="{GOLD}" stroke-width="3.5" opacity=".6"/>')
b.append(f'<line x1="112" y1="{ry+16}" x2="112" y2="{GY}" stroke="#5a646f" stroke-width="7" opacity=".5"/>')
b.append(T(250, ry - 10, "28' → next pole's ring", "lblw"))
b.append(f'<line x1="{px+10}" y1="{ry+7}" x2="740" y2="{GY-105}" stroke="{GOLD}" stroke-width="2.6"/>')
b.append(f'<line x1="{px+8}" y1="{ry+10}" x2="660" y2="{GY-60}" stroke="{GOLD}" stroke-width="2.6"/>')
b.append(f'<line x1="740" y1="{GY-105}" x2="820" y2="{GY-105}" stroke="{STEEL}" stroke-width="3"/>')
b.append(f'<line x1="628" y1="{GY-60}" x2="700" y2="{GY-60}" stroke="{STEEL}" stroke-width="3"/>')
b.append(T(700, GY - 128, "2× 20' → steel cables", "lblw"))
b.append(f'<line x1="{px-9}" y1="{ry+9}" x2="230" y2="{GY-40}" stroke="{GOLD}" stroke-width="2.2" stroke-dasharray="6 5"/>')
b.append(T(240, GY - 22, "17' corner line — adjust after sides are grounded", "lbl2"))
# humans
b.append(human(px - 46, GY))
b.append(human(px + 52, GY, 58))
b.append(T(px - 120, GY + 24, "lift 5 ft ⬆", "dim", "end"))
b.append(T(px + 130, GY + 24, "buddy slots next segment in", "dim", "start"))
b.append(T(px + 130, GY - 20, "🧤 GLOVES ON — always", "lblw", "start"))
# base
b.append(f'<rect x="{px-22}" y="{GY-6}" width="44" height="7" rx="3" fill="#5b4a3a"/>')
b.append(T(px, GY + 44, "base: carpet square / wood + rebar (ALPS) · ours: David's yellow bases + welded-washer stake nails", "dim"))
b.append(T(430, 26, "THE SPREADER-POLE HARNESS — ONE UPRIGHT UNIT THE WIND CAN'T WALK", "ttl"))
figs["fig9-raise"] = svg(fid, "0 0 920 390", "\n".join(b))

# ============================================================ FIG 10 · GROUND THE SIDES
fid = "ground"
b = []
GY = 190
b.append(f'<rect x="0" y="{GY}" width="880" height="36" fill="{GROUND}"/>')
# aluminet bottom band
b.append(f'<polygon points="40,40 840,40 820,{GY-46} 60,{GY-46}" fill="rgba(159,179,200,.16)" stroke="{ALU}" stroke-width="2"/>')
b.append(T(440, 90, "side panel — bottom edge", "lbl2"))
# grommets + loops + stakes
for i, xx in enumerate(range(110, 800, 96)):
    yy = GY - 50
    b.append(f'<circle cx="{xx}" cy="{yy}" r="7" fill="none" stroke="{GOLD}" stroke-width="3"/>')
    if i == 4:
        # BAD example: stake straight through grommet
        b.append(f'<line x1="{xx}" y1="{yy-8}" x2="{xx}" y2="{GY+14}" stroke="{BAD}" stroke-width="5" stroke-linecap="round"/>')
        b.append(T(xx, yy - 22, "✗ NEVER through", "lblb"))
        b.append(T(xx, yy - 8 - 0, "", "lblb"))
        b.append(T(xx, GY + 32, "grommet or fabric", "lblb"))
        continue
    # paracord loop
    b.append(f'<path d="M {xx-6} {yy+4} Q {xx-14} {GY-16} {xx} {GY-8} Q {xx+14} {GY-16} {xx+6} {yy+4}" fill="none" stroke="{AMBER}" stroke-width="3.4"/>')
    # J stake through loop
    b.append(f'<path d="M {xx-10} {GY-14} L {xx-10} {GY+16} q 0 8 8 8" fill="none" stroke="{OK}" stroke-width="4.5" stroke-linecap="round"/>')
b.append(T(160, GY + 34, '✅ stake through the PARACORD LOOP', "lblg", "start"))
b.append(dim(fid, 302, 56, 398, 56, 'every 12–18"', 50))
figs["fig10-ground"] = svg(fid, "0 0 880 240", "\n".join(b))

# ============================================================ FIG 11 · ANTI-OSCILLATION
fid = "osc"
b = []
GY = 250
b.append(f'<rect x="0" y="{GY}" width="900" height="34" fill="{GROUND}"/>')
# LEFT: exterior midspan support
b.append(T(230, 34, "EXTERIOR MIDSPAN SUPPORT (windward)", "ttl"))
b.append(post_profile(80, GY, 160, 14))
b.append(post_profile(390, GY, 160, 14))
b.append(f'<path d="M 80 {GY-150} Q 235 {GY-118} 390 {GY-150}" fill="none" stroke="{STEEL}" stroke-width="3"/>')
mx = 235
b.append(f'<rect x="{mx-5}" y="{GY-142}" width="10" height="142" rx="3" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2"/>')
b.append(f'<path d="M {mx-9} {GY-140} q 9 -12 18 0" fill="none" stroke="{STEEL_D}" stroke-width="3.5"/>')  # hook trapping cable
b.append(f'<line x1="{mx}" y1="{GY-134}" x2="{mx+52}" y2="{GY-4}" stroke="{GOLD}" stroke-width="2.6"/>')
b.append(stake(mx + 52, GY, 24, 5))
b.append(T(mx + 66, GY - 40, "line/ratchet down", "lbl2", "start"))
b.append(T(mx + 66, GY - 26, "to 18\" J-hook stake", "lbl2", "start"))
b.append(T(mx, GY - 152, "2×4 pushes cable UP", "lblw"))
b.append(arrow(fid, mx - 40, GY - 96, mx - 12, GY - 128))
# RIGHT: interior tiedown
b.append(T(700, 34, "INTERIOR CABLE TIEDOWN", "ttl"))
b.append(f'<path d="M 560 {GY-150} Q 700 {GY-124} 840 {GY-150}" fill="none" stroke="{STEEL}" stroke-width="3"/>')
tx = 700
b.append(f'<line x1="{tx}" y1="{GY-128}" x2="{tx+58}" y2="{GY-2}" stroke="{GOLD}" stroke-width="2.6"/>')
b.append(stake(tx + 58, GY, 24, 6))
b.append(arrow(fid, tx + 108, GY - 96, tx + 66, GY - 48))
b.append(T(892, GY - 116, "OFFSET the stake a few feet —", "lbl2", "end"))
b.append(T(892, GY - 102, "never pull straight up on it", "lbl2", "end"))
b.append(T(700, GY - 160, "aluminet pulls interior cables UP — tie them down", "lbl2"))
b.append(T(450, GY + 26, "trucker's-hitch everything taut · watch each wall in the first big wind", "lblw"))
figs["fig11-osc"] = svg(fid, "0 0 900 300", "\n".join(b))

# ============================================================ FIG 12 · FINAL CHECKS
fid = "check"
b = []
GY = 210
b.append(f'<rect x="0" y="{GY}" width="560 " height="30" fill="{GROUND}"/>')
b.append(post_profile(150, GY, 160, 15))
b.append(f'<line x1="150" y1="{GY-176}" x2="150" y2="{GY+8}" stroke="{OK}" stroke-width="1.8" stroke-dasharray="6 5"/>')
b.append(T(150, GY - 186, "plumb ✅", "lblg"))
b.append(f'<rect x="196" y="{GY-120}" width="52" height="16" rx="6" fill="#39424e" stroke="{STEEL_D}" stroke-width="2"/>')
b.append(f'<circle cx="222" cy="{GY-112}" r="4" fill="{OK}"/>')
b.append(T(224, GY - 130, "level on two faces", "lbl2"))
b.append(T(400, 80, "posts take load best", "lbl2"))
b.append(T(400, 98, "STRAIGHT up-and-down —", "lblw"))
b.append(T(400, 116, "adjust ratchets, or loosen +", "lbl2"))
b.append(T(400, 134, "tap the base with a sledge", "lbl2"))
b.append(T(280, GY + 24, "5 minutes. every day. and after every blow. 🐢", "lblg"))
figs["fig12-check"] = svg(fid, "0 0 560 250", "\n".join(b))

# ---------------- write ----------------
for name, content in figs.items():
    with open(f"{OUT}/{name}.svg", "w") as f:
        f.write(content)
    print(name, len(content))

prev = ['<!DOCTYPE html><html><head><style>',
        "body{background:#030915;font-family:sans-serif} .fig{background:#071123;border:1px solid #1f2a38;border-radius:12px;padding:10px;margin:14px auto;max-width:900px}",
        "svg{width:100%;height:auto;display:block}",
        "svg .ttl{fill:#8a7d75;font:700 12px monospace;letter-spacing:.08em}",
        "svg .lbl{fill:#f7f0eb;font:700 14px sans-serif}",
        "svg .lbl2{fill:#ddd6d1;font:600 12.5px sans-serif}",
        "svg .lblw{fill:#ffd43b;font:700 13px sans-serif}",
        "svg .lblb{fill:#ff8787;font:700 13px sans-serif}",
        "svg .lbla{fill:#4dd4e8;font:700 13px sans-serif}",
        "svg .lblg{fill:#69db7c;font:700 13px sans-serif}",
        "svg .dim{fill:#8a7d75;font:600 11px monospace}",
        "h3{color:#ddd}",
        "</style></head><body>"]
for name in figs:
    prev.append(f"<h3>{name}</h3><div class='fig'>{figs[name]}</div>")
prev.append("</body></html>")
with open(f"{OUT}/preview.html", "w") as f:
    f.write("\n".join(prev))
print("preview written")
