from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPushButton, QCheckBox, QTabWidget, QLineEdit, QDateEdit, QFrame


class Style:
    def __init__(self, obj):
        self.obj = obj

    def get_background_style(self):
        self.obj.setStyleSheet('QWidget{background-color: #F5F5DC;}')

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

    def get_checkbox_style(self, text, font, color):
        check_box = QCheckBox(text, self.obj)
        check_box.setStyleSheet('QCheckBox{background-color: #F5F5DC; color: %s;}' % color)
        check_box.setFont(QFont('Consolas', font, QFont.Bold))
        check_box.adjustSize()
        return check_box

    def get_tab_style(self, kwargs):
        tabs = QTabWidget()
        for i in kwargs:
            tabs.addTab(kwargs[i], i)
        tabs.adjustSize()
        tabs.setStyleSheet('QTabWidget{background-color: #F5F5DD;}')
        return tabs

    def get_line_edit_style(self, font):
        line = QLineEdit(self.obj)
        line.setStyleSheet('QLineEdit{color: #000000;}')
        line.setFont(QFont('Consolas', font, QFont.Bold))
        return line

    def get_box_style(self, box, *widgets):
        layout = box(self.obj)
        for i in widgets:
            layout.addWidget(i)
        return layout

    def get_date_edit_style(self, font):
        datedit = QDateEdit(self.obj)
        datedit.setStyleSheet('QDateEdit{background-color: #F5F5DD; color: #000000;}')
        datedit.setFont(QFont('Consolas', font, QFont.Bold))
        return datedit

    def get_line_style(self, pos):
        line = QFrame()
        line.setFrameShape(pos)
        line.setFrameShadow(QFrame.Sunken)
        return line


