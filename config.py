#!/usr/bin/env python3

"""
CupidKit - Valentine Surprise Website Generator (CLI Tool)
-----------------------------------------------------------

Author      : Karthikeyan (https://karthithehacker.com)
GitHub      : https://github.com/karthi-the-hacker
Project     : CupidKit - A CLI tool to generate and host beautiful romantic surprise websites for Valentine's Day and special occasions.

License     : Open-source for educational and personal use.

Note to Users:
--------------
💖 This tool is meant for creating romantic surprise web pages for loved ones.
🌐 Generated websites are hosted locally and can be shared publicly using tunneling tools (e.g., ngrok).
❗ If you use or modify this code, PLEASE GIVE PROPER CREDIT to the original author.

Warning to Code Thieves:
------------------------
❌ Removing this header or claiming this project as your own without credit is unethical and against open-source community principles.
🧠 Writing your own code earns respect. Copy-pasting without attribution does not.
✅ Be a respectful developer. Credit the original author and contributors.
"""

# Configuration and constants for CupidKit

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
OUTPUT_DIR = PROJECT_ROOT / "output"
THEMES_DIR = PROJECT_ROOT / "themes"

# Ensure output directory exists
OUTPUT_DIR.mkdir(exist_ok=True)
THEMES_DIR.mkdir(exist_ok=True)

# Server configuration
DEFAULT_PORT = 8888
MAX_PORT_ATTEMPTS = 5

# Ngrok configuration
NGROK_AUTH_TOKEN = None  # Set if you have a paid ngrok account

# Color themes
THEMES = {
    "rose": {
        "primary": "#E91E63",
        "secondary": "#FF69B4",
        "accent": "#FFB6D9",
        "background_light": "#FFF0F5",
        "name": "🌹 Rose Theme"
    },
    "neon_love": {
        "primary": "#FF006E",
        "secondary": "#8338EC",
        "accent": "#3A86FF",
        "background_light": "#0F0E17",
        "name": "✨ Neon Love Theme"
    },
    "dark_romance": {
        "primary": "#8B0000",
        "secondary": "#DC143C",
        "accent": "#FF69B4",
        "background_light": "#1A1A1A",
        "name": "💎 Dark Romance Theme"
    }
}

# File paths
FILES = {
    "index": OUTPUT_DIR / "index.html",
    "styles": OUTPUT_DIR / "styles.css",
    "script": OUTPUT_DIR / "script.js",
    "qrcode": OUTPUT_DIR / "qrcode.png",
}
