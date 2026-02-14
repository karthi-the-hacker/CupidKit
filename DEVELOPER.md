# Developer Guide - Architecture & Extension

## Project Architecture

```
┌─────────────────────────────────────────────────────────┐
│              CLI Application Layer                      │
│  (cli.py - Interactive Menu & User Interface)          │
└──────────────┬────────────────────────────┬─────────────┘
               │                            │
          ┌────▼─────────┐         ┌────────▼──────────┐
          │  Website      │         │  Server Manager   │
          │  Generator    │         │  (ngrok + PHP)    │
          │ (cli.py)      │         │ (server_manager)  │
          └────┬─────────┘         └────────┬──────────┘
               │                            │
      ┌────────▼──────────────┐    ┌───────▼──────────────┐
      │ HTML/CSS/JS           │    │ PHP Server           │
      │ Generation            │    │ Process Management   │
      └────────┬──────────────┘    │ ngrok Tunneling      │
               │                   └──────────────────────┘
          ┌────▼───────────────────────────────────┐
          │  Output Directory                      │
          │  (Generated Website Files)             │
          │  - index.html                          │
          │  - styles.css                          │
          │  - script.js                           │
          │  - qrcode.png                          │
          └─────────────────────────────────────────┘
```

## Module Documentation

### config.py
Configuration and constants management.

**Key Components:**
- `PROJECT_ROOT` - Project root directory path
- `OUTPUT_DIR` - Generated files directory
- `DEFAULT_PORT` - PHP server port (default: 8888)
- `THEMES` - Theme definitions dictionary
- `FILES` - File paths for generated content

**Usage:**
```python
from config import PROJECT_ROOT, THEMES, OUTPUT_DIR

print(THEMES["rose"]["primary"])  # "#E91E63"
print(OUTPUT_DIR)  # /path/to/output
```

### animations.py
CLI UI components and animations.

**Key Functions:**
- `display_welcome_screen()` - Animated welcome
- `animate_generating()` - File generation animation
- `animate_server_starting()` - Server startup animation
- `animate_ngrok_connecting()` - ngrok connection animation
- `display_success_panel(title, content)` - Success message
- `display_error_panel(title, content)` - Error message
- `print_url(public_url)` - Display public URL

**Usage:**
```python
from animations import display_success_panel, print_url

display_success_panel("Success", "Website generated!")
print_url("https://abc123.ngrok.io")
```

### website_generator.py
Website generation engine.

**Main Class: WebsiteGenerator**

```python
from website_generator import WebsiteGenerator

# Create generator instance
gen = WebsiteGenerator(
    partner_name="Sarah",
    message="I love you!",
    theme="rose",
    include_music=True
)

# Generate all files
files = gen.generate_all()

# Or generate individually
gen.generate_html()
gen.generate_css()
gen.generate_js()
qr_path = gen.generate_qr_code("https://public-url.com")
```

**Methods:**
- `generate_html()` - Create HTML file
- `generate_css()` - Create CSS with animations
- `generate_js()` - Create JavaScript animations
- `generate_qr_code(url)` - Create QR code
- `generate_all()` - Generate all files
- `hex_to_rgb(hex)` - Utility to convert hex to RGB

### server_manager.py
Server and ngrok management.

**Main Class: ServerManager**

```python
from server_manager import ServerManager

server = ServerManager()

# PHP server
php_url = server.start_php_server()  # Returns: http://localhost:8888
server.kill_php_server()

# ngrok tunnel
public_url = server.start_ngrok_tunnel()  # Returns: https://abc123.ngrok.io
server.kill_ngrok()

# Check installations
has_php = server.check_php_installed()
has_ngrok = server.check_ngrok_installed()

# Port management
port = server.find_available_port()
```

**Methods:**
- `check_php_installed()` - Check if PHP is available
- `check_ngrok_installed()` - Check if ngrok is available
- `start_php_server(port)` - Start PHP server
- `verify_server(port)` - Verify server is running
- `start_ngrok_tunnel()` - Create ngrok tunnel
- `get_ngrok_public_url()` - Get public URL from API
- `kill_php_server()` - Stop PHP server
- `kill_ngrok()` - Stop ngrok tunnel
- `cleanup()` - Clean up all processes

### cli.py
Main CLI application.

**Main Class: ValentinesCLI**

```python
from cli import ValentinesCLI

app = ValentinesCLI()
app.run()  # Start interactive CLI
```

**Key Methods:**
- `run()` - Main application loop
- `show_welcome()` - Display welcome screen
- `show_main_menu()` - Display main menu
- `input_partner_name()` - Get partner name
- `choose_theme()` - Select theme
- `input_message()` - Get romantic message
- `generate_website()` - Create website files
- `start_server()` - Launch PHP server
- `expose_with_ngrok()` - Create ngrok tunnel
- `generate_qr_code()` - Create QR code
- `cleanup()` - Clean up resources

## Extending the Tool

### Adding a New Theme

**Option 1: Edit config.py**
```python
THEMES = {
    "my_custom_theme": {
        "primary": "#FF0000",
        "secondary": "#00FF00",
        "accent": "#0000FF",
        "background_light": "#FFFFFF",
        "name": "🌈 Custom Theme"
    }
}
```

**Option 2: Extend website_generator.py**
```python
def generate_custom_css(self):
    # Your custom CSS generation
    pass
```

### Adding New Website Features

**1. Modify HTML Template (website_generator.py)**
```python
def generate_html(self):
    html_content = f"""
    ...existing code...
    <div class="custom-section">
        <!-- Your new feature -->
    </div>
    """
```

**2. Add CSS Animations**
```python
def generate_css(self):
    css_content = f"""
    ...existing code...
    
    .custom-section {{
        animation: customAnimation 3s ease-in-out;
    }}
    
    @keyframes customAnimation {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    """
```

**3. Add JavaScript Interactions**
```python
def generate_js(self):
    js_content = """
    ...existing code...
    
    // New feature
    function customFeature() {
        // Implementation
    }
    """
```

### Adding Server Features

**Custom Port Logic**
```python
from server_manager import ServerManager

server = ServerManager()
server.port = 9000  # Custom port
port = server.find_available_port(start_port=9000)
```

**Custom PHP Configuration**
```python
# Edit server_manager.py
cmd = ['php', '-S', f'localhost:{port}', 
       '-t', str(OUTPUT_DIR),
       '-d', 'display_errors=1']  # Add custom options
```

## API Examples

### Complete Workflow

```python
#!/usr/bin/env python3
from website_generator import WebsiteGenerator
from server_manager import ServerManager
import time

# Create website
gen = WebsiteGenerator(
    partner_name="Emma",
    message="You are my everything",
    theme="dark_romance",
    include_music=True
)

# Generate files
files = gen.generate_all()
print(f"Website created: {files['html']}")

# Start server
server = ServerManager()
local_url = server.start_php_server()
print(f"Local URL: {local_url}")

time.sleep(2)

# Expose publicly
try:
    public_url = server.start_ngrok_tunnel()
    print(f"Public URL: {public_url}")
    
    # Generate QR code
    qr_path = gen.generate_qr_code(public_url)
    print(f"QR Code: {qr_path}")
    
    # Keep running
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    server.cleanup()
    print("Cleanup complete")
```

### Programmatic Usage (No UI)

```python
#!/usr/bin/env python3
from website_generator import WebsiteGenerator
from server_manager import ServerManager
from config import OUTPUT_DIR

def create_surprise_website(name, message, theme="rose"):
    """Create a complete surprise website"""
    
    # Generate website
    generator = WebsiteGenerator(name, message, theme)
    files = generator.generate_all()
    
    # Start server
    server = ServerManager()
    local_url = server.start_php_server()
    
    return {
        "local_url": local_url,
        "output_dir": OUTPUT_DIR,
        "files": files,
        "server": server
    }

# Usage
result = create_surprise_website("Alice", "I love you!", "neon_love")
print(f"Local: {result['local_url']}")
print(f"Files: {result['files']}")
```

## Testing

### Unit Testing Example

```python
import unittest
from website_generator import WebsiteGenerator
from config import OUTPUT_DIR

class TestWebsiteGenerator(unittest.TestCase):
    
    def setUp(self):
        self.gen = WebsiteGenerator("Test", "Test message", "rose")
    
    def test_html_generation(self):
        self.gen.generate_html()
        with open(OUTPUT_DIR / "index.html") as f:
            content = f.read()
        self.assertIn("Test", content)
    
    def test_hex_to_rgb(self):
        rgb = self.gen.hex_to_rgb("#FF0000")
        self.assertEqual(rgb, "255,0,0")

if __name__ == '__main__':
    unittest.main()
```

## Performance Optimization

### Generated Website Size
- HTML: ~3KB
- CSS: ~8KB
- JavaScript: ~4KB
- Total: ~15KB (uncompressed)

### Load Time Optimization
- Pure CSS animations (hardware accelerated)
- Minimal JavaScript payload
- Responsive images placeholder
- No external dependencies

### Server Performance
- PHP can handle 1000+ concurrent users
- ngrok suitable for personal/small group use
- For production: use dedicated hosting

## Security Considerations

### Current Implementation
- ✅ No data storage on servers
- ✅ All processing local
- ✅ No third-party tracking
- ✅ No sensitive data in URLs

### Production Hardening
- ✅ Add HTTPS (ngrok provides this)
- ✅ Add rate limiting
- ✅ Sanitize user inputs
- ✅ Add authentication if needed
- ✅ Use environment variables for secrets

## Troubleshooting Guide

### Port Conflicts
```python
from server_manager import ServerManager

server = ServerManager()
# Automatically finds available port
port = server.find_available_port(start_port=8888)
```

### ngrok Authentication
```bash
# Get auth token from https://ngrok.com
ngrok config add-authtoken YOUR_TOKEN
```

### Process Cleanup
```python
import atexit
from server_manager import ServerManager

server = ServerManager()

def cleanup():
    server.cleanup()

atexit.register(cleanup)
```

## Contributing

To extend this tool:
1. Follow the existing code structure
2. Add documentation for new features
3. Test with all themes
4. Test on Windows/Mac/Linux
5. Update README if needed

## License & Credits

MIT License - Use and modify freely!

Created for Valentine's Day 2026 💕
