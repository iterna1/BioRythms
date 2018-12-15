import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(259, 160)
        self.setStyleSheet('QWidget{background-color: #F5F5DC;}')
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('BioRythms')

        label = QLabel('Добро пожаловать в BioRythms', self)
        label.setStyleSheet('QLabel{color: #8B0000;}')
        label.setFont(QFont('Calibri', 13, QFont.Bold))
        label.adjustSize()

        button = QPushButton('Старт', self)
        button.setStyleSheet('QPushButton{background-color: #8B0000; color: #F5F5DD}')
        button.setFont(QFont('Consolas', 12, QFont.Bold))
        label.adjustSize()

        vbox = QVBoxLayout(self)
        vbox.addWidget(label)
        vbox.addWidget(button)
        self.setLayout(vbox)

        button.clicked.connect(self.start)

    def start(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())




