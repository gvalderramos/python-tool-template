import os
import webbrowser
import sys
import typer
import pathlib
import shutil
import subprocess

from urllib.request import pathname2url
from contextlib import contextmanager

app = typer.Typer()
RCC_EXEC = {
    "None": "",
    "PySide": "pyside-rcc",
    "PySide2": "pyside2-rcc",
    "PySide6": "pyside6-rcc",
    "PyQt4": "pyrcc4",
    "PyQt5": "pyrcc5"
}
UIC_EXEC = {
    "None": "",
    "PySide": "pyside-uic",
    "PySide2": "pyside2-uic",
    "PySide6": "pyside6-uic",
    "PyQt4": "pyuic4",
    "PyQt5": "pyuic5"
}
QT_WRAPPER = {
    "None": "",
    "qtpy": "qtpy",
    "Qt.py": "Qt"
}


def _delete_path(path: pathlib.Path):
    if path.exists():
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()


def _open_browser(path: str):
    webbrowser.open(f"file://{pathname2url(os.path.abspath(path))}")


@contextmanager
def _set_directory(path: pathlib.Path):
    origin = pathlib.Path().absolute()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(origin)


@app.command(help="remove build artifacts")
def clean_build():
    _delete_path(pathlib.Path("build"))
    _delete_path(pathlib.Path("dist"))
    _delete_path(pathlib.Path(".eggs"))
    for p in pathlib.Path("src").rglob("*.egg-info"):
        _delete_path(p)
    for p in pathlib.Path("src").rglob("*.egg"):
        _delete_path(p)


@app.command(help="remove Python file artifacts")
def clean_pyc():
    for p in pathlib.Path("src").rglob("*.pyc"):
        _delete_path(p)

    for p in pathlib.Path("src").rglob("*.pyo"):
        _delete_path(p)

    for p in pathlib.Path("src").rglob("*~"):
        _delete_path(p)

    for p in pathlib.Path("src").rglob("__pycache__"):
        _delete_path(p)


@app.command(help="remove test and coverage artifacts")
def clean_test():
    _delete_path(pathlib.Path(".coverage"))
    _delete_path(pathlib.Path("htmlcov"))
    _delete_path(pathlib.Path(".pytest_cache"))


@app.command(help="remove all build, test, coverage and Python artifacts")
def clean():
    clean_build()
    clean_pyc()
    clean_test()


@app.command(help="check style")
def lint():
    subprocess.run("flake8 src/{{cookiecutter.project_slug}} tests", shell=True)


@app.command(help="format the python source and test folder")
def format():
    subprocess.run("black src/{{cookiecutter.project_slug}} tests", shell=True)


@app.command(help="run tests with pytest")
def test():
    subprocess.run("pytest", shell=True)


@app.command(help="check code coverage quickly with the default Python")
def coverage():
    subprocess.run("coverage run --source {{cookiecutter.project_slug}} -m pytest", shell=True)
    subprocess.run("coverage report -m", shell=True)
    subprocess.run("coverage html", shell=True)
    _open_browser("htmlcov/index.html")


@app.command(help="generate Sphinx HTML documentation, including API docs")
def docs():
    _delete_path(pathlib.Path("docs", "{{cookiecutter.project_slug}}.rst"))
    _delete_path(pathlib.Path("docs", "modules.rst"))
    subprocess.run("sphinx-apidoc -o docs/ {{cookiecutter.project_slug}}")
    make_cmd = "make.bat" if sys.platform() in ["win32", "cygwin"] else "make"
    with _set_directory(pathlib.Path("docs")):
        subprocess.run(f"{make_cmd} clean")
        subprocess.run(f"{make_cmd} html")
    _open_browser("docs/_build/html/index.html")


{%- if cookiecutter.qt_application == "y" %}
@app.command(help="Make the qt resource files")
def qt_rcc():
    rcc_exec = RCC_EXEC["{{cookiecutter.qt_api}}"]
    qt_wrapper = QT_WRAPPER["{{cookiecutter.qt_wrapper}}"]
    replacements = {
        "from {{cookiecutter.qt_api}}": f"from {qt_wrapper}"
    }
    rcc_file = pathlib.Path("resource.qrc")
    output = pathlib.Path("src", "{{cookiecutter.project_slug}}", "resource", "resource.py")
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

@app.command(help="Convert ui to python files")
def qt_ui():
    uic_exec = UIC_EXEC["{{cookiecutter.qt_api}}"]
    qt_wrapper = QT_WRAPPER["{{cookiecutter.qt_wrapper}}"]
    replacements = {
        "from {{cookiecutter.qt_api}}": f"from {qt_wrapper}"
    }
    for ui in pathlib.Path("resource", "ui").glob("*.ui"):
        output = pathlib.Path("src", "{{cookiecutter.project_slug}}", "resource", "ui", ui.name.replace(".ui", "_ui.py"))
        subprocess.run(f"{uic_exec} {ui.absolute().as_posix()} -o {output.as_posix()}", shell=True, check=True)

        content = []
        for line in output.read_text().split("\n"):
            for src, target in replacements.items():
                line = line.replace(src, target)
            content.append(line)
        output.write_text("\n".join(content))


@app.command(help="Compile all files and resources")
def qt():
    qt_rcc()
    qt_ui()

@app.command(help="Run qt application")
def run():
    install()
    subprocess.run("{{cookiecutter.project_slug}}")
{%- endif %}


@app.command(help="install the package to the active Python's site-packages")
def install():
    clean()
    {%- if cookiecutter.qt_application == "y" %}
    qt()
    {%- endif %}
    subprocess.run("pip install .")

if __name__ == "__main__":
    app()
