import sys
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from qt_material import apply_stylesheet



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
                    print('SETTING FONT?')
                    if value.isnumeric():
                        return int(value)

                    return 13


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    extra = {

    # Font
    'font_size': '17px',
    }

    if False:
        font_size = read_font_size()
        font = QFont()
        font.setPointSize(font_size)
        app.setFont(font)
        apply_stylesheet(app, theme='dark_pink.xml', extra=extra)
    else:
        app.setStyle('Fusion')

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


