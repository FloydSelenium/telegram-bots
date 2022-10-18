@echo
setlocal enableextensions enabledelayedexpansion
cd A:\BigDeal\Release\AccsNew
Set /A files=0
For %%I In (*) Do Set /A files += 1

Set Drive=A:\BigDeal\Release\Bots
For /F "Tokens=1 Delims=:" %%A In ('Dir %Drive% /B /S /AD^|FindStr /IN .') Do Set /A folders=%%A

Set /A k=files+folders-1


FOR /L %%i IN (%folders%, 1, %k%) DO  (
cd A:\BigDeal\Release\Bots\bot%%i
start powershell python botprod.py
SLEEP 130
)

FOR /L %%i IN (%folders%, 1, %k%) DO  (
cd A:\BigDeal\Release\Bots\bot%%i
start powershell python botprod.py
SLEEP 10
:do
SLEEP 10
if exist "A:/BigDeal/Release/marker.txt" {goto next} else {goto do}
:next
echo RUN
)
pause
