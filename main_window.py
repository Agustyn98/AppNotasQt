import sys
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
import qdarktheme


# Import the converted .ui file
from ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def read_font_size() -> int:
    with open("config") as f:
        for line in f:
            blocks = line.split(":")
            config = blocks[0]
            value = blocks[1]
            value = value.strip()
            if config == "font_size":
                print("SETTING FONT?")
                if value.isnumeric():
                    return int(value)

                return 13


def main():
    app = QtWidgets.QApplication(sys.argv)

    if True:
        font_size = read_font_size()
        font = QFont()
        font.setPointSize(font_size)
        app.setFont(font)
        qdarktheme.setup_theme(
            custom_colors={
                "primary": "#F166FF",
                "foreground": "#FFFFFF",
                "primary>list.selectionBackground": "9D479F",
                "primary>list.inactiveSelectionBackground": "#9D479F",
                "primary>list.inactiveSelectionBackground": "#783E7A",
                "input.background": "202124",
            }
        )


    else:
        app.setStyle("Fusion")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    if True:
        font_size = read_font_size()
        font = QFont()
        font.setPointSize(font_size)
        app.setFont(font)
        qdarktheme.setup_theme(
            custom_colors={
                "primary": "#F166FF",
                "foreground": "#FFFFFF",
                "primary>list.selectionBackground": "9D479F",
                "primary>list.inactiveSelectionBackground": "#9D479F",
                "primary>list.inactiveSelectionBackground": "#783E7A",
                "input.background": "202124",
            }
        )


    else:
        app.setStyle("Fusion")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
