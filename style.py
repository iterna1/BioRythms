from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QLabel, QPushButton


class Style():
    def __init__(self, obj):
        self.obj = obj

    def get_background_style(self):
        self.obj.setStyleSheet('QWidget{background-color: #F5F5DC;}')
        self.obj.setWindowIcon(QIcon('icon.png'))
        self.obj.setWindowTitle('BioRythms')

    def get_button_style(self, text, font):
        button = QPushButton(text, self.obj)
        button.setStyleSheet('QPushButton{background-color: #8B0000; color: #F5F5DD}')
        button.setFont(QFont('Consolas', font, QFont.Bold))
        button.adjustSize()
        return button

    def get_label_style(self, text, font):
        label = QLabel(text, self.obj)
        label.setStyleSheet('QLabel{color: #8B0000;}')
        label.setFont(QFont('Calibri', font, QFont.Bold))
        label.adjustSize()
        return label