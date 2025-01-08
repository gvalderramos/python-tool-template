"""Main app."""
import sys

from {{cookiecutter.project_slug}}.resource import resource
from {{cookiecutter.project_slug}}.resource.ui.mainwindow import MainWindow


def apply_stylesheet(app, css_path):
    css_file = QFile(css_path)
    if not css_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {css_path}: {css_file.errorString()}")
        return
    css = css_file.readAll().data().decode("utf-8")
    app.setStyleSheet(css)
    css_file.close()

def run():
    app = QApplication(sys.argv)
    main_window = MainWindow()

    # Apply stylesheet from resource system
    apply_stylesheet(app, ":/resource/css/mainwindow.css")

    # Show the main window
    main_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    run()
