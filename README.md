# nebulous-sar
Math model for Synthetic aperture radar to study such techniques like:
- RDA image synthesys
- MIMO SAR

## Prerequisits
Before running, and especially commiting to the repo, do the following things

### Python virtual environment
For the very first time it is mandatory to create virtual environment and install requrenments:
```bash
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
If you run it on the Windows, fix the following steps using the instructions from https://docs.python.org/3/library/venv.html

...or on a Linux machine just run the sript:
```bash
./create_venv.sh
```
than it is necessary only to activate it:
```bash
source .env/bin/activate
```
Deactivate:
```bash
deactivate
```

### Install the git hooks
To keep code formatted and non-ASCII free, please install git hooks
```bash
git config core.hooksPath hooks
```

## Running the model
```bash
python3 run_simulation.py
```
