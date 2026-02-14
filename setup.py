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

# Setup and installation configuration

from setuptools import setup, find_packages
from pathlib import Path

project_dir = Path(__file__).parent
readme_file = project_dir / "README.md"
requirements_file = project_dir / "requirements.txt"

# Read README
long_description = ""
if readme_file.exists():
    long_description = readme_file.read_text(encoding="utf-8")

# Read requirements
install_requires = []
if requirements_file.exists():
    install_requires = requirements_file.read_text(encoding="utf-8").strip().split("\n")

setup(
    name="valentine-surprise-generator",
    version="1.0.0",
    author="Valentine's Day Team",
    description="A production-ready CLI tool for generating romantic animated websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/valentine-surprise-generator",
    py_modules=[
        "cli",
        "config",
        "animations",
        "website_generator",
        "server_manager"
    ],
    install_requires=install_requires,
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "valentine=cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Communications",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
