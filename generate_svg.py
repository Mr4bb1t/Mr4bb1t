import random

width = 800
height = 250
bg_color = "#030308"

stars = []
for _ in range(250):
    x = random.randint(0, width)
    y = random.randint(0, height)
    r = random.choice([1, 1, 1, 2, 2])
    opacity = random.uniform(0.1, 0.9)
    dur = random.uniform(1.5, 5.0)
    stars.append(f'<rect x="{x}" y="{y}" width="{r}" height="{r}" fill="#ffffff" opacity="{opacity}">'
                 f'<animate attributeName="opacity" values="{opacity};0.1;{opacity}" dur="{dur}s" repeatCount="indefinite" />'
                 f'</rect>')

meteors = []
for i in range(20):
    x_start = random.randint(width//2, width + 500)
    y_start = random.randint(-300, height//2)
    length = random.randint(50, 150)
    dur = random.uniform(0.6, 2.0)
    delay = random.uniform(0, 8)
    
    meteors.append(
        f'<line x1="{x_start}" y1="{y_start}" x2="{x_start - length}" y2="{y_start + length}" '
        f'stroke="url(#meteorGrad)" stroke-width="2" opacity="0">'
        f'<animate attributeName="x1" from="{x_start}" to="{x_start - 600}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite" />'
        f'<animate attributeName="y1" from="{y_start}" to="{y_start + 600}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite" />'
        f'<animate attributeName="x2" from="{x_start - length}" to="{x_start - length - 600}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite" />'
        f'<animate attributeName="y2" from="{y_start + length}" to="{y_start + length + 600}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite" />'
        f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.1;0.8;1" dur="{dur}s" begin="{delay}s" repeatCount="indefinite" />'
        f'</line>'
    )

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%">
<defs>
    <linearGradient id="meteorGrad" x1="0%" y1="100%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#ffffff" stop-opacity="1" />
        <stop offset="10%" stop-color="#00FF88" stop-opacity="0.9" />
        <stop offset="100%" stop-color="#00FF88" stop-opacity="0" />
    </linearGradient>
</defs>
<rect width="100%" height="100%" fill="{bg_color}" />
{''.join(stars)}
{''.join(meteors)}
<g transform="translate(400, 125)">
    <text x="0" y="-15" font-family="'Courier New', Courier, monospace" font-size="34" font-weight="900" fill="#00FF88" text-anchor="middle" style="text-shadow: 0 0 10px #00FF88;">MR4BB1T</text>
    <text x="0" y="20" font-family="'Courier New', Courier, monospace" font-size="14" font-weight="bold" fill="#ffffff" opacity="0.8" text-anchor="middle" letter-spacing="3">R4BB1T LABS</text>
</g>
</svg>
"""

with open('meteor_shower.svg', 'w') as f:
    f.write(svg_content)
