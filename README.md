# 🕐 RGB Live Digital Clock

A vibrant, full-screen digital clock built with **Pygame** featuring live weather, auto-detected location, and a retro RGB color scheme.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.0%2B-green?logo=pygame)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Author](https://img.shields.io/badge/Author-gayathrinaiduallu-purple?logo=github)

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Preview](#-preview)
- [Sample Output](#-sample-output)
- [Getting Started](#-getting-started)
- [How Location Works](#-how-location-works)
- [Color Reference](#-color-reference)
- [Project Structure](#-project-structure)
- [Customization](#-customization)
- [Dependencies](#-dependencies)
- [Limitations & Disadvantages](#-limitations--disadvantages)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- [License](#-license)

---

## 📖 About

**RGB Live Digital Clock** is a desktop clock application built with Python and Pygame. It automatically detects your location via IP geolocation and fetches real-time temperature data — no API keys or manual setup required. The clock displays the current time in a colorful retro RGB style with a blinking separator, live weather, and today's date.

> Repository: [github.com/gayathrinaiduallu/RGB-Live-Digital-Clock](https://github.com/gayathrinaiduallu/RGB-Live-Digital-Clock)

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
│  SAT    8 : 4 2 PM      72  °F                           │
│                                                          │
│                      05/23                               │
│                  MONTH  DATE                             │
└──────────────────────────────────────────────────────────┘
```
*(Left: Day/AM-PM in purple | Center: Time in pink/yellow/cyan | Right: Temp & Date in blue)*

---

## 🖥️ Sample Output

### Console / Terminal Output

When you run `python clock.py`, the terminal prints live status messages:

```
[Location] Detected: Austin (30.2672, -97.7431)
[Weather] Temp updated: 84°F (Austin)
[Weather] Temp updated: 83°F (Austin)
```

**What each line means:**

| Line | When it appears | Meaning |
|------|----------------|---------|
| `[Location] Detected: <City> (<lat>, <lon>)` | Once at startup | IP geolocation succeeded |
| `[Location] Detected via ipinfo: ...` | Once at startup | Primary API failed, backup used |
| `[Location] Could not detect. Using default: New York City.` | Once at startup | Both APIs failed, using fallback |
| `[Weather] Temp updated: XX°F (<City>)` | Every 15 minutes | Weather fetch succeeded |
| `[Weather] Fetch Error: <reason>` | If network fails | Old value kept, no crash |

---

### Clock Window Layout

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   SAT      8  :  4  2  PM         84 °F                         │
│                                                                 │
│                                                                 │
│                              05/23                              │
│                          MONTH  DATE                            │
└─────────────────────────────────────────────────────────────────┘
  purple   pink  yel  yel cyan   blue
```

| Panel | Content | Color |
|-------|---------|-------|
| Left | Day of week (`MON`–`SUN`) + AM/PM | Purple |
| Center | Hour digits | Hot pink |
| Center | Blinking `:` separator | Yellow (even sec) / hidden (odd sec) |
| Center right | First minute digit | Yellow |
| Center right | Second minute digit | Cyan |
| Right top | Live temperature + `°F` | Sky blue |
| Right bottom | Date as `MM/DD` + label | Sky blue |

---

### Behavior Notes

- The **colon blinks** every second — visible on even seconds, hidden on odd.
- Temperature shows `--` on startup until the first weather fetch completes (~1–2 sec).
- If `digital.ttf` is missing, falls back to system Arial — functional but less stylized.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/gayathrinaiduallu/RGB-Live-Digital-Clock.git
cd RGB-Live-Digital-Clock

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
├── Digitalclock.py          # Main application
├── requirements.txt  # Python dependencies
├── .gitignore        # Git ignore rules
├── LICENSE           # MIT license
└── README.md
```

---

## 🔧 Customization

Open `clock.py` and tweak these constants:

```python
# Change temperature unit — swap "fahrenheit" to "celsius"
f"&current=temperature_2m&temperature_unit=fahrenheit"

# Change weather refresh interval (seconds)
time.sleep(900)   # 900 = 15 minutes

# Change window size
WIDTH, HEIGHT = 900, 350

# Change colors
PINK   = (240, 32, 190)
YELLOW = (255, 222, 23)
CYAN   = (0, 229, 255)
PURPLE = (176, 38, 255)
BLUE   = (0, 191, 255)
```

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `pygame` | ≥ 2.0.0 | Window, rendering, event loop |
| `requests` | ≥ 2.28.0 | HTTP calls for geolocation & weather |

All weather and location data is fetched from **free, no-key APIs**:
- Weather: [Open-Meteo](https://open-meteo.com/)
- Location: [ip-api.com](http://ip-api.com) / [ipinfo.io](https://ipinfo.io)

---

## ⚠️ Limitations & Disadvantages

### Location Accuracy
- IP geolocation can be inaccurate by **30–100+ miles**, especially on VPNs, mobile networks, or shared ISPs.
- Location is detected **once at startup** — moving or switching networks requires a restart.

### Weather Data
- Temperature updates only every **15 minutes** and may lag behind real conditions.
- Uses Open-Meteo's forecast endpoint — minor discrepancies vs. actual sensor readings possible.
- No additional weather details — no humidity, wind, precipitation, or "feels like."

### Font
- Without `digital.ttf`, falls back to Arial bold — still works but looks less authentic.
- The font file must be sourced and placed manually; it is not included in the repo.

### Platform & Display
- Fixed **900×350 window** — does not scale or go fullscreen automatically.
- No **HiDPI / Retina display** support; may appear blurry on high-resolution screens.
- Desktop only — no web, mobile, or embedded support.

### Network
- Requires internet on startup for location detection; offline launch falls back to New York City.
- Subject to rate limits or downtime of the free third-party APIs.

### Code Structure
- All logic lives in a **single file** — harder to test or extend as the project grows.
- No config file; all changes require editing source code directly.

---

## 🚀 Future Enhancements

### Display & UI
- [ ] **Fullscreen / resizable window** with dynamic layout scaling
- [ ] **Theme switcher** — toggle dark, light, and custom palettes at runtime
- [ ] **HiDPI support** for sharp rendering on Retina and 4K screens
- [ ] **Screensaver mode** — dim after inactivity, brighten on mouse move

### Weather & Location
- [ ] **Manual location override** via config file or CLI (`--city London`)
- [ ] **Celsius / Fahrenheit toggle** with a keypress (`F` key)
- [ ] **Extended weather panel** — humidity, wind speed, weather icons (☀️ 🌧️ ❄️)
- [ ] **"Feels like" temperature** using Open-Meteo's `apparent_temperature` field
- [ ] **Hourly forecast bar** across the bottom showing next 6–12 hours

### Clock & Time
- [ ] **24-hour mode toggle** (`H` key)
- [ ] **Seconds display** as a progress bar or arc
- [ ] **Multiple time zones** — two cities side by side
- [ ] **Alarm / reminder system** — visual flash and sound at set times

### Technical
- [ ] **Config file** (`config.json`) for colors, units, refresh rate — no code edits needed
- [ ] **Modular refactor** — `weather.py`, `location.py`, `renderer.py`
- [ ] **Unit tests** for location parsing and weather fetching
- [ ] **GitHub Actions CI** — lint with `flake8`, run tests on push
- [ ] **Executable builds** via PyInstaller for Windows (`.exe`), macOS (`.app`), Linux binary
- [ ] **Raspberry Pi support** — optimized for small displays like the 7" touchscreen

---

## 👩‍💻 Author

**Gayathri Allu**

- GitHub: [@gayathrinaiduallu](https://github.com/gayathrinaiduallu)
- Repository: [RGB-Live-Digital-Clock](https://github.com/gayathrinaiduallu/RGB-Live-Digital-Clock)

Feel free to open an [issue](https://github.com/gayathrinaiduallu/RGB-Live-Digital-Clock/issues) or submit a [pull request](https://github.com/gayathrinaiduallu/RGB-Live-Digital-Clock/pulls) for bugs, suggestions, or new features!

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.
See the [LICENSE](LICENSE) file for full details.

---

*Built with ❤️ using Python & Pygame*
