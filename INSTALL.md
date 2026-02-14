#!/usr/bin/env python3
"""
Installation and Setup Verification Script
Run this after downloading to ensure everything is properly set up
"""

import sys
import os
from pathlib import Path

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(text.center(70))
    print("=" * 70 + "\n")

def print_section(text):
    """Print a section header"""
    print(f"\n{'─' * 70}")
    print(f"  {text}")
    print(f"{'─' * 70}\n")

def print_step(step_num, text):
    """Print a numbered step"""
    print(f"  {step_num}. {text}")

def show_installation_guide():
    """Show comprehensive installation guide"""
    
    print_header("Valentine's Day Surprise Generator - Installation Guide")
    
    print("This comprehensive tool helps you create and share romantic websites.")
    print("Follow these steps to get started.\n")
    
    print_section("Prerequisites")
    
    print("Before starting, ensure you have:")
    print_step(1, "Python 3.7 or higher")
    print_step(2, "PHP installed and in your PATH")
    print_step(3, "ngrok installed and in your PATH")
    
    print_section("Step 1: Install Python Dependencies")
    
    print("Run this command in the lovesite directory:")
    print("\n  pip install -r requirements.txt\n")
    
    print("This will install:")
    print("  • rich - Beautiful terminal UI")
    print("  • questionary - Interactive prompts")
    print("  • psutil - Process management")
    print("  • requests - HTTP library")
    print("  • qrcode - QR code generation")
    print("  • Pillow - Image processing")
    print("  • pyngrok - ngrok integration")
    
    print_section("Step 2: Install PHP")
    
    print("PHP is required to serve your website locally.\n")
    
    print("[Windows]")
    print("  1. Download from https://www.php.net/downloads.php")
    print("  2. Extract to C:\\php (or your preferred location)")
    print("  3. Add C:\\php to your system PATH")
    print("  4. Restart your terminal")
    print("  5. Verify: php --version\n")
    
    print("[macOS]")
    print("  Install via Homebrew:")
    print("  brew install php")
    print("  Verify: php --version\n")
    
    print("[Linux]")
    print("  Install via package manager:")
    print("  sudo apt-get install php  # Debian/Ubuntu")
    print("  sudo yum install php      # RedHat/CentOS")
    print("  Verify: php --version")
    
    print_section("Step 3: Install ngrok")
    
    print("ngrok exposes your local server to the internet.\n")
    
    print("  1. Download from https://ngrok.com/download")
    print("  2. Extract the file")
    print("  3. Move to a location in your PATH (or use full path)")
    print("  4. Verify: ngrok --version\n")
    
    print("  [Optional] Create free ngrok account:")
    print("  • Sign up at https://ngrok.com")
    print("  • Get your auth token")
    print("  • Run: ngrok config add-authtoken YOUR_TOKEN")
    
    print_section("Step 4: Validate Installation")
    
    print("Run the validation script to ensure everything is installed:\n")
    print("  python validate.py\n")
    
    print("This will check:")
    print("  ✓ Python packages")
    print("  ✓ System tools (PHP, ngrok)")
    print("  ✓ Project files")
    print("  ✓ Module imports")
    
    print_section("Step 5: Run the CLI Tool")
    
    print("Once everything is validated, start the tool:\n")
    print("  python cli.py\n")
    
    print("You'll see a beautiful animated welcome screen and interactive menu!")
    
    print_section("Troubleshooting")
    
    print("[PHP not found]")
    print("  • Ensure PHP is installed: php --version")
    print("  • Check if PHP is in PATH")
    print("  • Use full path if needed: C:\\php\\php.exe --version\n")
    
    print("[ngrok not found]")
    print("  • Ensure ngrok is installed: ngrok --version")
    print("  • Download from https://ngrok.com/download")
    print("  • Add to PATH or use full path\n")
    
    print("[Port already in use]")
    print("  • Tool automatically finds next available port")
    print("  • Check terminal output for actual port used\n")
    
    print("[Python package errors]")
    print("  • Upgrade pip: python -m pip install --upgrade pip")
    print("  • Reinstall: pip uninstall -y -r requirements.txt")
    print("              pip install -r requirements.txt")
    
    print_section("Quick Start")
    
    print("After installation, your typical workflow is:\n")
    print_step(1, "Enter partner's name")
    print_step(2, "Choose a romantic theme")
    print_step(3, "Enter your romantic message")
    print_step(4, "Generate the website")
    print_step(5, "Start local PHP server")
    print_step(6, "Expose with ngrok for public access")
    print_step(7, "Generate QR code for easy sharing")
    print_step(8, "Share the link with your loved one!")
    
    print_section("Features")
    
    print("Your generated website includes:\n")
    print("  ✨ Animated floating hearts")
    print("  ✨ Glowing romantic text")
    print("  ✨ Gradient backgrounds (theme-specific)")
    print("  ✨ Smooth fade-in animations")
    print("  ✨ Parallax mouse effects")
    print("  ✨ Mobile responsive design")
    print("  ✨ Optional background music")
    print("  ✨ Works on all devices")
    
    print_section("Project Structure")
    
    print("""
lovesite/
├── cli.py                    Main CLI entry point
├── config.py                 Configuration and constants
├── animations.py             CLI animations and UI
├── website_generator.py      HTML/CSS/JS generation
├── server_manager.py         PHP server & ngrok
├── validate.py               Validation script
├── advanced_themes.py        Theme configuration
├── setup.py                  Installation script
├── requirements.txt          Python dependencies
├── README.md                 Comprehensive documentation
├── QUICKSTART.md             Quick start guide
├── INSTALL.md                This file
├── .gitignore                Git ignore patterns
├── output/                   Generated website files
└── themes/                   Theme configurations
    """)
    
    print_section("Support & Documentation")
    
    print("For more information, see:")
    print("  • README.md - Full documentation")
    print("  • QUICKSTART.md - Quick start guide")
    print("  • README in output/ - Generated files info")
    
    print_section("Ready to Begin?")
    
    print("Run the validation script first:\n")
    print("  python validate.py\n")
    
    print("Then start the tool when ready:\n")
    print("  python cli.py")
    
    print_header("Happy Valentine's Day! 💕")
    
    print("Follow the on-screen prompts to create and share your surprise website.")
    print("Any questions? See README.md for troubleshooting.")
    print("\nGood luck! 💖\n")

if __name__ == "__main__":
    try:
        show_installation_guide()
    except KeyboardInterrupt:
        print("\n\nInstallation guide closed.")
        sys.exit(0)
