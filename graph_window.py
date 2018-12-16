import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout
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

        tabs = stl.get_tab_style({'Параметры': SetupTab(), 'График': GraphTab()})
        layout = stl.get_box_style(QVBoxLayout, tabs)

        self.setLayout(layout)


class SetupTab(QWidget):
    def __init__(self):
        super().__init__()
        self.stl = Style(self)
        self.initUi()

    def initUi(self):
        self.stl.get_background_style()
        check_box = [self.stl.get_label_style('Отображать:', 16),
                     self.stl.get_checkbox_style('Физический биоритм', 10, 'green'),
                     self.stl.get_checkbox_style('Эмоциональный биоритм', 10, 'red'),
                     self.stl.get_checkbox_style('Интеллектуальный биоритм', 10, 'blue'),
                     self.stl.get_checkbox_style('Среднее значение', 10, 'black'),
                     self.stl.get_button_style('Перейти к графику', 10)]
        name_label = self.stl.get_label_style('Введите ваше имя:', 10)
        name_line_edit = self.stl.get_line_edit_style(10)
        birth_date_label = self.stl.get_label_style('[*]Введите дату рождения: ', 10)
        birth_date_edit = self.stl.get_date_edit_style(10)
        forecast_date_label = self.stl.get_label_style('[*]Введите дату прогноза:', 10)
        forecast_date = self.stl.get_date_edit_style(10)

        gsetupbox_layout = self.stl.get_box_style(QGridLayout)
        r = 0
        for i in check_box:
            gsetupbox_layout.addWidget(i, r, 0)
            r += 1
        gsetupbox_layout.addWidget(name_label, 0, 1)
        gsetupbox_layout.addWidget(name_line_edit, 1, 1)
        gsetupbox_layout.addWidget(birth_date_label, 2, 1)
        gsetupbox_layout.addWidget(birth_date_edit, 3, 1)
        gsetupbox_layout.addWidget(forecast_date_label, 4, 1)
        gsetupbox_layout.addWidget(forecast_date, 5, 1)
        self.setLayout(gsetupbox_layout)


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
