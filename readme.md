# YNAB client

This project consumes the YNAB API to get my own personal transaction data. The plan is to store it somewhere and do interesting stuff with it.

## Setup

### Use the correct version of Python
I use `pyenv` to manage python versions. If you have `pyenv`, it should detect the `.python-version` file and use the same version of Python as me. If this does not happen automatically, you can do

```bash
# This detects the python version and switches for you
pyenv local
```

### Create your virtual environmenmt
Use a virtual environment for your dependencies.

```bash
# From in this directory
python -m venv . # Create the virtual environment
source bin/activate # Switch to the virtual env you just created
```

### Install dependencies

```bash
pip install -r requirements.txt
```



