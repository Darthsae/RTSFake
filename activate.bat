@echo off

if exist ".\venv" (
    echo venv exists.
) else (
    echo venv does not exist, creating now.
    py -m venv venv
)

call venv/Scripts/activate.bat

pip install -r requirements.txt