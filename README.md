# 🕐 RGB Live Digital Clock

A vibrant, full-screen digital clock built with **Pygame** featuring live weather, auto-detected location, and a retro RGB color scheme.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.0%2B-green?logo=pygame)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📋 Table of Contents

- [Features](#-features)
- [Preview](#-preview)
- [Getting Started](#-getting-started)
- [How Location Works](#-how-location-works)
- [Color Reference](#-color-reference)
- [Project Structure](#-project-structure)
- [Customization](#-customization)
- [Dependencies](#-dependencies)
- [Limitations & Disadvantages](#-limitations--disadvantages)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)

---

## ✨ Features

- **Real-time clock** with blinking colon separator
- **Live temperature** — fetches current weather via [Open-Meteo](https://open-meteo.com/) (no API key needed)
- **Auto location detection** — uses IP geolocation, no manual coordinates required
- **RGB color scheme** — pink hours, yellow/cyan minutes, blue weather panel, purple day/AM-PM
- **Optional custom font** — supports `digital.ttf` for an authentic LCD look; gracefully falls back to system fonts
- **Background weather refresh** — updates every 15 minutes without freezing the UI

---

## 📸 Preview

```
┌──────────────────────────────────────────────────────────┐
│  SAT    8 : 4 2      72                                  │
│  PM                  °F                                  │
│                      05/23                               │
│              MONTH       DATE                            │
└──────────────────────────────────────────────────────────┘
```
*(Left: Day/AM-PM in purple | Center: Time in pink/yellow/cyan | Right: Temp & Date in blue)*

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/gayathrinaiduallu/RGB-Live-Digital-ClocK.git
cd rgb-clock

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Add a digital font for the authentic LCD look
#    Download any free "digital" TTF font and place it as:
#    digital.ttf  (in the same folder as clock.py)

# 4. Run the clock
python clock.py
```

---

## 🌍 How Location Works

On startup the app tries two IP geolocation services in order:

| Priority | Service | Notes |
|----------|---------|-------|
| 1 | [ip-api.com](http://ip-api.com) | Free, no key |
| 2 | [ipinfo.io](https://ipinfo.io) | Free tier, no key |
| fallback | New York City (40.71, -74.01) | Used if both fail |

Weather coordinates are set once at launch and reused every refresh cycle.

---

## 🎨 Color Reference

| Element | Color | RGB |
|---------|-------|-----|
| Background | Near-black | `(15, 15, 20)` |
| Hours | Hot pink | `(240, 32, 190)` |
| First minute digit | Yellow | `(255, 222, 23)` |
| Second minute digit | Cyan | `(0, 229, 255)` |
| Day / AM-PM | Purple | `(176, 38, 255)` |
| Temperature & Date | Sky blue | `(0, 191, 255)` |

---

## 🗂 Project Structure

```
RGB-Live-Digital-Clock/
├──DigitalClock.py          # Main application
├── requirements.txt  # Python dependencies
├── .gitignore        # Git ignore rules
├── LICENSE           # MIT license
├── digital.ttf       # (Optional) LCD-style font — add your own
└── README.md
```

---

## 🔧 Customization

Open `DigitalClock.py` and tweak these constants near the top:

```python
# Change temperature unit — swap "fahrenheit" to "celsius" in the URL
f"&current=temperature_2m&temperature_unit=fahrenheit"

# Change refresh interval (seconds)
time.sleep(900)   # 900 = 15 minutes

# Change window size
WIDTH, HEIGHT = 900, 350

# Change colors
PINK   = (240, 32, 190)
YELLOW = (255, 222, 23)
# ... etc.
```

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `pygame` | Window, rendering, event loop |
| `requests` | HTTP calls for geolocation & weather |

All weather and location data is fetched from **free, no-key APIs**.

---

## ⚠️ Limitations & Disadvantages

### Location Accuracy
- IP geolocation can be inaccurate by **30–100+ miles**, especially on mobile networks, VPNs, or shared ISPs. The detected city may not match your actual location.
- Location is detected **once at startup** — if you move or switch networks, you must restart the app.

### Weather Data
- Temperature updates only every **15 minutes**. The displayed value may lag behind real conditions.
- Uses **Open-Meteo's forecast endpoint**, not a real-time sensor, so there can be minor discrepancies vs. actual current conditions.
- No weather details beyond temperature — no humidity, wind, precipitation, or "feels like."

### Font Dependency
- Without `digital.ttf`, the clock falls back to Arial/system fonts which look significantly less authentic. The font file must be sourced and placed manually.

### Platform & Display
- Designed for a **fixed 900×350 window** — does not scale or go fullscreen automatically.
- No **HiDPI / Retina display** support; text may appear blurry on high-resolution screens.
- Runs only as a **desktop app** — no web, mobile, or embedded support.

### Network Dependency
- Requires an active internet connection on startup for location detection. Offline launch always falls back to New York City coordinates.
- Subject to rate limits or downtime of the free third-party geolocation APIs.

### Maintainability
- All logic is in a **single file** (`clock.py`) — harder to test or extend as the project grows.
- No configuration file; all tweaks require editing source code directly.

---

## 🚀 Future Enhancements

### Display & UI
- [ ] **Fullscreen / resizable window** with layout that scales dynamically
- [ ] **Theme switcher** — toggle between dark, light, and custom color palettes at runtime
- [ ] **HiDPI support** for sharp rendering on Retina and 4K screens
- [ ] **Screensaver mode** — dim display after inactivity, brighten on mouse move

### Weather & Location
- [ ] **Manual location override** via a config file or command-line argument (`--city London`)
- [ ] **Celsius / Fahrenheit toggle** with a keypress (e.g. `F` key)
- [ ] **Extended weather panel** — humidity, wind speed, weather icon (☀️ 🌧️ ❄️)
- [ ] **"Feels like" temperature** using Open-Meteo's `apparent_temperature` field
- [ ] **Hourly forecast bar** showing the next 6–12 hours across the bottom

### Clock & Time
- [ ] **24-hour mode toggle** (`H` key)
- [ ] **Second-hand display** as a small progress bar or arc
- [ ] **Multiple time zones** — display two cities side by side
- [ ] **Alarm / reminder system** — set times that trigger a visual flash and sound

### Technical
- [ ] **Config file support** (`config.json` or `config.ini`) for colors, units, refresh rate
- [ ] **Refactor into modules** — `weather.py`, `location.py`, `renderer.py` for better testability
- [ ] **Unit tests** for location parsing and weather fetching
- [ ] **GitHub Actions CI** to lint with `flake8` and run tests on push
- [ ] **Executable builds** via PyInstaller for Windows (`.exe`), macOS (`.app`), Linux binary
- [ ] **Raspberry Pi support** — optimized rendering for small displays like the official 7" touchscreen

---
## 👤 Author

**Gayathri**  
Python Programming Intern — Intern pe (2026) 

## 📄 License

MIT License — feel free to fork, modify, and share.
