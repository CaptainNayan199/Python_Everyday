# pyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,400,1000,1000)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("Nayan", self)
        label2 = QLabel("Sita", self)
        label3 = QLabel("Ujjwal", self)
        label4 = QLabel("Sitoshna", self)

        label1.setStyleSheet("background-color : red")
        label2.setStyleSheet("background-color : yellow")
        label3.setStyleSheet("background-color : Green")
        label4.setStyleSheet("background-color : orange")

        # vbox = QVBoxLayout()
        vbox = QGridLayout()

        vbox.addWidget(label1, 0, 0)
        vbox.addWidget(label2, 0 ,1)
        vbox.addWidget(label3, 1, 0)
        vbox.addWidget(label4, 1, 2)
        
        central_widget.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
