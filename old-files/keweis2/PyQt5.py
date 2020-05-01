from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit
app = QApplication([])
window = QMainWindow()
window.resize(500,400)
window.move(300,310)
window.setWindowTitle("grade overview")

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("please enter grade")
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton("overall", window)
button.move(380,80)
window.show()
app.exec_()

