import sys

from PyQt5.QtWidgets import QApplication, QWidget
from style import Style


class GraphWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.stl = Style(self)

    def initUI(self):
        self.stl.get_background_style()
        check_box = [self.stl.get_checkbox_style('Физический', 8),
                     self.stl.get_checkbox_style('Эмоциональный', 8),
                     self.stl.get_checkbox_style('Интеллектуальный', 8)]






if __name__ == 'main_window':
    print(globals())
    app = QApplication(sys.argv)
    gw = GraphWindow()
    gw.show()
    sys.exit(app.exec())
