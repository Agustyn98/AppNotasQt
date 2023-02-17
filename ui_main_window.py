# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
    QIcon,
)
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QDialog,
    QDesktopWidget,
)
import os


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
        # Qlistwidget
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.horizontalScrollBar().setVisible(False)
        self.listWidget.verticalScrollBar().setVisible(False)
        #self.listWidget.setStyleSheet("QListWidget::item { border: 1px solid red }")
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
        self.lineEdit_title.textChanged.connect(lambda: self.unsaved_changes_text(w='title'))

        self.add_data_listview()
        self.listWidget.setFocus()

    note_db = NotesDB()

    saved_flag = False

    dont_update_list = 0
    def add_data_listview(self, saved_flag=False, search_all_flag=False):
        # Refresh listview
        print(f'current dont_update count: {self.dont_update_list}')
        if self.dont_update_list > 0:
            return

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
                icon = QIcon("pin.png")
                #item_to_add.setBackground(QColor(0, 128, 0))
                item_to_add.setIcon(icon)
            item_to_add.setText(note[1])
            item_to_add.setData(QtCore.Qt.UserRole, (note[0], note[4]))
            self.listWidget.addItem(item_to_add)

        #print("listWidget updated")

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

    changing_listwidgetitem_flag = 0

    def set_textedit_text(self, metadata, previous_obj=None):
        """Current item in listWidget changed"""

        id = metadata[0]

        #if previous_obj is None:
        #    print('DONT UPDATE LIST NOW, setting updoot to 0')
        #    self.dont_update_list = 0

        if previous_obj is not None:
            previous_obj = previous_obj.data(QtCore.Qt.UserRole)
            #print(f'previous obj is not none, its {previous_obj}, and current id is {id}')
            if id != previous_obj[0]:
                self.dont_update_list = 0
        
        # This prevents the listwidget from changing items when the note is saved
        if self.saved_flag:
            self.saved_flag = False
            return

        print("Changing current item in listwidget..")
        self.changing_listwidgetitem_flag = 1

        note = self.note_db.get_note_by_id(id)
        self.textEdit.setText(note[2])
        self.lineEdit_title.setText(note[1])
        self.refresh_pin_checkbox()
        Ui_MainWindow.unsaved_changes = False

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
            Ui_MainWindow.unsaved_changes = False
            current_item_data = self.listWidget.currentItem().data(QtCore.Qt.UserRole)
            id = current_item_data[0]
            pin = 1 if self.checkbox_pin.isChecked() else 0
            self.note_db.update_note(
                id, self.lineEdit_title.text(), self.textEdit.toPlainText(), pin
            )
            self.add_data_listview(saved_flag=True)
            self.dont_update_list += 1

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

        if txt == "Settings":
            self.open_setting_dialog()

        self.comboBox.setCurrentIndex(0)

    unsaved_changes = False

    def unsaved_changes_text(self, w='text'):
        if self.changing_listwidgetitem_flag == 1:
            self.changing_listwidgetitem_flag += 1
            return
        elif self.changing_listwidgetitem_flag >= 2:
            self.changing_listwidgetitem_flag = 0
            return

        print('\nsaving...\n\n')
        self.combobox_changed("Save")

    def search_in_note(self):
        word = self.lineEdit_searchnote.text()

        cursor = self.textEdit.textCursor()
        # Setup the desired format for matches
        format = QTextCharFormat()
        # format.setBackground(QBrush(QColor("yellow")))
        format.setBackground(QColor(160,80,160))

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
            format.setBackground(QColor(32,33,36))
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

    def open_setting_dialog(self):
        return
        new_window = MyDialog()
        new_window.setWindowTitle("New Window")
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
                    print('SETTING FONT?')
                    font = QtGui.QFont()
                    font.setPointSize(int(value))
                    self.MainWindow.setFont(font)
                elif config == "window_size":
                    last_sizes = value.split("x")
                    self.MainWindow.resize(int(last_sizes[0]), int(last_sizes[1]))
                elif config == "window_center":
                    if value == "true":
                        self.center_screen()
