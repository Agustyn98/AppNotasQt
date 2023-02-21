# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5 import QtWidgets
import os
import qdarktheme
from backend import NotesDB


# Import the converted .ui file
from ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def read_font_size() -> int:
    NotesDB.get_dir_path()
    config = NotesDB.create_config()
    with open(config) as f:
        for line in f:
            blocks = line.split(":")
            config = blocks[0]
            value = blocks[1]
            value = value.strip()
            if config == "font_size":
                if value.isnumeric():
                    return int(value)

                return 16


db_name = "notes.db"
dir_path = NotesDB.get_dir_path()
db_path = os.path.join(dir_path, db_name)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #app.lastWindowClosed.connect(upload_before_quitting)
    #download_before_starting()

    if True:
        font_size = read_font_size()
        font = QFont()
        font.setFamily('sans-serif')
        font.setPointSize(font_size)
        app.setFont(font)
        icons_path = f"{NotesDB.get_dir_path()}/icons/"
        app.setWindowIcon(QIcon(f'{icons_path}app_icon.jpg'))
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
