def card(name, href, tech, line1, line2, line3, tags, is_public=True):
    tag_x = 38
    tag_els = []
    for t in tags:
        tag_els.append(f'<text x="{tag_x}" y="155" font-family="\'Courier New\',monospace" font-size="11" fill="#00FF88" opacity="0.7">{t}</text>')
        tag_x += len(t)*7 + 18

    visibility = "[ public ]" if is_public else "[ public ]"

    return f'''<a href="{href}">
    <rect x="10" y="10" width="840" height="160" rx="6" fill="#050510" stroke="#00FF88" stroke-width="1" opacity="0.7"/>
    <rect x="10" y="10" width="6" height="160" rx="3" fill="#00FF88" opacity="0.8"/>
    <text x="38" y="42" font-family="\'Courier New\',monospace" font-size="17" font-weight="bold" fill="#00FF88" filter="url(#glow)">{name}</text>
    <text x="{38 + len(name)*10 + 16}" y="42" font-family="\'Courier New\',monospace" font-size="11" fill="#8B949E">{tech}</text>
    <text x="38" y="68"  font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">{line1}</text>
    <text x="38" y="88"  font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">{line2}</text>
    <text x="38" y="108" font-family="\'Courier New\',monospace" font-size="12" fill="#C9D1D9">{line3}</text>
    {"".join(tag_els)}
    <text x="810" y="155" font-family="\'Courier New\',monospace" font-size="11" fill="#8B949E" text-anchor="end">{visibility}</text>
  </a>'''

def make_svg(name, href, tech, line1, line2, line3, tags, is_public=True):
    inner = card(name, href, tech, line1, line2, line3, tags, is_public)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 180" width="100%">
<defs>
  <filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="860" height="180" fill="#030308"/>
{inner}
</svg>'''

projects = [
    {
        "file": "project_r4bb1t_fhc.svg",
        "name": "R4BB1T_FHC",
        "href": "https://github.com/Mr4bb1t/R4bb1t_fhc",
        "tech": "C++  •  Arduino  •  ESP32  •  CC1101  •  NRF24L01",
        "line1": "ESP32-based cybersecurity hardware toolkit. Covers WiFi attacks (deauth, beacon spam, captive portal,",
        "line2": "MAC changer), Sub-GHz RF operations (replay attack, raw capture, RF analyzer) via CC1101, and",
        "line3": "2.4GHz NRF24L01 scanning — all driven from a custom on-device menu interface.",
        "tags": ["⚙ Embedded", "📡 RF / Sub-GHz", "🔐 Cybersecurity", "📶 Wi-Fi"],
    },
    {
        "file": "project_blockerspam.svg",
        "name": "BlockerSpam",
        "href": "https://github.com/Mr4bb1t/BlockerSpam",
        "tech": "Kotlin  •  Android SDK 34  •  MVVM  •  Room DB",
        "line1": "Android app that silently intercepts and rejects calls from unknown/unsaved numbers using the",
        "line2": "CallScreeningService API. Logs blocked calls with timestamp, region and carrier. Full dark-mode UI,",
        "line3": "in-app auto-update via GitHub releases, and 100% local data — no cloud dependency.",
        "tags": ["🤖 Android", "🛡 Security", "📱 Mobile", "🔒 Privacy"],
    },
    {
        "file": "project_remotecode.svg",
        "name": "REMOTECODE",
        "href": "https://github.com/Mr4bb1t/RemoteCode",
        "tech": "Python",
        "line1": "Remote code execution tool for running and managing scripts across machines over the network.",
        "line2": "Enables sending, executing and monitoring code on remote targets without physical access —",
        "line3": "useful for automation pipelines, embedded device management and lab control.",
        "tags": ["⚡ Automation", "🌐 Networking", "🖥 Remote Exec"],
    },
    {
        "file": "project_jarvis.svg",
        "name": "JARVIS",
        "href": "https://github.com/Mr4bb1t",
        "tech": "Python  •  OpenCV  •  ESP32  •  Linux  •  MQTT",
        "line1": "Self-hosted automation and AI ecosystem running on a local Linux server. Integrates computer",
        "line2": "vision (OpenCV + MediaPipe), ESP32 sensor networks, camera feeds, automation routines and",
        "line3": "LLM-based control — all managed locally, zero cloud dependency.",
        "tags": ["⚙ Embedded", "🤖 AI / CV", "🌐 Networking", "⚡ Automation"],
        "is_public": False,
    },
]

for p in projects:
    svg = make_svg(
        p["name"], p["href"], p["tech"],
        p["line1"], p["line2"], p["line3"],
        p["tags"], p.get("is_public", True)
    )
    with open(p["file"], "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {p['file']}")

print("Done!")
