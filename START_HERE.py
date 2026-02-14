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

# Quick reference guide - start here!

def main():
    print("""
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║  💕 Valentine's Day Surprise Generator - Quick Start 💕           ║
║                                                                    ║
║  A complete, production-ready Python CLI tool for creating        ║
║  beautiful romantic animated websites and sharing them publicly.  ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝

📋 QUICK SETUP (5 minutes):

Step 1: Install Python packages
   → pip install -r requirements.txt

Step 2: Install PHP (if not already installed)
   → Windows: https://www.php.net/downloads.php
   → macOS: brew install php
   → Linux: sudo apt-get install php

Step 3: Install ngrok (if not already installed)
   → Download from: https://ngrok.com/download
   → Extract and add to PATH (or use full path)

Step 4: Validate installation
   → python validate.py

Step 5: Run the CLI tool
   → python cli.py

═══════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'LL GET:

✨ Beautiful romantic website with:
   • Animated floating hearts
   • Glowing text effects
   • Gradient backgrounds
   • Mobile responsive design
   • Optional background music

🌐 Public sharing via:
   • Local PHP server (http://localhost:8888)
   • Public ngrok URL (https://your-url.ngrok.io)
   • Scannable QR code
   • Easy URL sharing

🎨 3 Beautiful Themes:
   • Rose Theme (classic pink)
   • Neon Love Theme (modern & vibrant)
   • Dark Romance Theme (elegant & mystical)

═══════════════════════════════════════════════════════════════════════

📖 DOCUMENTATION:

Main Documentation:
   → README.md - Full guide with all features

Quick Start:
   → QUICKSTART.md - 5-minute setup guide

Installation Help:
   → INSTALL.md - Step-by-step instructions

For Developers:
   → DEVELOPER.md - Technical details & API

Examples:
   → EXAMPLES.md - Sample outputs & usage

Project Summary:
   → PROJECT_SUMMARY.md - Complete overview

═══════════════════════════════════════════════════════════════════════

⚡ QUICK COMMANDS:

Check if everything is installed:
   python validate.py

Run the CLI tool:
   python cli.py

Install Python packages:
   pip install -r requirements.txt

═══════════════════════════════════════════════════════════════════════

❓ TROUBLESHOOTING:

"PHP not found"
   → Install PHP from https://www.php.net/downloads.php
   → Add PHP to your PATH

"ngrok not found"
   → Download from https://ngrok.com/download
   → Extract and add to PATH

"Port already in use"
   → Tool automatically finds next available port
   → No manual configuration needed

═══════════════════════════════════════════════════════════════════════

✅ PROJECT CHECKLIST:

Core Features:
   ✅ Beautiful CLI with animations
   ✅ Interactive menu system
   ✅ Website generation
   ✅ Local PHP server
   ✅ ngrok public access
   ✅ QR code generation
   ✅ Multiple themes
   ✅ Error handling

Documentation:
   ✅ README.md (600+ lines)
   ✅ QUICKSTART.md
   ✅ INSTALL.md
   ✅ DEVELOPER.md
   ✅ EXAMPLES.md
   ✅ PROJECT_SUMMARY.md

Code Quality:
   ✅ 2000+ lines of production code
   ✅ Comprehensive error handling
   ✅ Cross-platform compatible
   ✅ Clean, modular architecture
   ✅ Well-documented

═══════════════════════════════════════════════════════════════════════

🚀 YOUR FIRST RUN:

1. Run validation:
   python validate.py

2. Start the tool:
   python cli.py

3. In the menu, choose:
   ✏️  Enter Partner Name

4. Enter your loved one's name

5. Choose a theme:
   🎨 Choose Theme Color

6. Enter a romantic message:
   💌 Enter Romantic Message

7. Generate the website:
   🌐 Generate Website

8. Start local server:
   🚀 Start Local Server

9. Expose publicly:
   🔗 Expose with ngrok

10. Generate QR code:
    📱 Generate QR Code

11. Share the public URL with your loved one!

═══════════════════════════════════════════════════════════════════════

💡 TIPS:

• Keep the CLI running to maintain the server
• Local URL: http://localhost:8888
• Public URL will be shown automatically
• QR code is saved in output/ directory
• Each regeneration updates the files (server stays running)
• Close with Ctrl+C (graceful shutdown)

═══════════════════════════════════════════════════════════════════════

🎁 BONUS FEATURES:

• Multiple themes (Rose, Neon Love, Dark Romance)
• QR code generation
• Website regeneration
• Background music
• Responsive design
• Animation effects
• Cross-platform support

═══════════════════════════════════════════════════════════════════════

📞 NEED HELP?

1. Check QUICKSTART.md for fast setup
2. See INSTALL.md for detailed installation
3. Read README.md for full documentation
4. Check EXAMPLES.md for sample outputs
5. Review DEVELOPER.md for technical details

═══════════════════════════════════════════════════════════════════════

Ready? Let's create something special! 💕

Run this command to start:

    python cli.py

═══════════════════════════════════════════════════════════════════════

Made with ❤️ for Valentine's Day
    """)

if __name__ == "__main__":
    main()
