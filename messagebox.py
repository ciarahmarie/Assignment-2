from PyQt5.QtWidgets import QMessageBox

def invalidInfo(parent=None):
    return QMessageBox.information(parent, 'Add Student','Please fill all the fields and make sure the ID is unique.')

def confirmDelete(parent=None):
    prompt = QMessageBox.warning(parent,'Delete Student', 'Are you sure you want to proceed?', QMessageBox.Ok, QMessageBox.Cancel)
    if prompt == QMessageBox.Ok:
        return True
