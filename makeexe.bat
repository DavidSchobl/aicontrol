@echo off
call venv\Scripts\activate
pyinstaller --onefile --windowed --icon ailogo.ico AI-Control.py
echo Kompilace dokoncena.
pause
