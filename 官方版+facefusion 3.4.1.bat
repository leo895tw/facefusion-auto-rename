@echo off
chcp 65001 >nul 2>&1
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8

REM �Ұʺʱ��{�� (�I������A���|�d��D�{��)
start "" python "%~dp0json_watcher.py"

REM �Ұ� FaceFusion
call conda activate facefusion
python facefusion.py run --open-browser

pause
