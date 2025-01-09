import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'


def main():
    module_name = '{{ cookiecutter.project_slug}}'

    if not re.match(MODULE_REGEX, module_name):
        print('ERROR: The project slug (%s) is not a valid Python module name. '
            'Please do not use a - and use _ instead' % module_name)
        #Exit to cancel project
        sys.exit(1)

    is_cli = '{{cookiecutter.command_line_interface}}' == "y"
    qt_app  = '{{ cookiecutter.qt_application }}'
    qt_api  = '{{ cookiecutter.qt_api }}'
    qt_wrapper  = '{{ cookiecutter.qt_wrapper }}'
    if qt_app == "y":
        if qt_api == "None":
            print("Error: You should choose the Qt API if set this project  as Qt Application.")
            sys.exit(1)
        if is_cli:
            print("You should choose or CLI application or Qt Application. Not both")
            sys.exit(1)
    else:
        if (qt_api != "None" or qt_wrapper != "None") and qt_api == "None":
            print("Warning: You didn't set this project as Qt Application. Any Qt API or Qt Wrapper option will be ignored.")


if __name__ == "__main__":
    main()