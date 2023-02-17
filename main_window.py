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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    if False:
        qdarktheme.setup_theme()
    else:
        app.setStyle('Fusion')

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

