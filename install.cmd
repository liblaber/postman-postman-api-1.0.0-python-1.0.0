@echo off
set USE_VENV=0

:loop
if "%~1"=="" goto afterloop
if "%~1"=="--use-venv" set USE_VENV=1
shift
goto loop
:afterloop

if "%USE_VENV%"=="1" (
    python -m venv .venv
    call .venv\Scripts\activate
)

pip install build
python -m build --outdir dist .
<<<<<<< HEAD
pip install dist\postman_sdk-1.0.0-py3-none-any.whl --force-reinstall
=======
pip install dist\postman-1.0.0-py3-none-any.whl --force-reinstall
>>>>>>> 95da91c (initial commit)

if "%USE_VENV%"=="1" (
    deactivate
)
