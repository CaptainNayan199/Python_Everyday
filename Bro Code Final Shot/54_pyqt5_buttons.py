# pyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 400, 1000, 1000)

        self.initUI()

    def initUI(self):
        button = QPushButton("Login", self)
        button.setGeometry(350,400,200,100)
        button.setStyleSheet("font-size:30px")
        button.clicked.connect(self.on_Click)


    def on_Click(self):
        print("Button is clicked!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
