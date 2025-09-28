@echo off
chcp 65001 >nul 2>&1
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8

REM 啟動監控程式 (背景執行，不會卡住主程式)
start "" python "%~dp0json_watcher.py"

REM 啟動 FaceFusion
call conda activate facefusion
python facefusion.py run --open-browser

pause
