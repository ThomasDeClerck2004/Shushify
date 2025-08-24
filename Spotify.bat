@echo off
start "" "%APPDATA%\Spotify\Spotify.exe"
start "" "%~dp0.venv\Scripts\pythonw.exe" "%~dp0main.py"