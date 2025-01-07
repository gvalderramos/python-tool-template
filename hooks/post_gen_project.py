#!/usr/bin/env python
import pathlib


if __name__ == '__main__':
    if 'n' == '{{ cookiecutter.command_line_interface|lower }}':
        pathlib.Path('src', '{{ cookiecutter.project_slug }}', 'cli.py').unlink()
