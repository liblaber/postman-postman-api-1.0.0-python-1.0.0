python -m venv .venv
. .venv/bin/activate
pip install build
python -m build --outdir dist ../
<<<<<<< HEAD
pip install dist/postman_sdk-1.0.0-py3-none-any.whl --force-reinstall
=======
pip install dist/postman-1.0.0-py3-none-any.whl --force-reinstall
>>>>>>> 95da91c (initial commit)
