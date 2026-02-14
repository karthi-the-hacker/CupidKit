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

# Server management - PHP server and ngrok integration

import subprocess
import socket
import time
import psutil
import platform
from pathlib import Path
from config import OUTPUT_DIR, DEFAULT_PORT, MAX_PORT_ATTEMPTS
import requests


class ServerManager:
    """Manage PHP server and ngrok tunnel"""
    
    def __init__(self):
        self.php_process = None
        self.ngrok_process = None
        self.port = DEFAULT_PORT
        self.os_type = platform.system()
    
    def find_available_port(self, start_port=DEFAULT_PORT):
        """Find an available port"""
        for offset in range(MAX_PORT_ATTEMPTS):
            port = start_port + offset
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.bind(('127.0.0.1', port))
                sock.close()
                self.port = port
                return port
            except OSError:
                continue
        raise RuntimeError(f"Could not find available port after {MAX_PORT_ATTEMPTS} attempts")
    
    def check_php_installed(self):
        """Check if PHP is installed"""
        try:
            result = subprocess.run(
                ['php', '--version'],
                capture_output=True,
                timeout=5
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False
    
    def check_ngrok_installed(self):
        """Check if ngrok is installed"""
        try:
            result = subprocess.run(
                ['ngrok', '--version'],
                capture_output=True,
                timeout=5
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False
    
    def start_php_server(self, port=None):
        """Start PHP server on the output directory"""
        if not self.check_php_installed():
            raise RuntimeError(
                "PHP is not installed. Please install PHP from https://www.php.net/downloads.php"
            )
        
        if port is None:
            port = self.find_available_port()
        
        self.port = port
        
        try:
            if self.os_type == "Windows":
                cmd = ['php', '-S', f'localhost:{port}', '-t', str(OUTPUT_DIR)]
                self.php_process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    creationflags=subprocess.CREATE_NEW_CONSOLE if self.os_type == "Windows" else 0
                )
            else:
                cmd = ['php', '-S', f'localhost:{port}', '-t', str(OUTPUT_DIR)]
                self.php_process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
            
            # Give the server time to start
            time.sleep(1)
            
            # Verify server is running
            if self.verify_server(port):
                return f"http://localhost:{port}"
            else:
                raise RuntimeError("Failed to verify PHP server is running")
        
        except Exception as e:
            raise RuntimeError(f"Failed to start PHP server: {str(e)}")
    
    def verify_server(self, port, attempts=5):
        """Verify that the server is running"""
        for _ in range(attempts):
            try:
                response = requests.get(f"http://localhost:{port}/", timeout=2)
                return response.status_code == 200
            except requests.exceptions.RequestException:
                time.sleep(0.5)
        return False
    
    def start_ngrok_tunnel(self):
        """Start ngrok tunnel to expose local server"""
        if not self.check_ngrok_installed():
            raise RuntimeError(
                "ngrok is not installed. Download from https://ngrok.com/download"
            )
        
        try:
            # Kill any existing ngrok processes
            self.kill_ngrok()
            time.sleep(0.5)
            
            cmd = ['ngrok', 'http', str(self.port), '--log=stdout']
            
            self.ngrok_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            
            # Give ngrok time to start and establish tunnel
            time.sleep(3)
            
            # Get the public URL from ngrok
            public_url = self.get_ngrok_public_url()
            if public_url:
                return public_url
            else:
                raise RuntimeError("Failed to get public URL from ngrok")
        
        except Exception as e:
            raise RuntimeError(f"Failed to start ngrok tunnel: {str(e)}")
    
    def get_ngrok_public_url(self):
        """Get the public URL from ngrok API"""
        try:
            # ngrok provides a local API on port 4040
            response = requests.get('http://127.0.0.1:4040/api/tunnels', timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                tunnels = data.get('tunnels', [])
                
                if tunnels:
                    # Find the HTTP tunnel
                    for tunnel in tunnels:
                        if tunnel.get('proto') == 'http':
                            return tunnel.get('public_url')
                
                return None
            else:
                return None
        
        except Exception as e:
            print(f"Error getting ngrok URL: {e}")
            return None
    
    def kill_php_server(self):
        """Kill the PHP server process"""
        if self.php_process:
            try:
                if self.os_type == "Windows":
                    self.php_process.terminate()
                else:
                    self.php_process.terminate()
                    self.php_process.wait(timeout=5)
            except:
                pass
            finally:
                self.php_process = None
    
    def kill_ngrok(self):
        """Kill the ngrok process"""
        if self.ngrok_process:
            try:
                self.ngrok_process.terminate()
                self.ngrok_process.wait(timeout=5)
            except:
                pass
            finally:
                self.ngrok_process = None
        
        # Also kill any other ngrok processes
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                if 'ngrok' in proc.info['name'].lower():
                    psutil.Process(proc.info['pid']).terminate()
        except:
            pass
    
    def cleanup(self):
        """Clean up all processes"""
        self.kill_php_server()
        self.kill_ngrok()
    
    def __del__(self):
        """Cleanup on object destruction"""
        self.cleanup()
