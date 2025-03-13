# stop watch program

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from PyQt5.QtCore import QTimer, QTime, Qt


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.label = QLabel("00:00:00:00", self)
        self.startButton = QPushButton("Start", self)
        self.stopButton = QPushButton("Stop", self)
        self.resetButton = QPushButton("reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stop Watch")
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.startButton)
        vbox.addWidget(self.stopButton)
        vbox.addWidget(self.resetButton)

        self.setLayout(vbox)

        self.label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.startButton)
        hbox.addWidget(self.stopButton)
        hbox.addWidget(self.resetButton)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton{
                font-size : 50px;
            }
            QLabel{
                font-size : 120px;
                background-color : hsl(200, 100%, 80%);
            }
        """)


    def start(self):
        pass

    def stop(self):
        pass

    def reset(self):
        pass

    def format_time(self, time):
        pass

    def update_display(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    stop_watch = StopWatch()
    stop_watch.show()
    sys.exit(app.exec_())
