# checkboxes using pyqt5


# pyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 400, 1000, 1000)
        self.checkbox = QCheckBox("Do you like dogs ? ", self)
        self.initUI()

    def initUI(self):
       self.checkbox.setStyleSheet("font-size:50px;" "font-family:Arial;")
       self.checkbox.setGeometry(10,10,800,100)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
