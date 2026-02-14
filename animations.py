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

# CLI animations and UI utilities

import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich import box
import sys

console = Console()

def display_welcome_screen():
    """Display an animated welcome screen"""
    console.clear()
    
    # Animated hearts
    heart_animation = [
        "    ❤️  ❤️  ❤️  ❤️  ❤️",
        "   ❤️ 💕 💕 💕 ❤️",
        "  ❤️ 💕 💖 💕 ❤️",
        "   ❤️ 💕 💕 💕 ❤️",
        "    ❤️  ❤️  ❤️  ❤️  ❤️",
    ]
    
    for frame in heart_animation:
        console.clear()
        console.print(Align.center("[bold magenta]" + frame + "[/bold magenta]"))
        time.sleep(0.1)
    
    console.clear()
    
    # Welcome panel
    welcome_text = Text()
    welcome_text.append("💕 ", style="bold red")
    welcome_text.append("Valentine's Day", style="bold cyan")
    welcome_text.append(" Surprise Generator ", style="bold magenta")
    welcome_text.append("💕", style="bold red")
    
    console.print(Align.center(welcome_text))
    console.print()
    
    # Animated description with character by character effect
    description = "✨ Create a beautiful romantic website and share it with your loved one ✨"
    console.print(Align.center("[yellow]" + description + "[/yellow]"))
    console.print()
    time.sleep(0.5)

def display_menu(options):
    """Display an interactive menu"""
    console.print()
    table = Table(title="[bold magenta]Main Menu[/bold magenta]", box=box.ROUNDED)
    table.add_column("Option", style="cyan", width=2)
    table.add_column("Description", style="yellow")
    
    for i, option in enumerate(options, 1):
        table.add_row(str(i), option)
    
    console.print(Align.center(table))

def animate_generating():
    """Show animated generating message"""
    spinner_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    message = "Generating your romantic website"
    
    for i in range(20):
        frame = spinner_frames[i % len(spinner_frames)]
        sys.stdout.write(f"\r{frame} {message}... ")
        sys.stdout.flush()
        time.sleep(0.05)
    
    console.print()
    console.print("[bold green]✓ Website generated successfully![/bold green]")

def animate_server_starting():
    """Show animated server starting message"""
    spinner_frames = ["◐", "◓", "◑", "◒"]
    message = "Starting PHP server"
    
    for i in range(15):
        frame = spinner_frames[i % len(spinner_frames)]
        sys.stdout.write(f"\r{frame} {message}... ")
        sys.stdout.flush()
        time.sleep(0.08)
    
    console.print()
    console.print("[bold green]✓ PHP server started![/bold green]")

def animate_ngrok_connecting():
    """Show animated ngrok connecting message"""
    spinner_frames = ["🌍", "🌎", "🌏"]
    message = "Connecting to ngrok"
    
    for i in range(15):
        frame = spinner_frames[i % len(spinner_frames)]
        sys.stdout.write(f"\r{frame} {message}... ")
        sys.stdout.flush()
        time.sleep(0.1)
    
    console.print()
    console.print("[bold green]✓ Connected to ngrok![/bold green]")

def display_success_panel(title, content):
    """Display a success panel"""
    panel = Panel(
        content,
        title=f"[bold green]{title}[/bold green]",
        border_style="green",
        expand=False
    )
    console.print(Align.center(panel))

def display_error_panel(title, content):
    """Display an error panel"""
    panel = Panel(
        content,
        title=f"[bold red]{title}[/bold red]",
        border_style="red",
        expand=False
    )
    console.print(Align.center(panel))

def display_info_panel(title, content):
    """Display an info panel"""
    panel = Panel(
        content,
        title=f"[bold cyan]{title}[/bold cyan]",
        border_style="cyan",
        expand=False
    )
    console.print(Align.center(panel))

def print_url(public_url):
    """Print the public URL in a highlighted format"""
    console.print()
    url_text = Text()
    url_text.append("🔗 Your public URL: ", style="bold cyan")
    url_text.append(public_url, style="bold yellow")
    console.print(Align.center(url_text))
    console.print()

def print_qr_code_info(qr_code_path):
    """Print QR code information"""
    qr_text = Text()
    qr_text.append("📱 QR Code saved to: ", style="bold magenta")
    qr_text.append(str(qr_code_path), style="bold cyan")
    console.print(Align.center(qr_text))
    console.print()
