@echo off
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting Flask development server...
python run.py

pause