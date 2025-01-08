{{ cookiecutter.project_name }}
-------------------------------

{{ cookiecutter.project_short_description }}

# Makefile Commands

This project includes a Makefile to simplify common tasks during development, testing, and deployment. Below is a detailed description of each available make command.

## Commands

### General Commands

- **help**  
  Displays a list of all available commands with their descriptions.

- **clean**  
  Cleans up all build, test, coverage, and Python artifacts. This command is a combination of the following:
  - `clean-build`
  - `clean-pyc`
  - `clean-test`

### Cleaning Commands

- **clean-build**  
  Removes all build artifacts, including directories and files related to distribution:
  - `build/`
  - `dist/`
  - `.eggs/`
  - `*.egg-info`
  - `*.egg`

- **clean-pyc**  
  Removes Python file artifacts, including:
  - `*.pyc`, `*.pyo`
  - Temporary files (`*~`)
  - Python cache directories (`__pycache__/`)

- **clean-test**  
  Removes test and coverage artifacts:
  - `.coverage`
  - `htmlcov/`
  - `.pytest_cache`

### Code Quality Commands

- **lint/flake8**  
  Checks the code style using `flake8`. This checks the `src/python_cli_test` and `tests` directories for style issues.

- **format/black**  
  Formats Python source files in the `src/python_cli_test` and `tests` directories using `black`.

- **lint**  
  Alias for `lint/flake8`. Checks the code style using `flake8`.

- **format**  
  Alias for `format/black`. Formats the Python source and test folders.

### Testing and Coverage Commands

- **test**  
  Runs the test suite using `pytest`.

- **coverage**  
  Checks code coverage using `coverage.py`. This generates a coverage report in the terminal and as an HTML file in the `htmlcov/` directory. The HTML report is opened in the default web browser.

### Documentation Commands

- **docs**  
  Generates Sphinx HTML documentation, including API docs. The generated documentation is opened in the default web browser. This command:
  - Cleans the `docs/` directory.
  - Runs `sphinx-apidoc` to generate API documentation.
  - Builds the HTML documentation.

- **servedocs**  
  Compiles the Sphinx documentation and watches for changes in `.rst` files. Automatically rebuilds the documentation when changes are detected.

### Installation Commands

- **install**  
  Cleans the environment and installs the package to the active Python's `site-packages`.

{%- if cookiecutter.qt_application == "y" -%}
- **qt**
  Compile all QT files and resources

- **run**
  Execute the Qt Application
{%- endif %}

### Other Notes

- **Default Goal**  
  Running `make` without any arguments will display the `help` command by default.
