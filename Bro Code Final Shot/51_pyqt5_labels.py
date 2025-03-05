# pyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(40,40,500,500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(10,20,500,100)
        label.setStyleSheet("color:red;""background-color:yellow")
        # label.setAlignment(Qt.AlignRight)
        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
