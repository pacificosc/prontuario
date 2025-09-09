# PyQt6 Starter

Quick start for a PyQt6 desktop application.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
source .venv/bin/activate
python main.py
# or
make run
```

## Lint & format

```bash
# lint only
ruff check .

# auto-fix + format
ruff check --fix .
black .
# or
make fix
```

## Build single executable

```bash
source .venv/bin/activate
pyinstaller --name PyQt6Starter --noconsole --onefile main.py
# or
make build
```