import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from style import Style


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stl = Style(self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(259, 160)
        self.stl.get_background_style()

        label = self.stl.get_label_style('Добро пожаловать в BioRythms', 13)
        button = self.stl.get_button_style('Старт', 12)

        vbox = QVBoxLayout(self)
        vbox.addWidget(label)
        vbox.addWidget(button)
        self.setLayout(vbox)

        button.clicked.connect(self.start)

    def start(self):
        pass


def start():
    pass


def main():
    app = QApplication(sys.argv)
    mw = MenuWindow()
    mw.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
