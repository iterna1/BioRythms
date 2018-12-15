import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from style import Style


class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stl = Style(self)
        self.initUI()

    def initUI(self):
        table_widget = TableWidget(self)
        self.setCentralWidget(table_widget)


class TableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        stl = Style(self)

        layout = QVBoxLayout(self)
        tabs = stl.get_tab_style({'Параметры': SetupTab(), 'График': GraphTab()})

        layout.addWidget(tabs)
        self.setLayout(layout)


class SetupTab(QWidget):
    def __init__(self):
        super().__init__()
        self.stl = Style(self)
        self.initUi()

    def initUi(self):
        self.stl.get_background_style()
        check_box = [self.stl.get_label_style('Отображать:', 16),
                     self.stl.get_checkbox_style('Физический биоритм', 12, 'green'),
                     self.stl.get_checkbox_style('Эмоциональный биоритм', 12, 'red'),
                     self.stl.get_checkbox_style('Интеллектуальный биоритм', 12, 'blue'),
                     self.stl.get_checkbox_style('Среднее значение', 12, 'black')]
        vbox = QVBoxLayout(self)
        [vbox.addWidget(cb) for cb in check_box]


class GraphTab(QWidget):
    def __init__(self):
        super().__init__()
        self.stl = Style(self)
        self.initUi()

    def initUi(self):
        self.stl.get_background_style()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gw = GraphWindow()
    gw.show()
    sys.exit(app.exec())

if __name__ == 'main_window':
    app = QApplication(sys.argv)
    gw = GraphWindow()
    gw.show()
    sys.exit(app.exec())
