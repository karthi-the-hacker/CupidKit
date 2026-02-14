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

# Installation validator and testing script

import sys
import subprocess
from pathlib import Path

def check_dependencies():
    """Check if all required packages are installed"""
    print("=" * 50)
    print("Checking Python Dependencies...")
    print("=" * 50)
    
    required_packages = {
        'rich': 'rich',
        'questionary': 'questionary',
        'psutil': 'psutil',
        'requests': 'requests',
        'qrcode': 'qrcode',
        'PIL': 'Pillow',
        'pyngrok': 'pyngrok'
    }
    
    missing = []
    
    for import_name, package_name in required_packages.items():
        try:
            __import__(import_name)
            print(f"✓ {package_name} installed")
        except ImportError:
            print(f"✗ {package_name} NOT installed")
            missing.append(package_name)
    
    if missing:
        print("\n" + "=" * 50)
        print("MISSING PACKAGES")
        print("=" * 50)
        print("Install with: pip install " + " ".join(missing))
        return False
    
    return True

def check_system_tools():
    """Check if PHP and ngrok are installed"""
    print("\n" + "=" * 50)
    print("Checking System Tools...")
    print("=" * 50)
    
    tools_ok = True
    
    # Check PHP
    try:
        result = subprocess.run(['php', '--version'], capture_output=True, timeout=5)
        if result.returncode == 0:
            version = result.stdout.decode().split('\n')[0]
            print(f"✓ PHP installed: {version}")
        else:
            print("✗ PHP NOT installed")
            tools_ok = False
    except FileNotFoundError:
        print("✗ PHP NOT installed")
        tools_ok = False
    except subprocess.TimeoutExpired:
        print("✗ PHP check timed out")
        tools_ok = False
    
    # Check ngrok
    try:
        result = subprocess.run(['ngrok', '--version'], capture_output=True, timeout=5)
        if result.returncode == 0:
            version = result.stdout.decode().strip()
            print(f"✓ ngrok installed: {version}")
        else:
            print("✗ ngrok NOT installed")
            tools_ok = False
    except FileNotFoundError:
        print("✗ ngrok NOT installed")
        tools_ok = False
    except subprocess.TimeoutExpired:
        print("✗ ngrok check timed out")
        tools_ok = False
    
    if not tools_ok:
        print("\n" + "=" * 50)
        print("INSTALLATION INSTRUCTIONS")
        print("=" * 50)
        print("PHP: https://www.php.net/downloads.php")
        print("ngrok: https://ngrok.com/download")
    
    return tools_ok

def check_project_files():
    """Check if all required project files exist"""
    print("\n" + "=" * 50)
    print("Checking Project Files...")
    print("=" * 50)
    
    base_dir = Path(__file__).parent
    required_files = [
        'cli.py',
        'config.py',
        'animations.py',
        'website_generator.py',
        'server_manager.py',
        'setup.py',
        'requirements.txt',
        'README.md',
        'QUICKSTART.md',
        '.gitignore'
    ]
    
    all_exist = True
    
    for filename in required_files:
        filepath = base_dir / filename
        if filepath.exists():
            print(f"✓ {filename}")
        else:
            print(f"✗ {filename} NOT FOUND")
            all_exist = False
    
    # Check directories
    dirs_needed = ['output']
    for dirname in dirs_needed:
        dirpath = base_dir / dirname
        if dirpath.exists():
            print(f"✓ {dirname}/ directory")
        else:
            print(f"✗ {dirname}/ directory NOT FOUND")
            all_exist = False
    
    return all_exist

def test_imports():
    """Test if all modules can be imported"""
    print("\n" + "=" * 50)
    print("Testing Imports...")
    print("=" * 50)
    
    try:
        import config
        print("✓ config module")
    except Exception as e:
        print(f"✗ config module: {e}")
        return False
    
    try:
        import animations
        print("✓ animations module")
    except Exception as e:
        print(f"✗ animations module: {e}")
        return False
    
    try:
        import website_generator
        print("✓ website_generator module")
    except Exception as e:
        print(f"✗ website_generator module: {e}")
        return False
    
    try:
        import server_manager
        print("✓ server_manager module")
    except Exception as e:
        print(f"✗ server_manager module: {e}")
        return False
    
    try:
        import CupidKit
        print("✓ cli module")
    except Exception as e:
        print(f"✗ cli module: {e}")
        return False
    
    return True

def main():
    """Run all validation checks"""
    print("\n")
    print("╔════════════════════════════════════════════════════╗")
    print("║   Valentine's Day Surprise Generator - Validator  ║")
    print("╚════════════════════════════════════════════════════╝")
    print("\n")
    
    checks = [
        ("Python Dependencies", check_dependencies),
        ("Project Files", check_project_files),
        ("Module Imports", test_imports),
        ("System Tools", check_system_tools),
    ]
    
    results = []
    
    for check_name, check_func in checks:
        try:
            result = check_func()
            results.append((check_name, result))
        except Exception as e:
            print(f"\n✗ Error in {check_name}: {e}")
            results.append((check_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("VALIDATION SUMMARY")
    print("=" * 50)
    
    all_ok = True
    for check_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {check_name}")
        if not result:
            all_ok = False
    
    print("\n" + "=" * 50)
    
    if all_ok:
        print("✓ All checks passed! Ready to run!")
        print("\nStart the tool with: python cli.py")
        return 0
    else:
        print("✗ Some checks failed. Please fix the issues above.")
        print("\nFor help, see QUICKSTART.md or README.md")
        return 1

if __name__ == "__main__":
    sys.exit(main())
