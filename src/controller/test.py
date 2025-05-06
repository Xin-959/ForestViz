from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

app = QApplication([])
window = QMainWindow()
window.setCentralWidget(QLabel("Hello PyQt5!"))
window.show()
app.exec_()
