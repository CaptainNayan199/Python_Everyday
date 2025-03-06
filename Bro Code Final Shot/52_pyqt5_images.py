# pyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,400,1000,1000)

        label = QLabel(self)
        label.setGeometry(0,0,250,250)
        pixmap = QPixmap("test.png")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2 ,(self.height() - label.height()) // 2, label.width(), label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
