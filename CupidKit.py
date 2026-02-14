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

import sys
import time
import questionary
from pathlib import Path
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich import box
from rich.table import Table

from animations import (
    display_welcome_screen, animate_generating, animate_server_starting,
    animate_ngrok_connecting, display_success_panel, display_error_panel,
    display_info_panel, print_url, print_qr_code_info
)
from website_generator import WebsiteGenerator
from server_manager import ServerManager
from config import THEMES, OUTPUT_DIR

console = Console()


class ValentinesCLI:
    """Main CLI application"""
    
    def __init__(self):
        self.partner_name = None
        self.message = None
        self.theme = "rose"
        self.include_music = False
        self.server = ServerManager()
        self.website_generator = None
        self.public_url = None
    
    def run(self):
        """Main application flow"""
        try:
            self.show_welcome()
            
            while True:
                self.show_main_menu()
        
        except KeyboardInterrupt:
            console.print("\n[yellow]Exiting...[/yellow]")
            self.cleanup()
            sys.exit(0)
        except Exception as e:
            display_error_panel("Error", str(e))
            self.cleanup()
            sys.exit(1)
    
    def show_welcome(self):
        """Display welcome screen"""
        display_welcome_screen()
    
    def show_main_menu(self):
        """Show main menu and handle user selection"""
        choices = [
            "✏️  Enter Partner Name",
            "🎨 Choose Theme Color",
            "💌 Enter Romantic Message",
            "🌐 Generate Website",
            "🚀 Start Local Server",
            "🔗 Expose with ngrok",
            "📱 Generate QR Code",
            "🔄 Regenerate Website",
            "❌ Exit"
        ]
        
        answer = questionary.select(
            "What would you like to do?",
            choices=choices,
            pointer="❤️ "
        ).ask()
        
        if answer == "✏️  Enter Partner Name":
            self.input_partner_name()
        elif answer == "🎨 Choose Theme Color":
            self.choose_theme()
        elif answer == "💌 Enter Romantic Message":
            self.input_message()
        elif answer == "🌐 Generate Website":
            self.generate_website()
        elif answer == "🚀 Start Local Server":
            self.start_server()
        elif answer == "🔗 Expose with ngrok":
            self.expose_with_ngrok()
        elif answer == "📱 Generate QR Code":
            self.generate_qr_code()
        elif answer == "🔄 Regenerate Website":
            self.regenerate_website()
        elif answer == "❌ Exit":
            raise KeyboardInterrupt()
    
    def input_partner_name(self):
        """Get partner name from user"""
        name = questionary.text(
            "What is your partner's name?",
            validate=lambda x: len(x.strip()) > 0
        ).ask()
        
        if name:
            self.partner_name = name.strip()
            display_success_panel(
                "Success",
                f"Partner name set to: [bold cyan]{self.partner_name}[/bold cyan]"
            )
    
    def choose_theme(self):
        """Choose website theme"""
        theme_choices = []
        for key, theme_info in THEMES.items():
            theme_choices.append({
                'name': theme_info['name'],
                'value': key
            })
        
        answer = questionary.select(
            "Select a theme:",
            choices=theme_choices,
            pointer="❤️ "
        ).ask()
        
        if answer:
            self.theme = answer
            display_success_panel(
                "Theme Selected",
                f"Theme set to: [bold cyan]{THEMES[self.theme]['name']}[/bold cyan]"
            )
    
    def input_message(self):
        """Get romantic message from user"""
        message = questionary.text(
            "Enter your romantic message (max 500 characters):",
            validate=lambda x: 0 < len(x.strip()) <= 500
        ).ask()
        
        if message:
            self.message = message.strip()
            display_success_panel(
                "Message Saved",
                f"Message: [italic yellow]{self.message}[/italic yellow]"
            )
            
            # Ask about music
            include_music = questionary.confirm(
                "Include background music autoplay?",
                default=False
            ).ask()
            
            self.include_music = include_music
    
    def generate_website(self):
        """Generate website files"""
        if not self.partner_name:
            display_error_panel("Error", "Please enter partner name first")
            return
        
        if not self.message:
            display_error_panel("Error", "Please enter romantic message first")
            return
        
        try:
            animate_generating()
            
            # Generate website
            self.website_generator = WebsiteGenerator(
                partner_name=self.partner_name,
                message=self.message,
                theme=self.theme,
                include_music=self.include_music
            )
            
            files = self.website_generator.generate_all()
            
            # Display generated files
            display_success_panel(
                "Website Generated",
                f"""
✓ HTML file: {files['html'].name}
✓ CSS file: {files['css'].name}
✓ JavaScript file: {files['js'].name}

Location: [cyan]{OUTPUT_DIR}[/cyan]
                """
            )
        
        except Exception as e:
            display_error_panel("Generation Error", str(e))
    
    def start_server(self):
        """Start PHP server"""
        if not self.website_generator:
            display_error_panel("Error", "Please generate website first")
            return
        
        try:
            # Check PHP installation
            if not self.server.check_php_installed():
                display_error_panel(
                    "PHP Not Found",
                    """PHP is not installed on your system.
Download from: https://www.php.net/downloads.php
                    """
                )
                return
            
            animate_server_starting()
            
            # Start server
            local_url = self.server.start_php_server()
            
            display_success_panel(
                "Server Started",
                f"""✓ PHP server is running at:
[bold yellow]{local_url}[/bold yellow]

Open this URL in your browser to see the website.
The server will continue running in the background.
                """
            )
            
            time.sleep(2)
        
        except Exception as e:
            display_error_panel("Server Error", str(e))
    
    def expose_with_ngrok(self):
        """Expose server with ngrok"""
        if not self.server.php_process:
            display_error_panel("Error", "Please start the local server first")
            return
        
        try:
            # Check ngrok installation
            if not self.server.check_ngrok_installed():
                display_error_panel(
                    "ngrok Not Found",
                    """ngrok is not installed on your system.
Download from: https://ngrok.com/download

After installation, authenticate with:
    ngrok config add-authtoken YOUR_TOKEN
                    """
                )
                return
            
            animate_ngrok_connecting()
            
            # Start ngrok tunnel
            public_url = self.server.start_ngrok_tunnel()
            
            if public_url:
                self.public_url = public_url
                print_url(public_url)
                
                display_success_panel(
                    "Connected to ngrok",
                    f"""✓ Your website is now publicly accessible!
                    
URL: [bold yellow]{public_url}[/bold yellow]

This link will work for 2 hours (free ngrok)
or longer with a paid account.
Share this link with your loved one!
                    """
                )
                
                time.sleep(2)
            else:
                display_error_panel("ngrok Error", "Failed to get public URL from ngrok")
        
        except Exception as e:
            display_error_panel("ngrok Error", str(e))
    
    def generate_qr_code(self):
        """Generate QR code for public URL"""
        if not self.public_url:
            display_error_panel("Error", "Please expose the server with ngrok first")
            return
        
        try:
            qr_path = self.website_generator.generate_qr_code(self.public_url)
            
            if qr_path:
                print_qr_code_info(qr_path)
                display_success_panel(
                    "QR Code Generated",
                    f"""✓ QR code has been generated and saved to:
[cyan]{qr_path}[/cyan]

Share the QR code with your loved one!
                    """
                )
            else:
                display_error_panel("Error", "Failed to generate QR code")
        
        except Exception as e:
            display_error_panel("QR Code Error", str(e))
    
    def regenerate_website(self):
        """Regenerate website with new inputs"""
        console.print("\n[cyan]Regenerating Website...[/cyan]")
        
        # Ask for changes
        change_name = questionary.confirm(
            "Change partner name?",
            default=False
        ).ask()
        
        if change_name:
            self.input_partner_name()
        
        change_theme = questionary.confirm(
            "Change theme?",
            default=False
        ).ask()
        
        if change_theme:
            self.choose_theme()
        
        change_message = questionary.confirm(
            "Change message?",
            default=False
        ).ask()
        
        if change_message:
            self.input_message()
        
        # Regenerate
        self.generate_website()
        
        # Restart server if running
        if self.server.php_process:
            display_info_panel(
                "Server Restart",
                "Restart your browser or press F5 to see the new website"
            )
    
    def cleanup(self):
        """Clean up resources"""
        try:
            self.server.cleanup()
        except:
            pass


def main():
    """Entry point"""
    app = ValentinesCLI()
    app.run()


if __name__ == "__main__":
    main()
