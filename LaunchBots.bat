@echo off
cd Bots
FOR /L %%i IN (1, 1, 53) DO  (
cd bot%%i
start powershell python Bot.py
SLEEP 1
cd ..
)
pause