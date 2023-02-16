# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from dialog import MyDialog
from PyQt5.QtCore import Qt, QRegExp, QRegularExpression
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QKeySequence
from backend import NotesDB
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtGui import (
    QTextCursor,
    QColor,
    QTextDocument,
    QTextCharFormat,
    QBrush,
    QPalette,
)
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QDesktopWidget
import os


class Ui_MainWindow(object):
    class MyListWidget(QtWidgets.QListWidget):
        def __init__(self, outer_instance):
            super(Ui_MainWindow.MyListWidget, self).__init__()
            self.outer_instance = outer_instance

        def keyPressEvent(self, event: QKeyEvent) -> None:
            if (
                event.key() == QtCore.Qt.Key.Key_Up
                or event.key() == QtCore.Qt.Key.Key_Down
            ):
                check = self.check_changes_before_leaving()
                if check == "cancel":
                    return
                super().keyPressEvent(event)

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Tab:
                self.outer_instance.lineEdit_title.setFocus()

        def check_changes_before_leaving(self):
            if Ui_MainWindow.unsaved_changes:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Save changes?")
                msgBox.setStandardButtons(
                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
                )
                return_value = msgBox.exec()
                if return_value == QMessageBox.Yes:
                    self.outer_instance.combobox_changed("Save")
                    self.outer_instance.MainWindow.setWindowTitle(
                        Ui_MainWindow.app_title_str
                    )
                    Ui_MainWindow.unsaved_changes = False
                    pass
                elif return_value == QMessageBox.No:
                    self.outer_instance.MainWindow.setWindowTitle(
                        Ui_MainWindow.app_title_str
                    )
                    Ui_MainWindow.unsaved_changes = False
                else:
                    return "cancel"

    def create_list_widget(self):
        return Ui_MainWindow.MyListWidget(self)

    app_title_str = "AppNotas"

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.keyPressEvent = self.newOnkeyPressEvent
        #font = QtGui.QFont()
        #font.setPointSize(14)
        #MainWindow.setFont(font)
        self.read_config()
        #self.MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(2)
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
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
        # self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        # self.listWidget = self.MyListWidget(self.centralwidget)
        self.listWidget = self.create_list_widget()
        # self.listWidget.setObjectName("listWidget")
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
        self.comboBox.setItemText(5, _translate("MainWindow", "Import"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Export"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Settings"))
        self.lineEdit_searchall.setPlaceholderText(
            _translate("MainWindow", "Search All")
        )
        self.lineEdit_searchnote.setPlaceholderText(
            _translate("MainWindow", "Search Note")
        )

        self.comboBox.currentTextChanged.connect(lambda x: self.combobox_changed(x))

        self.add_data_listview()

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

        # self.listWidget.currentItemChanged.connect(
        #    lambda x, previous: self.set_textedit_text(x.data(QtCore.Qt.UserRole), previous_obj=previous.data(QtCore.Qt.UserRole))
        #    if x is not None
        #    else x
        # )

        # self.listWidget.currentRowChanged.connect(
        #    lambda x: self.set_textedit_text()
        #    if x is not None
        #    else x
        # )

        self.lineEdit_searchnote.returnPressed.connect(lambda: self.search_in_note())
        self.lineEdit_searchnote.textChanged.connect(
            lambda x: self.clear_highlighted_background()
        )

        # self.listWidget.keyPressEvent = self.list_key_press_event

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
        self.shortcut.activated.connect(lambda: self.checkbox_pin.setCheckState(not self.checkbox_pin.checkState()))

        self.textEdit.textChanged.connect(lambda: self.unsaved_changes_text())

        self.listWidget.setTabOrder(self.lineEdit_title, self.textEdit)
        self.lineEdit_title.setTabOrder(self.textEdit, self.listWidget)
        self.textEdit.setTabOrder(self.listWidget, self.lineEdit_title)

        self.listWidget.setFocus()

    note_db = NotesDB()

    saved_flag = False

    def add_data_listview(self, saved_flag=False, search_all_flag=False):
        # Refresh listview
        if saved_flag:
            current_item_data = self.listWidget.currentItem().data(QtCore.Qt.UserRole)
            current_id = current_item_data[0]
            self.saved_flag = True

        self.listWidget.clear()
        if search_all_flag:
            list_of_notes = self.note_db.search_notes(self.lineEdit_searchall.text())
        else:
            list_of_notes = self.note_db.get_list_of_notes()
        for note in list_of_notes:
            item_to_add = QtWidgets.QListWidgetItem()
            if note[4] == 1:
                item_to_add.setBackground(QColor("yellow"))
            item_to_add.setText(note[1])
            item_to_add.setData(QtCore.Qt.UserRole, (note[0], note[4]))
            self.listWidget.addItem(item_to_add)

        if saved_flag:
            for item_index in range(self.listWidget.count()):
                item_data = self.listWidget.item(item_index).data(QtCore.Qt.UserRole)
                id = item_data[0]
                if id == current_id:
                    self.listWidget.setCurrentRow(item_index)

    def refresh_pin_checkbox(self):
        current_item_data = self.listWidget.currentItem().data(QtCore.Qt.UserRole)
        pin = current_item_data[1]
        if pin == 1:
            self.checkbox_pin.setChecked(True)
            self.checkbox_pin.setText("🏲")
        else:
            self.checkbox_pin.setChecked(False)
            self.checkbox_pin.setText("🏱")

    cancel_flag = False
    last_index_for_cancel = None

    def set_textedit_text(self, metadata, previous_obj=None):
        if self.cancel_flag:
            self.cancel_flag = False
            self.unsaved_changes = False
            return


        res_question = self.check_changes_before_leaving()
        if res_question == "Yes" and previous_obj is not None:
            Ui_MainWindow.unsaved_changes = False
            # self.MainWindow.setWindowTitle(self.app_title_str)
            current_item_data = previous_obj.data(QtCore.Qt.UserRole)
            id = current_item_data[0]
            pin = 1 if self.checkbox_pin.isChecked() else 0
            self.note_db.update_note(
                id, self.lineEdit_title.text(), self.textEdit.toPlainText(), pin
            )
            self.add_data_listview(saved_flag=True)
            for item_index in range(self.listWidget.count()):
                item_data = self.listWidget.item(item_index).data(QtCore.Qt.UserRole)
                id_current = item_data[0]
                if id == id_current:
                    self.listWidget.setCurrentRow(item_index)

            return

        if res_question == "cancel" and previous_obj is not None:
            previous_obj = previous_obj.data(QtCore.Qt.UserRole)
            current_id = previous_obj[0]
            for item_index in range(self.listWidget.count()):
                item_data = self.listWidget.item(item_index).data(QtCore.Qt.UserRole)
                id = item_data[0]
                if id == current_id:
                    self.cancel_flag = True
                    self.last_index_for_cancel = item_index
                    self.listWidget.setCurrentRow(item_index)
                    return

        if previous_obj is not None:
            previous_obj = previous_obj.data(QtCore.Qt.UserRole)

        if self.saved_flag:
            self.saved_flag = False
            return

        id = metadata[0]
        note = self.note_db.get_note_by_id(id)
        self.textEdit.setText(note[2])
        self.lineEdit_title.setText(note[1])
        self.refresh_pin_checkbox()
        Ui_MainWindow.unsaved_changes = False
        self.MainWindow.setWindowTitle(self.app_title_str)

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
            # self.listWidget.setCurrentRow(0)
            Ui_MainWindow.unsaved_changes = False
            # self.MainWindow.setWindowTitle(self.app_title_str)
            current_item_data = self.listWidget.currentItem().data(QtCore.Qt.UserRole)
            id = current_item_data[0]
            pin = 1 if self.checkbox_pin.isChecked() else 0
            self.note_db.update_note(
                id, self.lineEdit_title.text(), self.textEdit.toPlainText(), pin
            )
            self.add_data_listview(saved_flag=True)

        if txt == "Delete":
            # self.note_db.delete_note()
            if self.listWidget.currentItem() is not None:
                data = self.listWidget.currentItem().data(QtCore.Qt.UserRole)
                id = data[0]
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Delete " + self.lineEdit_title.text()[:20] + ".. ?")
                msgBox.setStandardButtons(
                    QMessageBox.Yes | QMessageBox.No
                )
                return_value = msgBox.exec()
                if return_value == QMessageBox.Yes:
                    self.note_db.delete_note(id)
                    self.add_data_listview()

        
        if txt == "Settings":
            self.open_setting_dialog()

        self.comboBox.setCurrentIndex(0)

    unsaved_changes = False

    def unsaved_changes_text(self):
        if not Ui_MainWindow.unsaved_changes:
            self.MainWindow.setWindowTitle("* " + self.app_title_str + " *")
            Ui_MainWindow.unsaved_changes = True

    def search_in_note(self):
        word = self.lineEdit_searchnote.text()

        cursor = self.textEdit.textCursor()
        # Setup the desired format for matches
        format = QTextCharFormat()
        # format.setBackground(QBrush(QColor("yellow")))
        format.setBackground(QColor("yellow"))

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

    def clear_highlighted_background(self):
        search = self.lineEdit_searchnote.text()
        if len(search) <= 0:
            cursor = self.textEdit.textCursor()
            format = QTextCharFormat()
            format.setBackground(QColor("white"))
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
            elif self.listWidget.hasFocus():
                self.lineEdit_title.setFocus()
            else:
                self.listWidget.setFocus()

    def check_changes_before_leaving(self):
        if Ui_MainWindow.unsaved_changes:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Save changes?")
            msgBox.setStandardButtons(
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )
            return_value = msgBox.exec()
            if return_value == QMessageBox.Yes:
                # self.combobox_changed("Save")
                self.MainWindow.setWindowTitle(Ui_MainWindow.app_title_str)
                return "Yes"
            elif return_value == QMessageBox.No:
                self.MainWindow.setWindowTitle(Ui_MainWindow.app_title_str)
                Ui_MainWindow.unsaved_changes = False
            else:
                return "cancel"

    def open_setting_dialog(self):
        new_window = MyDialog()
        new_window.setWindowTitle("New Window")
        new_window.exec_()


    def center_screen(self):
        screen = QDesktopWidget().screenGeometry()

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    
    def read_config(self):
        with open('config') as f:
            for line in f:
                blocks = line.split(':')
                config = blocks[0]
                value = blocks[1]
                value = value.strip()

                if config == 'font_size':
                    font = QtGui.QFont()
                    font.setPointSize(int(value))
                    self.MainWindow.setFont(font)
                elif config == 'window_size':
                    last_sizes = value.split('x')
                    self.MainWindow.resize(int(last_sizes[0]), int(last_sizes[1]))
                elif config == 'window_center':
                    if value == 'true':
                        self.center_screen()




