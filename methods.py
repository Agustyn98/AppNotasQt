from backend import NotesDB


        self.add_data_listview()

        self.listWidget.itemActivated.connect(
            lambda x: self.set_textedit_text(x.data(QtCore.Qt.UserRole))
        )

        self.listWidget.clicked.connect(
            lambda x: self.set_textedit_text(x.data(QtCore.Qt.UserRole))
        )
        
        self.listWidget.currentItemChanged.connect(
            lambda x: self.set_textedit_text(x.data(QtCore.Qt.UserRole))
        )

    note_db = NotesDB()

    def add_data_listview(self):
        # Creates a QListWidgetItem
        list_of_notes = self.note_db.get_list_of_notes()
        for note in list_of_notes:
            item_to_add = QtWidgets.QListWidgetItem()
            item_to_add.setText(note[1])
            item_to_add.setData(QtCore.Qt.UserRole, note[0])
            self.listWidget.addItem(item_to_add)

    def set_textedit_text(self, id):
        note = self.note_db.get_note_by_id(id)
        self.textEdit.setText(txt)