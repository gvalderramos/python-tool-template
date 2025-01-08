.PHONY: clean clean-build clean-pyc clean-test coverage docs help install lint lint/flake8 run

.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

{%- if cookiecutter.qt_application == "y" %}
define MAKE_RCC_FILES_SCRIPT
import sys
import subprocess
from pathlib import Path

rcc_exec = {
	"None": "",
	"PySide": "pyside-rcc",
	"PySide2": "pyside2-rcc",
	"PySide6": "pyside6-rcc",
	"PyQt4": "pyrcc4",
	"PyQt5": "pyrcc5"
}["{{cookiecutter.qt_api}}"]
qt_wrapper = {
	"None": "",
	"qtpy": "qtpy",
	"Qt.py": "Qt"
}["{{cookiecutter.qt_wrapper}}"]
replacements = {
	"from {{cookiecutter.qt_api}}": f"from {qt_wrapper}"
}
rcc_file = Path("resource.qrc")
output = Path("src", "{{cookiecutter.project_slug}}", "resource", "resource.py")
if not rcc_file.exists():
	print(f"file {line} not found.")
	sys.exit(-1)

cmd = f"{rcc_exec} {rcc_file.name}"
res = subprocess.run([rcc_exec, rcc_file.name], capture_output=True, text=True)
if not res:
	print(f"Error executing command: {cmd}")
	exit(-1)

content = []
for line in res.stdout.split("\n"):
	for src, target in replacements.items():
		line = line.replace(src, target)
	content.append(line)
output.write_text("\n".join(content))
endef
export MAKE_RCC_FILES_SCRIPT

define MAKE_UI_FILES_SCRIPT
import os, sys
import subprocess
from pathlib import Path

uic_exec = {
	"None": "",
	"PySide": "pyside-uic",
	"PySide2": "pyside2-uic",
	"PySide6": "pyside6-uic",
	"PyQt4": "pyuic4",
	"PyQt5": "pyuic5"
}["{{cookiecutter.qt_api}}"]
qt_wrapper = {
	"None": "",
	"qtpy": "qtpy",
	"Qt.py": "Qt"
}["{{cookiecutter.qt_wrapper}}"]
replacements = {
	"from {{cookiecutter.qt_api}}": f"from {qt_wrapper}"
}
for ui in Path("resource", "ui").glob("*.ui"):
	output = Path("src", "{{cookiecutter.project_slug}}", "resource", "ui", ui.name.replace(".ui", "_ui.py"))
	subprocess.run(f"{uic_exec} {ui.absolute().as_posix()} -o {output.as_posix()}", shell=True, check=True)

	content = []
	for line in output.read_text().split("\n"):
		for src, target in replacements.items():
			line = line.replace(src, target)
		content.append(line)
	output.write_text("\n".join(content))
endef
export MAKE_UI_FILES_SCRIPT
UI_FILES := $(wildcard resource/ui/*.ui)
{%- endif %}

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find ./src -name '*.egg-info' -exec rm -fr {} +
	find ./src -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find ./src -name '*.pyc' -exec rm -f {} +
	find ./src -name '*.pyo' -exec rm -f {} +
	find ./src -name '*~' -exec rm -f {} +
	find ./src -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint/flake8: ## check style with flake8
	flake8 src/{{ cookiecutter.project_slug }} tests

format/black: ## format the python source and test folder with black
	black src/{{ cookiecutter.project_slug }} tests

lint: lint/flake8 ## check style

format: format/black ## format the python source and test folder

test: ## run tests quickly with the default Python
	pytest

coverage: ## check code coverage quickly with the default Python
	coverage run --source {{ cookiecutter.project_slug }} -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/{{ cookiecutter.project_slug }}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{ cookiecutter.project_slug }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

install: clean qt ## install the package to the active Python's site-packages
	pip install .

{%- if cookiecutter.qt_application == "y" %}
Qt/rcc: ## Make the qt resouce files
	@python -c "$$MAKE_RCC_FILES_SCRIPT"

Qt/ui: ## Convert ui to python files
	@python -c "$$MAKE_UI_FILES_SCRIPT"

qt: Qt/rcc Qt/ui ## Compile all files and resources

run: install ## Run qt application
	{{cookiecutter.project_slug}}
{%- endif %}
