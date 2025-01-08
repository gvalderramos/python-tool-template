#!/usr/bin/env python
import pathlib

def _insert_lines_on_file(path: pathlib.Path, lines: list[str], index: int) -> None:
    with open(path, "r") as file:
        file_lines = file.readlines()
        for file_line in lines:
            file_lines.insert(index, file_line)

    with open(path, "w") as path:
        path.writelines(file_lines)

if __name__ == '__main__':
    if 'n' == '{{ cookiecutter.command_line_interface|lower }}':
        pathlib.Path('src', '{{ cookiecutter.project_slug }}', 'cli.py').unlink()
    
    app_file = pathlib.Path('src', '{{ cookiecutter.project_slug }}', 'app.py')
    main_file = pathlib.Path('src', '{{ cookiecutter.project_slug }}', 'resource', 'ui', 'mainwindow.py')
    if 'n' == '{{ cookiecutter.qt_application|lower }}':
        pathlib.Path('resource').unlink()
        pathlib.Path('src', '{{ cookiecutter.project_slug }}', 'resource').unlink()
        app_file.unlink()
    else:
        qt_app_imports = {
            "PySide": [
                "from PySide.QtGui import QApplication\n",
                "from PySide.QtCore import QFile, QIODevice\n"
            ],
            "PySide2": [
                "from PySide2.QtWidgets import QApplication\n",
                "from PySide2.QtCore import QFile, QIODevice\n"
            ],
            "PySide6": [
                "from PySide6.QtWidgets import QApplication\n",
                "from PySide6.QtCore import QFile, QIODevice\n"
            ],
            "PyQt4": [
                "from PyQt4.QtGui import QApplication\n",
                "from PyQt4.QtCore import QFile, QIODevice\n"
            ],
            "PyQt5": [
                "from PyQt5.QtWidgets import QApplication\n",
                "from PyQt5.QtCore import QFile, QIODevice\n"
            ],
            "qtpy": [
                "from qtpy.QtWidgets import QApplication\n",
                "from qtpy.QtCore import QFile, QIODevice\n"
            ],
            "Qt.py": [
                "from Qt.QtWidgets import QApplication\n",
                "from Qt.QtCore import QFile, QIODevice\n"
            ]
        }
        qt_main_imports = {
            "PySide": [
                "from PySide.QtGui import QMainWindow\n",
            ],
            "PySide2": [
                "from PySide2.QtWidgets import QMainWindow\n",
            ],
            "PySide6": [
                "from PySide6.QtWidgets import QMainWindow\n",
            ],
            "PyQt4": [
                "from PyQt4.QtGui import QMainWindow\n",
            ],
            "PyQt5": [
                "from PyQt5.QtWidgets import QMainWindow\n",
            ],
            "qtpy": [
                "from qtpy.QtWidgets import QMainWindow\n",
            ],
            "Qt.py": [
                "from Qt.QtWidgets import QMainWindow\n",
            ]
        }
        if '{{ cookiecutter.qt_wrapper }}' != "None":
            qt_app_imports = qt_app_imports['{{ cookiecutter.qt_wrapper }}']
            qt_main_imports = qt_main_imports['{{ cookiecutter.qt_wrapper }}']
        else:
            qt_app_imports = qt_app_imports['{{ cookiecutter.qt_api }}']
            qt_main_imports = qt_main_imports['{{ cookiecutter.qt_api }}']
        
        _insert_lines_on_file(app_file, qt_app_imports, 2)
        _insert_lines_on_file(main_file, qt_main_imports, 0)
