def make_whoami():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 170" width="100%">
<defs>
  <filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="860" height="170" fill="#030308"/>
<!-- card bg -->
<rect x="10" y="10" width="840" height="150" rx="6" fill="#050510" stroke="#00FF88" stroke-width="0.8" opacity="0.6"/>
<!-- copy icon -->
<text x="830" y="35" font-family="monospace" font-size="14" fill="#00FF88" opacity="0.4">⧉</text>
<!-- content -->
<text x="35" y="45" font-family="\'Courier New\',monospace" font-size="14" font-weight="bold" fill="#00FF88">MR4BB1T</text>
<text x="35" y="68" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">Developer • Maker • Automation • AI • Embedded Systems</text>
<text x="35" y="90" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">I like taking an idea, breaking it apart, building it,</text>
<text x="35" y="108" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">testing it and turning it into something that actually works.</text>
<text x="35" y="126" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">Software is only one part of the lab.</text>
<text x="35" y="144" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">Hardware, networks, sensors and AI are part of the game.</text>
</svg>'''
    with open('whoami.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def make_jarvis():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 220" width="100%">
<defs>
  <filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="860" height="220" fill="#030308"/>
<rect x="10" y="10" width="840" height="200" rx="6" fill="#050510" stroke="#00FF88" stroke-width="0.8" opacity="0.6"/>
<text x="830" y="35" font-family="monospace" font-size="14" fill="#00FF88" opacity="0.4">⧉</text>

<!-- ASCII diagram left side -->
<text x="35" y="45"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">PC SERVER</text>
<text x="35" y="62"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">   │</text>
<text x="35" y="79"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">   ├── AI / Computer Vision</text>
<text x="35" y="96"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">   ├── Automation</text>
<text x="35" y="113" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">   ├── Cameras</text>
<text x="35" y="130" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">   ├── Sensors</text>
<text x="35" y="147" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">   ├── Network</text>
<text x="35" y="164" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">   └── ESP32 / ESP8266</text>
<text x="35" y="181" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">            │</text>
<text x="35" y="198" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">            ├── Sensors  ├── Actuators  └── Experimental HW</text>

<!-- Right side JARVIS info -->
<line x1="430" y1="20" x2="430" y2="200" stroke="#00FF88" stroke-width="0.5" opacity="0.2"/>
<text x="460" y="50"  font-family="\'Courier New\',monospace" font-size="18" font-weight="bold" fill="#00FF88" filter="url(#glow)">JARVIS</text>
<text x="460" y="76"  font-family="\'Courier New\',monospace" font-size="12" fill="#00FF88" opacity="0.8">A local automation and intelligence</text>
<text x="460" y="94"  font-family="\'Courier New\',monospace" font-size="12" fill="#00FF88" opacity="0.8">ecosystem.</text>
<text x="460" y="122" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">A self-hosted system capable of</text>
<text x="460" y="140" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">connecting software, hardware,</text>
<text x="460" y="158" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">cameras, sensors and automation</text>
<text x="460" y="176" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">into a single ecosystem.</text>
</svg>'''
    with open('jarvis.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def make_build_cards():
    cards = [
        ("01", "EMBEDDED",   "ESP32 / ESP8266\nSensors & Actuators\nDisplays\nWireless\nCustom Controllers\nExperimental"),
        ("02", "AUTOMATION", "Self-hosted Systems\nWeb Automation\nBots / IoT\nHome Automation\nProcess Automation\n"),
        ("03", "AI",         "Local AI\nComputer Vision\nMediaPipe\nOpenCV\nLLM Experiments\nAI-assisted Systems"),
        ("04", "NETWORKS",   "Linux Servers\nNetworking / Wi-Fi\nNetwork Analysis\nVPN / Infrastructure\nSelf-hosted Services\n"),
    ]
    cw, ch = 200, 180
    gap = 20
    total_w = len(cards) * cw + (len(cards)+1) * gap
    total_h = ch + 2*gap
    rects = []
    for i, (num, title, content) in enumerate(cards):
        x = gap + i*(cw+gap)
        y = gap
        rects.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="5" fill="#050510" stroke="#00FF88" stroke-width="0.8" opacity="0.7"/>')
        rects.append(f'<text x="{x+16}" y="{y+30}" font-family="\'Courier New\',monospace" font-size="11" fill="#00FF88" opacity="0.5">{num} —</text>')
        rects.append(f'<text x="{x+16}" y="{y+50}" font-family="\'Courier New\',monospace" font-size="14" font-weight="bold" fill="#00FF88">{title}</text>')
        for j, line in enumerate(content.split('\n')):
            if line:
                rects.append(f'<text x="{x+16}" y="{y+70+j*18}" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">{line}</text>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%">
<rect width="{total_w}" height="{total_h}" fill="#030308"/>
{''.join(rects)}
</svg>'''
    with open('build_cards.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def make_lab_status():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 200" width="100%">
<rect width="860" height="200" fill="#030308"/>
<rect x="10" y="10" width="840" height="180" rx="6" fill="#050510" stroke="#00FF88" stroke-width="0.8" opacity="0.5"/>

<!-- title -->
<rect x="25" y="22" width="12" height="12" rx="2" fill="#00FF88" opacity="0.8"/>
<text x="44" y="33" font-family="\'Courier New\',monospace" font-size="11" fill="#00FF88" font-weight="bold" letter-spacing="2">LAB STATUS</text>

<!-- status rows -->
<text x="35" y="65"  font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">SYSTEM</text>
<text x="160" y="65" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">:</text>
<text x="180" y="65" font-family="\'Courier New\',monospace" font-size="12" fill="#00FF88">ONLINE</text>

<text x="35" y="85"  font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">HARDWARE</text>
<text x="160" y="85" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">:</text>
<text x="180" y="85" font-family="\'Courier New\',monospace" font-size="12" fill="#00FF88">CONNECTED</text>

<text x="35" y="105"  font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">AUTOMATION</text>
<text x="160" y="105" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">:</text>
<text x="180" y="105" font-family="\'Courier New\',monospace" font-size="12" fill="#00FF88">RUNNING</text>

<text x="35" y="125"  font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">AI</text>
<text x="160" y="125" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">:</text>
<text x="180" y="125" font-family="\'Courier New\',monospace" font-size="12" fill="#00FF88">EXPERIMENTAL</text>

<text x="35" y="145"  font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">NETWORK</text>
<text x="160" y="145" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">:</text>
<text x="180" y="145" font-family="\'Courier New\',monospace" font-size="12" fill="#00FF88">MONITORED</text>

<text x="35" y="165"  font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">IDEAS</text>
<text x="160" y="165" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">:</text>
<text x="180" y="165" font-family="\'Courier New\',monospace" font-size="12" fill="#00FF88">TOO MANY</text>

<text x="35" y="185"  font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">SLEEP</text>
<text x="160" y="185" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">:</text>
<text x="180" y="185" font-family="\'Courier New\',monospace" font-size="12" fill="#00FF88">OPTIONAL</text>

<!-- Progress bar -->
<rect x="430" y="165" width="380" height="14" rx="3" fill="#030308" stroke="#00FF88" stroke-width="0.8" opacity="0.5"/>
<rect x="431" y="166" width="377" height="12" rx="2" fill="#00FF88" opacity="0.7">
  <animate attributeName="opacity" values="0.7;0.4;0.7" dur="2s" repeatCount="indefinite"/>
</rect>
<text x="620" y="158" font-family="\'Courier New\',monospace" font-size="11" fill="#00FF88" text-anchor="middle" opacity="0.8">100%</text>
</svg>'''
    with open('lab_status.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

make_whoami()
make_jarvis()
make_build_cards()
make_lab_status()
print("All SVGs generated!")
