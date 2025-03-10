# pyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 400, 1000, 1000)
        self.button = QPushButton("Login", self)
        self.label = QLabel("Universe!", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(350,400,200,100)
        self.button.setStyleSheet("font-size:30px")
        self.button.clicked.connect(self.on_Click)
        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size:50;")

    def on_Click(self):
        print("Button is clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        self.label.setText("Milkyway!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
