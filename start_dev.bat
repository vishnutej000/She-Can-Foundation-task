@echo off
echo Starting She Can Foundation Development Environment
echo ================================================

echo.
echo Starting Backend (Flask)...
start "Backend" cmd /k "cd backend && venv\Scripts\activate && python run.py"

timeout /t 3 /nobreak > nul

echo.
echo Starting Frontend (React + Vite)...
start "Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo Development servers are starting...
echo Backend: http://localhost:5000
echo Frontend: http://localhost:5173
echo.
echo Press any key to exit...
pause > nul