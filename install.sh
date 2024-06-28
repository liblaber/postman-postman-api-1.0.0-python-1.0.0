#!/bin/bash

USE_VENV=0

for arg in "$@"
do
    case $arg in
        --use-venv)
        USE_VENV=1
        shift
        ;;
    esac
done

if [ "$USE_VENV" -eq 1 ]; then
    python -m venv .venv
    . .venv/bin/activate
fi

<<<<<<< HEAD
pip install build
python -m build --outdir dist .
pip install dist/postman_sdk-1.0.0-py3-none-any.whl --force-reinstall

if [ "$USE_VENV" -eq 1 ]; then
    deactivate
fi
=======
pip3 install build
python3 -m build --outdir dist .
pip3 install dist/postman-1.0.0-py3-none-any.whl --force-reinstall

if [ "$USE_VENV" -eq 1 ]; then
    deactivate
fi
>>>>>>> 95da91c (initial commit)
