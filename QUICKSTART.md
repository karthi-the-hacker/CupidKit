# Quick Start Guide 🚀

## Installation (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install PHP
- **Windows**: Download from https://www.php.net/downloads.php and add to PATH
- **Mac**: `brew install php`
- **Linux**: `sudo apt-get install php` or `sudo yum install php`

### 3. Install ngrok
- Download from https://ngrok.com/download
- Extract and add to PATH (or use full path when running)

### 4. Verify Installation
```bash
php --version
ngrok --version
```

## Running the Tool

```bash
python cli.py
```

## Full Workflow Example

1. **Start the CLI**
   ```bash
   python cli.py
   ```

2. **Follow the menu**
   - Enter partner's name (e.g., "Sarah")
   - Choose theme (e.g., "Rose")
   - Enter message (e.g., "You mean the world to me")
   - Generate website
   - Start server
   - Expose with ngrok
   - Share the URL!

## Generated Files

All files are created in the `output/` directory:
- `index.html` - Main website
- `styles.css` - Animations and styling
- `script.js` - Interactive animations
- `qrcode.png` - QR code for sharing

## Local Testing

After "Start Server" step, open your browser:
```
http://localhost:8888
```

## Sharing Publicly

After "Expose with ngrok" step, copy the public URL and share with your loved one!

Example: `https://abc123.ngrok.io`

## Troubleshooting

### PHP not found
- Install PHP and add to PATH
- Restart terminal after installation

### ngrok not found
- Download ngrok and extract it
- Add to PATH or use full path
- Free accounts get 2-hour temporary URLs

### Port already in use
- Tool automatically uses next available port
- Check terminal output for actual port

## Features Used

✅ Beautiful CLI with animations
✅ Romantic animated website
✅ Local PHP server hosting
✅ Public ngrok tunneling
✅ QR code generation
✅ Mobile responsive design
✅ Multiple themes
✅ Error handling
✅ Cross-platform compatible

Enjoy! 💕
