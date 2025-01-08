# Python Tool Template
This guide describes how to create a Python tool using the [cookiecutter](https://pypi.org/project/cookiecutter/) Python tool template. Follow these steps to generate a boilerplate project for your pipeline application.<br />
This template can create generate 3 kinds of projects:
* Standalone python api / libraries
* Python QT applications
* Python CLI applications

This project was created based on the [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage). Feel free to look there for more info.

## Prerequisites

Before starting, ensure you have the following installed:
- Python 3.x
- `cookiecutter` (`pip install cookiecutter`)

## Steps to Generate the Project

1. **Run the Cookiecutter Command**  
   Start by running the `cookiecutter` command with the desired Python tool template:
   ```bash
   cookiecutter python-tool-template/
   ```

2. Respond to the Prompts
   
   Fill in the prompts as per your project requirements. Below is a breakdown of the fields and their descriptions:

   * full_name: Your full name.<br />
     Example: `Gabriel Valderramos`

   * email: Your email address.<br />
     Example: `gabrielvalderramos@gmail.com`

   * git_username: Your Git username.<br />
     Example: `gvalderramos`

   * project_name: The name of your project.<br />
     Example: `My Fantastic Tool Name`

   * project_slug:<br />
     The slug for your project directory. Press Enter to accept the default value, which is derived from project_name.<br />
     Example: `my_fantastic_tool_name`

   * project_short_description:<br />
     A brief description of your project. Press Enter to use the default description or provide your own.<br />
     Example: `A Python tool for...`

   * version: The initial version of your project.<br />
   Example: 0.2.8

   * command_line_interface: Whether the project includes a CLI.<br />
   Enter `y` for Yes or `n` for No.<br />
   Example: y

   * qt_application: Whether the project includes a Qt application.<br />
   Enter `n` for No or `y` for Yes.<br />
   Example: n

   * qt_api: Select the desired Qt API (if applicable).<br />
     Choose one of the following options:
     ```
      1. None
      2. PySide
      3. PySide2
      4. PySide6
      5. PyQt4
      6. PyQt5
     ```
   
   * qt_wrapper: Select the Qt wrapper (if applicable).<br />
   Choose one of the following options:
      ```
      1. None
      2. qtpy
      3. Qt.py
      ```
   
   * studio_name: <br />
     Enter the name of your studio or leave blank.<br />
     Example: My Studio Name

   * department_name: <br />
     Enter the department name (e.g., Pipeline, R&D).<br />
     Example: Pipeline / R&D

3. Project Generation<br />
   After completing the prompts, cookiecutter generates the project in a new directory based on the project_slug.

4. Navigate to the Project Directory<br />
   Change into the newly created directory:
   ```bash
   cd my_fantastic_tool
   ```

5. Start Developing
   Use the generated boilerplate to build your Python tool.

## Example Output
Here's an example of the input-output process during project generation:
```bash
$ cookiecutter python-tool-template
  [1/13] full_name (Gabriel Valderramos): 
  [2/13] email (gabrielvalderramos@gmail.com): 
  [3/13] git_username (gvalderramos): 
  [4/13] project_name (Python Boilerplate): My Fantastic Tool
  [5/13] project_slug (my_fantastic_tool): 
  [6/13] project_short_description (Python Boilerplate contains all the boilerplate you need to create a Python package.): A python tool for ...
  [7/13] version (0.1.0): 0.28.2
  [8/13] command_line_interface (n): y
  [9/13] qt_application (n): 
  [10/13] Select qt_api
    1 - None
    2 - PySide
    3 - PySide2
    4 - PySide6
    5 - PyQt4
    6 - PyQt5
    Choose from [1/2/3/4/5/6] (1): 1
  [11/13] Select qt_wrapper
    1 - None
    2 - qtpy
    3 - Qt.py
    Choose from [1/2/3] (1): 1
  [12/13] studio_name (): My Studio Name
  [13/13] department_name (Pipeline / R&D): Pipeline TD
```

## Next Steps
* Explore the generated files and directories.
* Customize the boilerplate to suit your project's needs.
* Implement your CLI, library functionality or Qt application and test your it.


## Happy Codding!
```vbnet
Let me know if you'd like further refinements or additional sections!
```