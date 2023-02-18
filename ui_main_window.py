import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegularExpression, Qt
from PyQt5.QtGui import (
    QColor,
    QIcon,
    QKeyEvent,
    QKeySequence,
    QTextCharFormat,
    QTextCursor,
    QPixmap,
)
from PyQt5.QtWidgets import QDesktopWidget, QDialog, QMessageBox

from backend import NotesDB


class Ui_MainWindow(object):
    app_title_str = "AppNotas"

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.keyPressEvent = self.newOnkeyPressEvent
        # font = QtGui.QFont()
        # font.setPointSize(14)
        # MainWindow.setFont(font)
        self.read_config()
        # self.MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        # Title label
        #self.main_label = QLabel(self.centralwidget)
        #self.main_label.setText("<html><font color='Magenta'>AppNotas</font></html>")
        #self.main_label.setStyleSheet("border: 1px solid white;")
        #self.main_label.setTextFormat(Qt.RichText)
        #self.main_label.setAlignment(Qt.AlignCenter)
        #self.horizontalLayout_3.addWidget(self.main_label)
        # Search lineEdits
        self.lineEdit_searchall = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_searchall.setObjectName("lineEdit_searchall")
        self.horizontalLayout_3.addWidget(self.lineEdit_searchall)
        self.lineEdit_searchnote = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_searchnote.setObjectName("lineEdit_searchnote")
        self.horizontalLayout_3.addWidget(self.lineEdit_searchnote)
        # Buttons
        self.checkbox_pin = QtWidgets.QCheckBox("🏱", self.centralwidget)
        self.checkbox_pin.setTristate(False)
        self.checkbox_pin.setObjectName("checkbox_pin")
        self.horizontalLayout_3.addWidget(self.checkbox_pin)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        # Qlistwidget
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setAlternatingRowColors(True)
        # self.listWidget.horizontalScrollBar().setVisible(False)
        # self.listWidget.verticalScrollBar().setVisible(False)
        # self.listWidget.setStyleSheet("QListWidget::item { border: 1px solid red }")
        self.listWidget.setStyleSheet("QListWidget:focus { border: 1px solid #F166FF}")
        # self.listWidget.setWrapping(True)

        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_title = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_title.setFont(font)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.verticalLayout_3.addWidget(self.lineEdit_title)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 95)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.app_title_str))
        self.comboBox.setPlaceholderText(_translate("MainWindow", "Menu"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Menu"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Save"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Delete"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Info"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Help"))
        self.lineEdit_searchall.setPlaceholderText(
            _translate("MainWindow", "Search All")
        )
        self.lineEdit_searchnote.setPlaceholderText(
            _translate("MainWindow", "Search Note")
        )

        self.comboBox.currentTextChanged.connect(lambda x: self.combobox_changed(x))

        self.lineEdit_searchall.returnPressed.connect(
            lambda: self.add_data_listview(search_all_flag=True)
        )
        self.lineEdit_searchall.textChanged.connect(lambda: self.clear_searchall())

        # self.listWidget.itemClicked.connect(lambda: self.check_changes_before_leaving())
        self.listWidget.currentItemChanged.connect(
            lambda x, previous: self.set_textedit_text(
                x.data(QtCore.Qt.UserRole), previous_obj=previous
            )
            if x is not None
            else x
        )

        self.lineEdit_searchnote.returnPressed.connect(lambda: self.search_in_note())
        self.lineEdit_searchnote.textChanged.connect(
            lambda x: self.clear_highlighted_background()
        )

        self.shortcut = QtWidgets.QShortcut(QKeySequence("Ctrl+S"), self)
        self.shortcut.activated.connect(lambda: self.combobox_changed(txt="Save"))
        self.shortcut = QtWidgets.QShortcut(QKeySequence("Ctrl+N"), self)
        self.shortcut.activated.connect(lambda: self.combobox_changed(txt="New"))
        self.shortcut = QtWidgets.QShortcut(QKeySequence("Ctrl+D"), self)
        self.shortcut.activated.connect(lambda: self.combobox_changed(txt="Delete"))
        self.shortcut = QtWidgets.QShortcut(QKeySequence("Ctrl+F"), self)
        self.shortcut.activated.connect(lambda: self.lineEdit_searchnote.setFocus())
        self.shortcut = QtWidgets.QShortcut(QKeySequence("Ctrl+G"), self)
        self.shortcut.activated.connect(lambda: self.lineEdit_searchall.setFocus())
        self.shortcut = QtWidgets.QShortcut(QKeySequence("Ctrl+P"), self)
        self.shortcut.activated.connect(
            lambda: self.checkbox_pin.setCheckState(not self.checkbox_pin.checkState())
        )
        self.shortcut = QtWidgets.QShortcut(QKeySequence("Ctrl+M"), self)
        self.shortcut.activated.connect(lambda: self.comboBox.showPopup())

        self.textEdit.textChanged.connect(lambda: self.unsaved_changes_text())
        self.lineEdit_title.textChanged.connect(
            lambda: self.unsaved_changes_text(w="title")
        )
        self.checkbox_pin.stateChanged.connect(
            lambda: self.unsaved_changes_text(w="pin")
        )

        self.add_data_listview()
        self.listWidget.setFocus()

    note_db = NotesDB()

    saved_flag = False

    dont_update_list = 0

    def add_data_listview(self, saved_flag=False, search_all_flag=False):
        """Refresh listview"""

        if self.dont_update_list > 0:
            if self.edittext_changed:
                print("Youre editing the QEditText, therefore not refreshing. \n")
                self.edittext_changed = False
                return

        self.edittext_changed = False
        print("Refreshing listview")

        if saved_flag:
            current_item_data = self.listWidget.currentItem().data(QtCore.Qt.UserRole)
            current_id = current_item_data[0]
            self.saved_flag = True

        self.listWidget.clear()

        if search_all_flag and len(self.lineEdit_searchall.text()) > 0:
            list_of_notes = self.note_db.search_notes(self.lineEdit_searchall.text())
        else:
            list_of_notes = self.note_db.get_list_of_notes()

        for note in list_of_notes:
            item_to_add = QtWidgets.QListWidgetItem()
            if note[4] == 1:
                icon = QIcon("pin.png")
                item_to_add.setIcon(icon)
            item_to_add.setText(note[1])
            item_to_add.setData(QtCore.Qt.UserRole, (note[0], note[4]))
            self.listWidget.addItem(item_to_add)

        if saved_flag:
            for item_index in range(self.listWidget.count()):
                item_data = self.listWidget.item(item_index).data(QtCore.Qt.UserRole)
                id = item_data[0]
                if id == current_id:
                    self.listWidget.setCurrentRow(item_index)
                    break
        else:
            self.listWidget.setCurrentRow(0)

    def refresh_pin_checkbox(self):
        self.checkbox_pin.blockSignals(True)
        current_item_data = self.listWidget.currentItem().data(QtCore.Qt.UserRole)
        pin = current_item_data[1]
        if pin == 1:
            self.checkbox_pin.setChecked(True)
            self.checkbox_pin.setText("🏲")
        else:
            self.checkbox_pin.setChecked(False)
            self.checkbox_pin.setText("🏱")

        self.checkbox_pin.blockSignals(False)

    changing_listwidgetitem_flag = 0

    current_note_created = current_note_last_mod = current_note_id = None

    def set_textedit_text(self, metadata, previous_obj=None):
        """Current item in listWidget changed"""
        # print('current item changed inlistwidget')

        id = metadata[0]

        if previous_obj is not None:
            previous_obj = previous_obj.data(QtCore.Qt.UserRole)
            # print(f'previous obj is not none, its {previous_obj}, and current id is {id}')
            if id != previous_obj[0]:
                self.dont_update_list = 0

        # This prevents the listwidget from changing items when the note is saved
        if self.saved_flag:
            self.saved_flag = False
            return

        # print("Changing current item in listwidget..")
        self.changing_listwidgetitem_flag = 1

        note = self.note_db.get_note_by_id(id)
        self.textEdit.setText(note[2])
        self.lineEdit_title.setText(note[1])
        self.current_note_created = note[3]
        self.current_note_last_mod = note[4]
        self.current_note_id = id
        self.refresh_pin_checkbox()

    def combobox_changed(self, txt):
        if txt == "New":
            self.note_db.add_note()
            self.add_data_listview()
            for item_index in range(self.listWidget.count()):
                item_data = self.listWidget.item(item_index).data(QtCore.Qt.UserRole)
                pin = item_data[1]
                if pin == 0:
                    self.listWidget.setCurrentRow(item_index)
                    self.lineEdit_title.setFocus()
                    break

        if txt == "Save":
            current_item_data = self.listWidget.currentItem().data(QtCore.Qt.UserRole)
            id = current_item_data[0]
            pin = 1 if self.checkbox_pin.isChecked() else 0
            self.note_db.update_note(
                id, self.lineEdit_title.text(), self.textEdit.toPlainText(), pin
            )
            self.add_data_listview(saved_flag=True)
            self.dont_update_list = 1

        if txt == "Delete":
            # self.note_db.delete_note()
            if self.listWidget.currentItem() is not None:
                data = self.listWidget.currentItem().data(QtCore.Qt.UserRole)
                id = data[0]
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Delete " + self.lineEdit_title.text()[:20] + ".. ?")
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                return_value = msgBox.exec()
                if return_value == QMessageBox.Yes:
                    self.note_db.delete_note(id)
                    self.add_data_listview()

        if txt == "Info":
            self.open_info_dialog()
        
        if txt == "Help":
            self.open_help_dialog()

        self.comboBox.setCurrentIndex(0)

    edittext_changed = True

    def unsaved_changes_text(self, w="text"):
        if w == "text":
            self.edittext_changed = True

        if self.changing_listwidgetitem_flag == 1:
            self.changing_listwidgetitem_flag = 2
            return
        elif self.changing_listwidgetitem_flag >= 2:
            self.changing_listwidgetitem_flag = 0
            return

        self.combobox_changed("Save")

    def search_in_note(self):
        self.textEdit.blockSignals(True)
        word = self.lineEdit_searchnote.text()

        if len(word) < 1:
            return

        cursor = self.textEdit.textCursor()
        # Setup the desired format for matches
        format = QTextCharFormat()
        format.setBackground(QColor(160, 80, 160))

        # Setup the regex engine
        re = QRegularExpression(word)
        i = re.globalMatch(
            self.textEdit.toPlainText()
        )  # QRegularExpressionMatchIterator
        # iterate through all the matches and highlight
        while i.hasNext():
            match = i.next()  # QRegularExpressionMatch
            # Select the matched text and apply the desired format
            cursor.setPosition(match.capturedStart(), QTextCursor.MoveAnchor)
            cursor.setPosition(match.capturedEnd(), QTextCursor.KeepAnchor)
            cursor.mergeCharFormat(format)

        self.textEdit.blockSignals(False)

    def clear_highlighted_background(self):
        search = self.lineEdit_searchnote.text()
        if len(search) <= 0:
            cursor = self.textEdit.textCursor()
            format = QTextCharFormat()
            format.setBackground(QColor(32, 33, 36))
            cursor.setPosition(0, QTextCursor.MoveAnchor)
            cursor.setPosition(len(self.textEdit.toPlainText()), QTextCursor.KeepAnchor)
            cursor.mergeCharFormat(format)

    def clear_searchall(self):
        search = self.lineEdit_searchall.text()
        if len(search) <= 0:
            self.add_data_listview()

    def newOnkeyPressEvent(self, event: QKeyEvent):
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Tab:
            if self.textEdit.hasFocus():
                self.listWidget.setFocus()
            elif self.lineEdit_title.hasFocus():
                self.textEdit.setFocus()
                # get a QTextCursor object to manipulate the text cursor
                cursor = self.textEdit.textCursor()
                # move the cursor to the end of the text
                cursor.movePosition(QtGui.QTextCursor.End)
                # set the text cursor to the updated cursor position
                self.textEdit.setTextCursor(cursor)

            elif self.listWidget.hasFocus():
                self.lineEdit_title.setFocus()
            else:
                self.listWidget.setFocus()

    def open_info_dialog(self):
        num_of_chars = len(self.textEdit.toPlainText())
        current_note_created_formatted = datetime.datetime.fromtimestamp(
            self.current_note_created
        ).strftime("%Y-%m-%d %H:%M:%S")
        current_note_last_mod_formatted = datetime.datetime.fromtimestamp(
            self.current_note_last_mod
        ).strftime("%Y-%m-%d %H:%M:%S")

        new_window = MyDialog(self.current_note_id, current_note_created_formatted, current_note_last_mod_formatted, num_of_chars)
        new_window.exec_()

    
    def open_help_dialog(self):
        new_window = ShortcutsDialog()
        new_window.exec_()

    def center_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def read_config(self):
        with open("config") as f:
            for line in f:
                blocks = line.split(":")
                config = blocks[0]
                value = blocks[1]
                value = value.strip()

                if config == "font_size":
                    print("SETTING FONT?")
                    font = QtGui.QFont()
                    font.setPointSize(int(value))
                    self.MainWindow.setFont(font)
                elif config == "window_size":
                    last_sizes = value.split("x")
                    self.MainWindow.resize(int(last_sizes[0]), int(last_sizes[1]))
                elif config == "window_center":
                    if value == "true":
                        self.center_screen()


from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel


class MyDialog(QDialog):
    def __init__(self, id, created, last_mod, num_of_chars, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setWindowTitle("Note Information")
        layout = QVBoxLayout(self)
        label1 = QLabel(f"database id: {id}")
        layout.addWidget(label1)
        label2 = QLabel(f"date created: {created}")
        layout.addWidget(label2)
        label3 = QLabel(f"date last modified: {last_mod}")
        layout.addWidget(label3)
        label4 = QLabel(f"Number of characters: {num_of_chars}")
        layout.addWidget(label4)


class ShortcutsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Shortcuts')
        layout = QVBoxLayout()
        text = '<h2>Shortcuts:</h2>' \
               '<ul>' \
               '<li><b>Ctrl TAB</b> -> Cycle through main widgets</li>' \
               '<li><b>Ctrl F</b> -> Search all</li>' \
               '<li><b>Ctrl G</b> -> Search note</li>' \
               '<li><b>Ctrl S</b> -> Manually save</li>' \
               '<li><b>Ctrl N</b> -> New Note</li>' \
               '<li><b>Ctrl D</b> -> Delete Note</li>' \
               '<li><b>Ctrl P</b> -> Pin Note</li>' \
               '<li><b>Ctrl M</b> -> Open Menu</li>' \
               '</ul>'
        label = QLabel(text)
        layout.addWidget(label)
        self.setLayout(layout)