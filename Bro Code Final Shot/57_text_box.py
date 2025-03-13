# checkboxes using pyqt5


# pyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton ,QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 400, 1000, 1000)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10,10,250,50)
        self.line_edit.setStyleSheet("font-size : 25px;" "font-family : arial;" "border : 1px solid black;" "border-radius : 7px;")
        self.button.setGeometry(270,10,100,50)
        self.button.setStyleSheet("font-size : 25px;" "font-family : arial;" "background-color: yellow;""border : 1px solid black;" "border-radius : 7px;")
        self.button.clicked.connect(self.submit)
        self.line_edit.setPlaceholderText("Enter your name : ")

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
