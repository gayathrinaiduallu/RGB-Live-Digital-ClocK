import pygame
import sys
import requests
import threading
import time
from datetime import datetime

# ==========================================
# AUTO LOCATION DETECTION
# Uses IP-based geolocation to get your coordinates automatically.
# No manual latitude/longitude needed!
# ==========================================

def get_location():
    """
    Detects current location using IP-based geolocation.
    Returns (latitude, longitude, city_name) or falls back to a default.
    """
    # Method 1: ip-api.com (free, no key needed)
    try:
        response = requests.get("http://ip-api.com/json/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                lat = data["lat"]
                lon = data["lon"]
                city = data.get("city", "Unknown")
                print(f"[Location] Detected: {city} ({lat}, {lon})")
                return lat, lon, city
    except Exception as e:
        print(f"[Location] ip-api.com failed: {e}")

    # Method 2: ipinfo.io (backup)
    try:
        response = requests.get("https://ipinfo.io/json", timeout=5)
        if response.status_code == 200:
            data = response.json()
            loc = data.get("loc", "")
            if "," in loc:
                lat, lon = map(float, loc.split(","))
                city = data.get("city", "Unknown")
                print(f"[Location] Detected via ipinfo: {city} ({lat}, {lon})")
                return lat, lon, city
    except Exception as e:
        print(f"[Location] ipinfo.io failed: {e}")

    # Fallback: Default coordinates (New York City)
    print("[Location] Could not detect location. Using default: New York City.")
    return 40.7128, -74.0060, "New York"


# Detect location at startup
LATITUDE, LONGITUDE, CITY_NAME = get_location()

# Global variable to hold temperature
current_temp = "--"

# Function to fetch live weather in the background
def fetch_weather_bg():
    global current_temp
    # URL is built once using the auto-detected coordinates
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={LATITUDE}&longitude={LONGITUDE}"
        f"&current=temperature_2m&temperature_unit=fahrenheit"
    )

    while True:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                temp_num = round(data['current']['temperature_2m'])
                current_temp = str(temp_num)
                print(f"[Weather] Temp updated: {current_temp}°F ({CITY_NAME})")
        except Exception as e:
            print(f"[Weather] Fetch Error: {e}")
            # Keep the old temperature instead of crashing

        # Wait 15 minutes before refreshing
        time.sleep(900)


# Start the background weather thread BEFORE initializing the window
weather_thread = threading.Thread(target=fetch_weather_bg, daemon=True)
weather_thread.start()

# Initialize Pygame
pygame.init()

# Window Setup
WIDTH, HEIGHT = 900, 350
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"RGB Live Digital Clock — {CITY_NAME}")
clock = pygame.time.Clock()

# Color Definitions
BG_COLOR = (15, 15, 20)
PINK     = (240, 32, 190)
YELLOW   = (255, 222, 23)
CYAN     = (0, 229, 255)
PURPLE   = (176, 38, 255)
BLUE     = (0, 191, 255)

# Fonts
try:
    font_large = pygame.font.Font("digital.ttf", 180)
    font_small = pygame.font.Font("digital.ttf", 50)
    font_sub   = pygame.font.Font("digital.ttf", 25)
except IOError:
    font_large = pygame.font.SysFont("arial", 140, bold=True)
    font_small = pygame.font.SysFont("arial", 45, bold=True)
    font_sub   = pygame.font.SysFont("arial", 20)

# ---- Main Loop ----
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get current time data
    now      = datetime.now()
    day_str  = now.strftime("%a").upper()
    pm_str   = now.strftime("%p")
    hour_str = now.strftime("%I").lstrip('0')
    min_str  = now.strftime("%M")
    date_str = now.strftime("%m/%d")

    # Clear screen
    screen.fill(BG_COLOR)

    # --- Left Panel: Day & AM/PM ---
    day_lbl = font_small.render(day_str, True, PURPLE)
    pm_lbl  = font_small.render(pm_str,  True, PURPLE)
    screen.blit(day_lbl, (40, 90))
    screen.blit(pm_lbl,  (40, 180))

    # --- Center: Main Clock ---
    hour_lbl = font_large.render(hour_str, True, PINK)
    screen.blit(hour_lbl, (180, 70))

    # Blinking colon
    colon_color = YELLOW if now.second % 2 == 0 else BG_COLOR
    colon_lbl = font_large.render(":", True, colon_color)
    screen.blit(colon_lbl, (290, 60))

    min1_lbl = font_large.render(min_str[0], True, YELLOW)
    screen.blit(min1_lbl, (350, 70))

    min2_lbl = font_large.render(min_str[1], True, CYAN)
    screen.blit(min2_lbl, (480, 70))

    # --- Right Panel: Live Temp & Date ---
    temp_lbl = font_large.render(current_temp, True, BLUE)
    temp_lbl = pygame.transform.scale(temp_lbl, (110, 100))
    screen.blit(temp_lbl, (680, 70))

    f_lbl = font_sub.render("°F", True, BLUE)
    screen.blit(f_lbl, (800, 75))

    date_lbl = font_large.render(date_str, True, BLUE)
    date_lbl = pygame.transform.scale(date_lbl, (140, 80))
    screen.blit(date_lbl, (670, 190))

    m_lbl = font_sub.render("MONTH       DATE", True, BLUE)
    screen.blit(m_lbl, (675, 275))

    # Update Display
    pygame.display.flip()
    clock.tick(30)