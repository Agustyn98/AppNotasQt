# -*- coding: utf-8 -*-
import datetime
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegularExpression, Qt
from PyQt5.QtGui import (
    QColor,
    QIcon,
    QKeyEvent,
    QKeySequence,
    QTextCharFormat,
    QTextCursor,
    QBrush,
)
from PyQt5.QtWidgets import QDesktopWidget, QDialog, QMessageBox, QLineEdit

from backend import NotesDB


class MyLineEdit(QLineEdit):
    def __init__(self, parent=None, main_window_instance=None):
        super().__init__(parent)
        self.main_window = main_window_instance

    def focusOutEvent(self, event):
        if self.main_window is not None:
            self.main_window.clear_highlighted_background(unfocused_flag=True)
        super().focusOutEvent(event)


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
        # self.main_label = QLabel(self.centralwidget)
        # self.main_label.setText("<html><font color='Magenta'>AppNotas</font></html>")
        # self.main_label.setStyleSheet("border: 1px solid white;")
        # self.main_label.setTextFormat(Qt.RichText)
        # self.main_label.setAlignment(Qt.AlignCenter)
        # self.horizontalLayout_3.addWidget(self.main_label)

        # Search note lineEdits
        # self.lineEdit_searchnote = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_searchnote = MyLineEdit(self.centralwidget, self)
        self.lineEdit_searchnote.setObjectName("lineEdit_searchnote")
        self.horizontalLayout_3.addWidget(self.lineEdit_searchnote)
        # Search all lineEdit
        self.lineEdit_searchall = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_searchall.setObjectName("lineEdit_searchall")
        self.horizontalLayout_3.addWidget(self.lineEdit_searchall)
        # ComboBox Font Size
        self.comboBox_fontcolor = QtWidgets.QComboBox(self.centralwidget)
        # self.comboBox_fontsize.setMaximumWidth(150)
        self.comboBox_fontcolor.addItem("Font Color")
        self.icons_path = f"{NotesDB.get_dir_path()}/icons/"
        self.comboBox_fontcolor.addItem(QIcon(f"{self.icons_path}red.png"), "Red", None)
        self.comboBox_fontcolor.addItem(QIcon(f"{self.icons_path}green.png"), "Green", None)
        self.comboBox_fontcolor.addItem(QIcon(f"{self.icons_path}blue.png"), "Blue", None)
        self.comboBox_fontcolor.addItem(QIcon(f"{self.icons_path}yellow.png"), "Yellow", None)
        self.comboBox_fontcolor.addItem(QIcon(f"{self.icons_path}purple.png"), "Purple", None)
        self.comboBox_fontcolor.addItem(QIcon(f"{self.icons_path}white.png"), "White", None)

        self.comboBox.setItemData(
            3, QColor(255, 0, 0), QtCore.Qt.ItemDataRole.TextColorRole
        )
        self.comboBox_fontcolor.setItemData(
            1, QBrush(Qt.GlobalColor.blue), Qt.ItemDataRole.TextColorRole
        )
        self.comboBox_fontcolor.setItemData(
            2, QBrush(Qt.GlobalColor.red), Qt.ItemDataRole.TextColorRole
        )

        self.comboBox_fontcolor.setStyleSheet
        self.horizontalLayout_3.addWidget(self.comboBox_fontcolor)
        # ComboBox Font Color
        # self.comboBox_fontcolor = QtWidgets.QComboBox(self.centralwidget)
        # self.comboBox_fontcolor.setMaximumWidth(120)
        # self.horizontalLayout_3.addWidget(self.comboBox_fontcolor)
        # Buttons
        self.checkbox_pin = QtWidgets.QCheckBox("🏱", self.centralwidget)
        self.checkbox_pin.setTristate(False)
        self.checkbox_pin.setObjectName("checkbox_pin")
        self.horizontalLayout_3.addWidget(self.checkbox_pin)
        self.horizontalLayout_3.setStretch(0, 40)
        self.horizontalLayout_3.setStretch(1, 58)
        self.horizontalLayout_3.setStretch(2, 58)
        self.horizontalLayout_3.setStretch(3, 10)
        self.horizontalLayout_3.setStretch(4, 1)
        self.horizontalLayout_3.setStretch(5, 10)
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
        self.lineEdit_title.setStyleSheet(
            "QLineEdit#lineEdit_title{color:MediumOrchid}"
        )
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(80)
        self.lineEdit_title.setFont(font)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.verticalLayout_3.addWidget(self.lineEdit_title)
        # QTextEdit
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setAcceptRichText(False)
        font = QtGui.QFont()
        if self._textedit_font is not None:
            font.setPointSize(self._textedit_font)
        else:
            font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit { padding: 6px; }")
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

        self.shortcut = QtWidgets.QShortcut(QKeySequence("Ctrl+B"), self)
        self.shortcut.activated.connect(lambda: self.change_font_type("bold"))
        self.shortcut = QtWidgets.QShortcut(QKeySequence("Ctrl+I"), self)
        self.shortcut.activated.connect(lambda: self.change_font_type("italic"))
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
        self.shortcut.activated.connect(lambda: self.checkbox_pin_activated())
        self.shortcut = QtWidgets.QShortcut(QKeySequence("Ctrl+M"), self)
        self.shortcut.activated.connect(lambda: self.comboBox.showPopup())
        self.shortcut = QtWidgets.QShortcut(QKeySequence("Ctrl+Shift+F"), self)
        self.shortcut.activated.connect(lambda: self.comboBox_fontcolor.showPopup())

        self.textEdit.textChanged.connect(lambda: self.unsaved_changes_text())
        self.lineEdit_title.textChanged.connect(
            lambda: self.unsaved_changes_text(w="title")
        )
        self.checkbox_pin.stateChanged.connect(
            lambda: self.unsaved_changes_text(w="pin")
        )
        self.comboBox_fontcolor.currentTextChanged.connect(
            lambda x: self.change_selection_fontcolor(x)
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
                #print("Youre editing the QEditText, therefore not refreshing. \n")
                self.edittext_changed = False
                return

        self.edittext_changed = False
        #print("Refreshing listview\n")

        if saved_flag:
            current_item_data = self.listWidget.currentItem().data(QtCore.Qt.UserRole)
            current_id = current_item_data[0]
            self.saved_flag = True

        self.listWidget.clear()

        if search_all_flag and len(self.lineEdit_searchall.text()) > 0:
            list_of_notes = self.note_db.search_notes(
                self.lineEdit_searchall.text(), self._case_sensitive_search
            )
        else:
            list_of_notes = self.note_db.get_list_of_notes()

        icon = QIcon(f"{self.icons_path}pin.png")
        for note in list_of_notes:
            item_to_add = QtWidgets.QListWidgetItem()
            if note[4] == 1:
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

        # This line causes lag loading a large note depending on the wrapping mode
        self.textEdit.setHtml(note[2])

        self.lineEdit_title.blockSignals(True)
        self.lineEdit_title.clear()
        self.lineEdit_title.blockSignals(False)
        self.lineEdit_title.setText(note[1])
        self.current_note_created = note[3]
        self.current_note_last_mod = note[4]
        self.current_note_id = id
        self.refresh_pin_checkbox()

    def combobox_changed(self, txt):
        if txt == "Save":
            self.note_db.update_note(self.current_note_id, self.textEdit.toHtml())
            # print("saved text!")
            self.add_data_listview(saved_flag=True)
            self.dont_update_list = 1

        elif txt == "New":
            self.note_db.add_note()
            self.add_data_listview()
            for item_index in range(self.listWidget.count()):
                item_data = self.listWidget.item(item_index).data(QtCore.Qt.UserRole)
                pin = item_data[1]
                if pin == 0:
                    self.listWidget.setCurrentRow(item_index)
                    self.lineEdit_title.setFocus()
                    break

        elif txt == "Delete":
            # self.note_db.delete_note()
            if self.listWidget.currentItem() is not None:
                data = self.listWidget.currentItem().data(QtCore.Qt.UserRole)
                id = data[0]
                # msgBox = QtWidgets.QMessageBox.warning(None, 'Confirmation', "Delete " + self.lineEdit_title.text()[:20] + ".. ?", QMessageBox.Yes | QMessageBox.No)
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Confirmation")
                msgBox.setText("Delete " + self.lineEdit_title.text()[:20] + ".. ?")
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                return_value = msgBox.exec()
                if return_value == QMessageBox.Yes:
                    self.note_db.delete_note(id)
                    self.add_data_listview()

        elif txt == "Info":
            self.open_info_dialog()

        elif txt == "Help":
            self.open_help_dialog()

        self.comboBox.setCurrentIndex(0)

    edittext_changed = True

    def unsaved_changes_text(self, w="text"):
        # print(f'text changed, chinging_listwidgetitem_flag: {self.changing_listwidgetitem_flag}')
        if w == "text":
            self.edittext_changed = True
        elif w == "title":
            if self.changing_listwidgetitem_flag == 1:
                self.changing_listwidgetitem_flag = 2
            elif self.changing_listwidgetitem_flag >= 2:
                self.changing_listwidgetitem_flag = 0
            else:
                self.save_note_title()
            return
        elif w == "pin":
            if self.changing_listwidgetitem_flag == 1:
                self.changing_listwidgetitem_flag = 2
            elif self.changing_listwidgetitem_flag >= 2:
                self.changing_listwidgetitem_flag = 0
            self.save_note_pin()
            return

        if self.changing_listwidgetitem_flag == 1:
            self.changing_listwidgetitem_flag = 2
            return
        elif self.changing_listwidgetitem_flag >= 2:
            self.changing_listwidgetitem_flag = 0
            return

        self.combobox_changed("Save")

    def search_in_note(self):
        word = self.lineEdit_searchnote.text()

        if len(word) < 1:
            return

        self.textEdit.blockSignals(True)
        cursor = self.textEdit.textCursor()
        # Setup the desired format for matches
        format = QTextCharFormat()
        format.setBackground(QColor(123, 85, 211))

        # Setup the regex engine
        if self._case_sensitive_search:
            re = QRegularExpression(word)
        else:
            re = QRegularExpression(word, QRegularExpression.CaseInsensitiveOption)

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

    def clear_highlighted_background(self, unfocused_flag=False):
        search = self.lineEdit_searchnote.text()
        if len(search) <= 0 or unfocused_flag:
            # IF YOU EXPERIENCE ISSUES UPDATING/SAVING, REMOVE THIS
            self.changing_listwidgetitem_flag = 2
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
                cursor = self.textEdit.textCursor()
                cursor.movePosition(QtGui.QTextCursor.End)
                self.textEdit.setTextCursor(cursor)

            elif self.listWidget.hasFocus():
                self.lineEdit_title.setFocus()
            else:
                self.listWidget.setFocus()

    def save_note_pin(self):
        pin = 1 if self.checkbox_pin.isChecked() else 0
        self.note_db.update_note_pin(self.current_note_id, pin)
        # print("saved pin!")
        self.add_data_listview(saved_flag=True)

    def save_note_title(self):
        self.note_db.update_note_title(self.current_note_id, self.lineEdit_title.text())
        # print("saved title!")
        self.add_data_listview(saved_flag=True)
        self.dont_update_list = 1

    def open_info_dialog(self):
        num_of_chars = len(self.textEdit.toPlainText())
        current_note_created_formatted = datetime.datetime.fromtimestamp(
            self.current_note_created
        ).strftime("%Y-%m-%d %H:%M:%S")
        current_note_last_mod_formatted = datetime.datetime.fromtimestamp(
            self.current_note_last_mod
        ).strftime("%Y-%m-%d %H:%M:%S")

        new_window = MyDialog(
            self.current_note_id,
            current_note_created_formatted,
            current_note_last_mod_formatted,
            num_of_chars,
        )
        new_window.exec_()

    def open_help_dialog(self):
        new_window = ShortcutsDialog()
        new_window.exec_()

    def change_font_type(self, type="bold"):
        if type == "bold":
            normal_weight = 50
            bold_weight = 80
            current_font_weight = self.textEdit.fontWeight()
            if current_font_weight <= normal_weight:
                self.textEdit.setFontWeight(bold_weight)
            else:
                self.textEdit.setFontWeight(normal_weight)
        elif type == "italic":
            is_italic = self.textEdit.fontItalic()
            self.textEdit.setFontItalic(not is_italic)

    def change_selection_fontcolor(self, color="White"):
        # self.textEdit.setFontPointSize(int(selected_size))
        if color == "Red":
            self.textEdit.setTextColor(QColor(255, 0, 0))
        elif color == "Green":
            self.textEdit.setTextColor(QColor(0, 255, 0))
        elif color == "Blue":
            self.textEdit.setTextColor(QColor(0, 128, 255))
        elif color == "Yellow":
            self.textEdit.setTextColor(QColor(255, 255, 0))
        elif color == "Purple":
            self.textEdit.setTextColor(QColor(186, 85, 211))
        elif color == "White":
            self.textEdit.setTextColor(QColor(255, 255, 255))

        self.comboBox_fontcolor.blockSignals(True)
        self.comboBox_fontcolor.setCurrentIndex(0)
        self.comboBox_fontcolor.blockSignals(False)

    def checkbox_pin_activated(self):
        self.checkbox_pin.setCheckState(not self.checkbox_pin.checkState())
        if self.checkbox_pin.checkState():
            self.checkbox_pin.setText("🏲")
        else:
            self.checkbox_pin.setText("🏱")

    def center_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    _textedit_font = None
    _case_sensitive_search = False

    def read_config(self):
        config_path = NotesDB.config_path
        with open(config_path) as f:
            for line in f:
                blocks = line.split(":")
                config = blocks[0]
                value = blocks[1]
                value = value.strip()

                if config == "font_size":
                    self._textedit_font = int(value)
                elif config == "window_size":
                    last_sizes = value.split("x")
                    self.MainWindow.resize(int(last_sizes[0]), int(last_sizes[1]))
                elif config == "window_center":
                    if value == "true":
                        self.center_screen()
                elif config == "case_sensitive_search":
                    self._case_sensitive_search = True if value == "true" else False


from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout


class MyDialog(QDialog):
    def __init__(self, id, created, last_mod, num_of_chars, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setWindowTitle("Note Information")
        layout = QVBoxLayout()
        text = f"""
                <table>
          <thead>
            <tr>
              <th>INFORMATION TABLE</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Database ID:</td>
              <td>{id}</td>
            </tr>
            <tr>
              <td>Date Created:</td>
              <td>{created}</td>
            </tr>
            <tr>
              <td>Last Modified:</td>
              <td>{last_mod}</td>
            </tr>
            <tr>
              <td>Char Count:</td>
              <td>{num_of_chars}</td>
            </tr>
          </tbody>
        </table>
        """
        label = QLabel(text)
        layout.addWidget(label)
        self.setLayout(layout)
        # layout = QVBoxLayout(self)
        # label1 = QLabel(f"database id: {id}")
        # layout.addWidget(label1)
        # label2 = QLabel(f"date created: {created}")
        # layout.addWidget(label2)
        # label3 = QLabel(f"date last modified: {last_mod}")
        # layout.addWidget(label3)
        # label4 = QLabel(f"Number of characters: {num_of_chars}")
        # layout.addWidget(label4)


class ShortcutsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shortcuts")
        layout = QVBoxLayout()
        text = (
            "<h2>Shortcuts:</h2>"
            "<ul>"
            "<li><b>Ctrl TAB</b> -> Cycle through list and text fields</li>"
            "<li><b>Ctrl F</b> -> Search in all notes</li>"
            "<li><b>Ctrl G</b> -> Search note</li>"
            "<li><b>Ctrl S</b> -> Manually save</li>"
            "<li><b>Ctrl N</b> -> New Note</li>"
            "<li><b>Ctrl D</b> -> Delete Note</li>"
            "<li><b>Ctrl P</b> -> Pin Note</li>"
            "<li><b>Ctrl M</b> -> Open Menu</li>"
            "<li><b>Ctrl Shift F</b> -> Open font color menu</li>"
            "<li><b>Ctrl B</b> -> Bold text</li>"
            "<li><b>Ctrl I</b> -> Italic text</li>"
            f"<h4>Configuration and DB: {NotesDB.app_dir}</h4>"
            f"<p style='text-align: center;'>Delete the config file to reset it</p>"
            "</ul>"
        )
        label = QLabel(text)
        layout.addWidget(label)
        self.setLayout(layout)
