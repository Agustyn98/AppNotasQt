from backend import NotesDB

def add_data_listview(self):
# Creates a QListWidgetItem
    note_db = NotesDB()
    list_of_notes = note_db.get_list_of_notes()
    for note in list_of_notes:
        item_to_add = QtWidgets.QListWidgetItem()
        item_to_add.setText(note[1])
        item_to_add.setData(QtCore.Qt.UserRole, note[0])
        self.listWidget.addItem(item_to_add)