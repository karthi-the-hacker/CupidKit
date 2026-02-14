# Valentine's Day Surprise Generator 💕

A CupidKit is a Python CLI tool for generating beautiful romantic animated websites and sharing them publicly with your loved one.

## Features ✨

### Core Features
- ✅ **Beautiful CLI Interface** - Animated welcome screen and interactive menus
- ✅ **Website Generation** - Dynamically generate HTML, CSS, and JavaScript
- ✅ **Romantic Animations** - Floating hearts, glowing text, fade-in effects
- ✅ **Multiple Themes** - Rose, Neon Love, Dark Romance (fully customizable)
- ✅ **Local Hosting** - PHP built-in server for local testing
- ✅ **Public URL** - Ngrok integration for sharing publicly
- ✅ **QR Code** - Generate QR codes for easy sharing
- ✅ **Mobile Responsive** - Works on all devices
- ✅ **Background Music** - Optional autoplay music with consent
- ✅ **Error Handling** - Graceful error handling for missing dependencies
- ✅ **Cross-Platform** - Works on Windows, macOS, and Linux

## Project Structure 📁

```
CupidKit/
├── CupidKit.py                 # Main CLI entry point
├── config.py                   # Configuration and constants
├── animations.py               # CLI animations and UI
├── website_generator.py        # HTML/CSS/JS generation
├── server_manager.py           # PHP server & ngrok management
├── setup.py                    # Setup script
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── output/                     # Generated website files
    ├── index.html
    ├── styles.css
    ├── script.js
    └── qrcode.png
```

## Installation & Setup 🚀

### Prerequisites
- **Python 3.7+**
- **PHP** (for local hosting) - [Download here](https://www.php.net/downloads.php)
- **ngrok** (for public URL) - [Download here](https://ngrok.com/download)

### Step 1: Install Python Dependencies

```bash
# Clone or download the project
cd CupidKit

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Install PHP

#### Windows
1. Download PHP from https://www.php.net/downloads.php
2. Extract to a folder (e.g., `C:\php`)
3. Add PHP to your PATH:
   - Open "Environment Variables"
   - Add `C:\php` to System PATH
   - Restart terminal

#### macOS
```bash
brew install php
```

#### Linux
```bash
sudo apt-get install php
# or
sudo yum install php
```

**Verify PHP installation:**
```bash
php --version
```

### Step 3: Install ngrok

1. Download from https://ngrok.com/download
2. Extract to a folder in your PATH
3. (Optional) Create free ngrok account and authenticate:
   ```bash
   ngrok config add-authtoken YOUR_TOKEN
   ```

**Verify ngrok installation:**
```bash
ngrok --version
```

## Usage 🎯

### Quick Start

```bash
# Run the CLI tool
python CupidKit.py
```

Or if installed via setup.py:
```bash
valentine
```

### CLI Flow

1. **Welcome Screen** - Beautiful animated greeting
2. **Enter Partner Name** - Your loved one's name
3. **Choose Theme** - Select from Rose, Neon Love, or Dark Romance
4. **Enter Message** - Your romantic message (with optional music)
5. **Generate Website** - Creates HTML, CSS, and JS files
6. **Start Server** - Launches local PHP server
7. **Expose with ngrok** - Makes the website publicly accessible
8. **Generate QR Code** - Creates shareable QR code
9. **Share** - Copy the URL or scan the QR code

### Example Session

```
$ python cli.py

❤️  ❤️  ❤️  ❤️  ❤️
❤️ 💕 💕 💕 ❤️
❤️ 💕 💖 💕 ❤️
❤️ 💕 💕 💕 ❤️
❤️  ❤️  ❤️  ❤️  ❤️

💕 Valentine's Day Surprise Generator 💕
✨ Create a beautiful romantic website and share it with your loved one ✨

? What would you like to do?
❤️  ✏️  Enter Partner Name
   🎨 Choose Theme Color
   💌 Enter Romantic Message
   🌐 Generate Website
   🚀 Start Local Server
   🔗 Expose with ngrok
   📱 Generate QR Code
   🔄 Regenerate Website
   ❌ Exit
```

## Features in Detail 📚

### Theme Customization

#### Rose Theme 🌹
- Pink gradient background
- Romantic red accents
- Perfect for classic romance

#### Neon Love Theme ✨
- Dark background with neon colors
- Modern and vibrant
- Great for tech-savvy lovers

#### Dark Romance Theme 💎
- Deep red background
- Mysterious and elegant
- Perfect for sophisticated vibes

### Website Features

**Animated Elements:**
- Floating hearts that continuously fall
- Glowing title with pulsing effect
- Smooth fade-in card animation
- Parallax effect on mouse movement
- Responsive mobile design

**Content:**
- Partner's name in large, elegant font
- Your romantic message
- Animated background
- Optional background music
- Timestamp of creation

### Hosting Options

**Local Testing (PHP Server)**
- Instant testing on your machine
- No internet required
- Perfect for development

**Public Sharing (ngrok)**
- 2-hour duration (free ngrok)
- Permanent URLs (paid ngrok)
- Easy to share via URL or QR code
- Works on all devices

## Architecture 🏗️

### Core Modules

**cli.py**
- Main application entry point
- Menu system and user interactions
- Workflow orchestration

**config.py**
- Configuration constants
- Theme definitions
- File paths

**animations.py**
- CLI UI animations
- Progress indicators
- Panel displays

**website_generator.py**
- Dynamic HTML generation
- CSS with animations
- JavaScript interactions
- QR code generation

**server_manager.py**
- PHP server lifecycle
- ngrok tunnel management
- Port availability checking
- Process monitoring

## Error Handling ⚠️

The tool handles common issues:

### Missing PHP
```
❌ PHP is not installed. Please install PHP from https://www.php.net/downloads.php
```

### Missing ngrok
```
❌ ngrok is not installed on your system.
Download from: https://ngrok.com/download
```

### Port in Use
```
→ Automatically finds next available port
→ No manual configuration needed
```

### Network Issues
```
→ Graceful error messages
→ Suggestions for resolution
→ Automatic cleanup on failure
```

## Bonus Features 🎁

### Multiple Themes
Choose from 3 pre-built themes or customize colors

### QR Code Generation
Generate scannable QR codes for easy mobile access

### Website Regeneration
Update name, message, or theme without restarting server

### Background Music
Optional ambient music with user-controlled autoplay

## Technical Details 🔧

### Technologies Used
- **Python 3.7+** - Backend automation
- **Rich** - Beautiful terminal UI
- **Questionary** - Interactive prompts
- **qrcode** - QR code generation
- **pyngrok** - ngrok integration
- **PHP** - Web server
- **HTML5/CSS3/JavaScript** - Frontend

### Generated Website Stack
- **HTML5** - Semantic markup
- **CSS3** - Advanced animations and gradients
- **JavaScript** - Interactive animations
- **Mobile Responsive** - Works on all devices
- **No Dependencies** - Pure HTML/CSS/JS (fast loading)

## Performance Notes ⚡

- Generated websites are lightweight (~15KB total)
- No external dependencies in generated files
- Fast loading time
- Optimized animations using CSS
- Minimal JavaScript payload

## Troubleshooting 🔍

### PHP Not Starting
```bash
# Check if PHP is in PATH
php --version

# If not, add PHP to PATH or use full path
C:\php\php.exe -S localhost:8888 -t output
```

### ngrok Not Connecting
```bash
# Verify ngrok is installed
ngrok --version

# Check if you have internet connection
# Try authenticating if you have an account
ngrok config add-authtoken YOUR_TOKEN
```

### Port Already in Use
```bash
# Tool automatically finds next available port
# Or manually specify:
php -S localhost:8889 -t output
```

### QR Code Not Generating
```bash
# Ensure qrcode package is installed
pip install qrcode[pil]
```

## Production Deployment 🚀

For permanent deployment:

1. **Use Paid ngrok Account** - For permanent URLs
2. **Deploy to Web Server** - Upload to hosting service
3. **Use Custom Domain** - Set up DNS records
4. **Enable HTTPS** - For security
5. **Add Analytics** - Track visits

## Security Considerations 🔐

- ✅ No data stored on servers
- ✅ All files generated locally
- ✅ No third-party tracking
- ✅ HTTPS support via ngrok
- ✅ Clean URLs without sensitive data

## Customization Guide 🎨

### Change Default Port
Edit `config.py`:
```python
DEFAULT_PORT = 9000  # Change from 8888
```

### Add Custom Theme
Edit `config.py`:
```python
THEMES = {
    "my_theme": {
        "primary": "#FF0000",
        "secondary": "#00FF00",
        "accent": "#0000FF",
        "background_light": "#FFFFFF",
        "name": "🌈 My Theme"
    }
}
```

### Modify Website Layout
Edit `website_generator.py` - Customize the HTML template in `generate_html()` method

### Change Animations
Edit `website_generator.py` - Modify CSS animations in `generate_css()` method

## Keyboard Shortcuts ⌨️

- **Ctrl+C** - Exit the application (graceful shutdown)
- **Ctrl+Z** - Exit on some systems

## License 📄

MIT License - Feel free to use and modify!

## Credits 💌

Created with ❤️ for Valentine's Day

## FAQ ❓

**Q: Can I use this on my phone?**
A: The generated website works on all devices, but the CLI tool requires Python (Windows/Mac/Linux).

**Q: How long does the ngrok URL last?**
A: Free ngrok URLs last 2 hours. Paid accounts get permanent URLs.

**Q: Can I customize the website design?**
A: Yes! Edit the HTML, CSS, and JavaScript templates in `website_generator.py`.

**Q: Is this suitable for production?**
A: The CLI is production-ready, but for permanent hosting, use a dedicated web hosting service.

**Q: Can I add my own assets?**
A: Yes! Modify the website_generator.py to include your own images, fonts, or media.

**Q: What if I have no internet for ngrok?**
A: The local PHP server works without internet. Use it to test locally first.

## Support & Feedback 👥

For issues, suggestions, or contributions:
1. Check the troubleshooting section
2. Review error messages carefully
3. Ensure all prerequisites are installed
4. Try running in administrator mode

## Changelog 📝

### Version 1.0.0
- Initial release
- 3 beautiful themes
- Full ngrok integration
- QR code generation
- Error handling
- Cross-platform support

---

**Happy Valentine's Day! 💕 Share the love! 💕**

Made with ❤️ by your favorite developer

