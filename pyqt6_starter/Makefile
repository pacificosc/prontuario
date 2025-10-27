VENV=.venv
PY=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
RUFF=$(VENV)/bin/ruff
BLACK=$(VENV)/bin/black
PYINSTALLER=$(VENV)/bin/pyinstaller

.PHONY: venv install run lint format fix build clean

venv:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip setuptools wheel

install: venv
	$(PIP) install -r requirements.txt

run:
	$(PY) main.py

lint:
	$(RUFF) check .

format:
	$(BLACK) .

fix:
	$(RUFF) check --fix .
	$(BLACK) .

build:
	$(PYINSTALLER) --name PyQt6Starter --noconsole --onefile main.py

clean:
	rm -rf build dist *.spec

