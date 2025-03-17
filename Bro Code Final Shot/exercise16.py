# digital clock

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.timeLabel = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 1000,700)

        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)
        self.setLayout(vbox)

        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.timeLabel.setStyleSheet("font-size:200px;" "font-family: Arial;" "color:red;")
        self.setStyleSheet("background-color : black;")
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh : mm : ss AP")
        self.timeLabel.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())