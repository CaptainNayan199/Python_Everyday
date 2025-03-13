# checkboxes using pyqt5


# pyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QRadioButton, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 400, 1000, 1000)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift card", self)
        # different button groups
        self.button_gr1 = QButtonGroup(self)
        self.button_gr2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0,0,300,50)
        self.radio2.setGeometry(0,50,300,50)
        self.radio3.setGeometry(0,100,300,50)

        self.setStyleSheet("QRadioButton{"
                           "font-size : 40px;"
                           "font-family : arial;"
                           "padding:  50px;"
                           "}")
        self.button_gr1.addButton(self.radio1)
        self.button_gr1.addButton(self.radio2)
        self.button_gr2.addButton(self.radio3)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
