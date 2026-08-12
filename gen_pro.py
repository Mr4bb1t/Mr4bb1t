def make_whoami_pro():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 140" width="100%">
<rect width="860" height="140" fill="#030308"/>
<rect x="10" y="10" width="840" height="120" rx="6" fill="#050510" stroke="#00FF88" stroke-width="0.8" opacity="0.6"/>
<text x="35" y="42"  font-family="\'Courier New\',monospace" font-size="13" font-weight="bold" fill="#00FF88">Developer focused on embedded systems, automation and AI-integrated hardware.</text>
<text x="35" y="66"  font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">Building self-hosted systems that connect software, hardware, sensors and AI.</text>
<text x="35" y="88"  font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">Experienced with ESP32/ESP8266, computer vision pipelines, network infrastructure</text>
<text x="35" y="108" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">and full-stack automation from firmware to web interface.</text>
<text x="35" y="128" font-family="\'Courier New\',monospace" font-size="12" fill="#8B949E">📍 Londrina, PR — Brasil</text>
</svg>'''
    with open('whoami.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def make_skills():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 200" width="100%">
<rect width="860" height="200" fill="#030308"/>

<!-- Column 1: Languages -->
<rect x="10"  y="10" width="195" height="180" rx="5" fill="#050510" stroke="#00FF88" stroke-width="0.7" opacity="0.5"/>
<text x="25" y="35" font-family="\'Courier New\',monospace" font-size="11" font-weight="bold" fill="#00FF88" letter-spacing="1">LANGUAGES</text>
<text x="25" y="57"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">Python</text>
<text x="25" y="75"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">C / C++</text>
<text x="25" y="93"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">JavaScript</text>
<text x="25" y="111" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">Bash / Shell</text>
<text x="25" y="129" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">HTML / CSS</text>

<!-- Column 2: Hardware -->
<rect x="220" y="10" width="195" height="180" rx="5" fill="#050510" stroke="#00FF88" stroke-width="0.7" opacity="0.5"/>
<text x="235" y="35" font-family="\'Courier New\',monospace" font-size="11" font-weight="bold" fill="#00FF88" letter-spacing="1">HARDWARE</text>
<text x="235" y="57"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">ESP32 / ESP8266</text>
<text x="235" y="75"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">Arduino</text>
<text x="235" y="93"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">Raspberry Pi</text>
<text x="235" y="111" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">Sensors / Actuators</text>
<text x="235" y="129" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">Serial / I2C / SPI</text>

<!-- Column 3: AI & Vision -->
<rect x="430" y="10" width="195" height="180" rx="5" fill="#050510" stroke="#00FF88" stroke-width="0.7" opacity="0.5"/>
<text x="445" y="35" font-family="\'Courier New\',monospace" font-size="11" font-weight="bold" fill="#00FF88" letter-spacing="1">AI / VISION</text>
<text x="445" y="57"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">OpenCV</text>
<text x="445" y="75"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">MediaPipe</text>
<text x="445" y="93"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">NumPy / Pandas</text>
<text x="445" y="111" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">LLM Integration</text>
<text x="445" y="129" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">Real-time Pipelines</text>

<!-- Column 4: Infra -->
<rect x="640" y="10" width="210" height="180" rx="5" fill="#050510" stroke="#00FF88" stroke-width="0.7" opacity="0.5"/>
<text x="655" y="35" font-family="\'Courier New\',monospace" font-size="11" font-weight="bold" fill="#00FF88" letter-spacing="1">INFRASTRUCTURE</text>
<text x="655" y="57"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">Linux (Debian/Ubuntu)</text>
<text x="655" y="75"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">Docker</text>
<text x="655" y="93"  font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">Git / GitHub</text>
<text x="655" y="111" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">Wi-Fi / TCP/IP</text>
<text x="655" y="129" font-family="\'Courier New\',monospace" font-size="11" fill="#C9D1D9">MQTT / REST APIs</text>
</svg>'''
    with open('skills.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def make_projects():
    # JARVIS project card
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 180" width="100%">
<defs>
  <filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="860" height="180" fill="#030308"/>

<!-- JARVIS card -->
<rect x="10" y="10" width="840" height="160" rx="6" fill="#050510" stroke="#00FF88" stroke-width="1" opacity="0.7"/>
<rect x="10" y="10" width="6" height="160" rx="3" fill="#00FF88" opacity="0.8"/>

<!-- Title + lang -->
<text x="38" y="42" font-family="\'Courier New\',monospace" font-size="17" font-weight="bold" fill="#00FF88" filter="url(#glow)">JARVIS</text>
<text x="120" y="42" font-family="\'Courier New\',monospace" font-size="11" fill="#8B949E">Python  •  OpenCV  •  ESP32  •  Linux  •  MQTT</text>

<!-- Description -->
<text x="38" y="68" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">Self-hosted automation and AI ecosystem running on a local Linux server.</text>
<text x="38" y="88" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">Integrates computer vision (OpenCV + MediaPipe), sensor networks via ESP32/ESP8266,</text>
<text x="38" y="106" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">camera feeds, automation routines and LLM-based control — all managed through a</text>
<text x="38" y="124" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">unified local interface without cloud dependency.</text>

<!-- Stats row -->
<text x="38"  y="155" font-family="\'Courier New\',monospace" font-size="11" fill="#00FF88" opacity="0.7">⚙ Embedded</text>
<text x="140" y="155" font-family="\'Courier New\',monospace" font-size="11" fill="#00FF88" opacity="0.7">🤖 AI / CV</text>
<text x="230" y="155" font-family="\'Courier New\',monospace" font-size="11" fill="#00FF88" opacity="0.7">🌐 Networking</text>
<text x="340" y="155" font-family="\'Courier New\',monospace" font-size="11" fill="#00FF88" opacity="0.7">⚡ Automation</text>
<text x="810" y="155" font-family="\'Courier New\',monospace" font-size="11" fill="#8B949E" text-anchor="end">[ private ]</text>
</svg>'''
    with open('project_jarvis.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

make_whoami_pro()
make_skills()
make_projects()
print("All professional SVGs generated!")
