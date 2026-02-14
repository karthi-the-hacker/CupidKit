#!/usr/bin/env python3
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

# Advanced theme configuration - optional theme definitions

import json
from pathlib import Path

THEMES_JSON = {
    "rose": {
        "id": "rose",
        "name": "🌹 Rose Theme",
        "description": "Classic romantic rose theme with pink gradients",
        "primary": "#E91E63",
        "secondary": "#FF69B4",
        "accent": "#FFB6D9",
        "background_light": "#FFF0F5",
        "created": "2026-02-14"
    },
    "neon_love": {
        "id": "neon_love",
        "name": "✨ Neon Love Theme",
        "description": "Modern neon theme for tech-savvy lovers",
        "primary": "#FF006E",
        "secondary": "#8338EC",
        "accent": "#3A86FF",
        "background_light": "#0F0E17",
        "created": "2026-02-14"
    },
    "dark_romance": {
        "id": "dark_romance",
        "name": "💎 Dark Romance Theme",
        "description": "Elegant dark theme with deep reds",
        "primary": "#8B0000",
        "secondary": "#DC143C",
        "accent": "#FF69B4",
        "background_light": "#1A1A1A",
        "created": "2026-02-14"
    }
}

def save_theme_configs(output_dir="themes"):
    """Save theme definitions to JSON files"""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    for theme_id, theme_data in THEMES_JSON.items():
        file_path = output_path / f"{theme_id}.json"
        with open(file_path, 'w') as f:
            json.dump(theme_data, f, indent=2)
        print(f"Saved {file_path}")

def load_theme_config(theme_id, config_dir="themes"):
    """Load theme configuration from JSON file"""
    file_path = Path(config_dir) / f"{theme_id}.json"
    if file_path.exists():
        with open(file_path, 'r') as f:
            return json.load(f)
    return THEMES_JSON.get(theme_id)

if __name__ == "__main__":
    save_theme_configs()
