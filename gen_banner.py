import random
import math

random.seed(42)
width = 900
height = 320

# --- Circuit decorations ---
def circuit_lines(n=30):
    lines = []
    for _ in range(n):
        x = random.randint(0, width)
        y = random.randint(0, height)
        length = random.randint(20, 80)
        direction = random.choice(['h', 'v'])
        opacity = random.uniform(0.05, 0.18)
        if direction == 'h':
            lines.append(f'<line x1="{x}" y1="{y}" x2="{x+length}" y2="{y}" stroke="#00FF88" stroke-width="1" opacity="{opacity:.2f}"/>')
            # dot at end
            lines.append(f'<circle cx="{x+length}" cy="{y}" r="2" fill="#00FF88" opacity="{opacity:.2f}"/>')
        else:
            lines.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+length}" stroke="#00FF88" stroke-width="1" opacity="{opacity:.2f}"/>')
            lines.append(f'<circle cx="{x}" cy="{y+length}" r="2" fill="#00FF88" opacity="{opacity:.2f}"/>')
    return '\n'.join(lines)

# --- Small particles/dots ---
def particles(n=60):
    pts = []
    for _ in range(n):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.choice([1, 1, 1, 2])
        opacity = random.uniform(0.05, 0.3)
        pts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#00FF88" opacity="{opacity:.2f}"/>')
    return '\n'.join(pts)

# --- Diagonal corner decorations ---
corner_deco = """
<!-- Top-right corner deco -->
<line x1="820" y1="10" x2="890" y2="10" stroke="#00FF88" stroke-width="1" opacity="0.3"/>
<line x1="890" y1="10" x2="890" y2="80" stroke="#00FF88" stroke-width="1" opacity="0.3"/>
<circle cx="820" cy="10" r="3" fill="#00FF88" opacity="0.5"/>
<!-- Top-left corner deco -->
<line x1="10" y1="10" x2="80" y2="10" stroke="#00FF88" stroke-width="1" opacity="0.3"/>
<line x1="10" y1="10" x2="10" y2="80" stroke="#00FF88" stroke-width="1" opacity="0.3"/>
<circle cx="80" cy="10" r="3" fill="#00FF88" opacity="0.5"/>
<!-- Bottom-right -->
<line x1="820" y1="310" x2="890" y2="310" stroke="#00FF88" stroke-width="1" opacity="0.3"/>
<line x1="890" y1="240" x2="890" y2="310" stroke="#00FF88" stroke-width="1" opacity="0.3"/>
<!-- Bottom-left -->
<line x1="10" y1="310" x2="80" y2="310" stroke="#00FF88" stroke-width="1" opacity="0.3"/>
<line x1="10" y1="240" x2="10" y2="310" stroke="#00FF88" stroke-width="1" opacity="0.3"/>
"""

# --- Button data ---
buttons = [
    ("⊕ GITHUB",   "https://github.com/Mr4bb1t",                    130),
    ("> MR4BB1T",  "https://github.com/Mr4bb1t",                    310),
    ("✦ PROJECTS", "https://github.com/Mr4bb1t?tab=repositories",   490),
    ("⚡ ACTIVE",   "https://github.com/Mr4bb1t",                    670),
]

btn_svgs = []
for label, href, bx in buttons:
    btn_svgs.append(f'''
  <a href="{href}">
    <rect x="{bx}" y="245" width="150" height="36" rx="4"
          fill="#030308" stroke="#00FF88" stroke-width="1" opacity="0.85"/>
    <text x="{bx+75}" y="268" font-family="'Courier New',monospace" font-size="12"
          font-weight="bold" fill="#00FF88" text-anchor="middle"
          letter-spacing="1">{label}</text>
  </a>''')

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {width} {height}" width="100%">
<defs>
  <filter id="glow">
    <feGaussianBlur stdDeviation="4" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="glow2">
    <feGaussianBlur stdDeviation="8" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#010208"/>
    <stop offset="100%" stop-color="#030308"/>
  </linearGradient>
</defs>

<!-- Background -->
<rect width="{width}" height="{height}" fill="url(#bgGrad)"/>

<!-- Circuit decorations -->
{circuit_lines(40)}
{particles(80)}
{corner_deco}

<!-- Subtle horizontal separator line -->
<line x1="150" y1="230" x2="750" y2="230" stroke="#00FF88" stroke-width="0.5" opacity="0.15"/>

<!-- MR4BB1T main title (shadow layer) -->
<text x="{width//2}" y="115" font-family="'Courier New',Courier,monospace"
      font-size="78" font-weight="900" fill="#00FF88" text-anchor="middle"
      opacity="0.15" filter="url(#glow2)">MR4BB1T</text>

<!-- MR4BB1T main title -->
<text x="{width//2}" y="115" font-family="'Courier New',Courier,monospace"
      font-size="78" font-weight="900" fill="#00FF88" text-anchor="middle"
      filter="url(#glow)">MR4BB1T
  <animate attributeName="opacity" values="1;0.85;1" dur="3s" repeatCount="indefinite"/>
</text>

<!-- Subtitle decorators -->
<line x1="220" y1="140" x2="330" y2="140" stroke="#00FF88" stroke-width="1.5" opacity="0.6"/>
<line x1="570" y1="140" x2="680" y2="140" stroke="#00FF88" stroke-width="1.5" opacity="0.6"/>

<!-- Subtitle text -->
<text x="{width//2}" y="148" font-family="'Courier New',Courier,monospace"
      font-size="16" font-weight="700" fill="#00FF88" text-anchor="middle"
      letter-spacing="6" opacity="0.85">R4BB1T LAB</text>

<!-- Power icon -->
<text x="{width//2}" y="185" font-family="sans-serif" font-size="16"
      fill="#00FF88" text-anchor="middle" opacity="0.7">⏻</text>

<!-- Tagline -->
<text x="{width//2}" y="218" font-family="'Courier New',Courier,monospace"
      font-size="13" fill="#00FF88" text-anchor="middle" opacity="0.7"
      letter-spacing="1">Building things that actually do something.</text>

<!-- Buttons -->
{''.join(btn_svgs)}

</svg>
"""

with open('banner.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("banner.svg generated!")
