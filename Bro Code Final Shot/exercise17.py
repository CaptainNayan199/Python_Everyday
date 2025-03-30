# stop watch program

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.label2 = QLabel("Made By Nayan for Practice ✅")
        self.label = QLabel("00:00:00:00", self)
        self.startButton = QPushButton("Start", self)
        self.stopButton = QPushButton("Stop", self)
        self.resetButton = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stop Watch")
        self.setGeometry(500,500,1000,450)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.startButton)
        vbox.addWidget(self.stopButton)
        vbox.addWidget(self.resetButton)

        self.setLayout(vbox)

        self.label.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.startButton)
        hbox.addWidget(self.stopButton)
        hbox.addWidget(self.resetButton)

        vbox.addLayout(hbox)
        vbox.addWidget(self.label2)
        self.label2.setObjectName("label2")

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding : 20px;
                font-weight : bold;
                font-family : calibri;
            }
            QPushButton{
                font-size : 50px;
            }
            QLabel{
                font-size : 120px;
                background-color : hsl(200, 100%, 80%);
                border-radius: 15px;
                
            }
            QLabel#label2{
                font-size : 20px;
                background-color : white;
            }
        """)

        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.resetButton.clicked.connect(self.reset)

        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        second = time.second()
        ms = time.msec() // 10
        return f"{hours:02} : {minutes:02} : {second:02} : {ms:02}"

    def update_display(self):
        self.time =  self.time.addMSecs(10)
        self.label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stop_watch = StopWatch()
    stop_watch.show()
    sys.exit(app.exec_())