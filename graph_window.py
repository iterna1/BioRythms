import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout
from style import Style


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stl = Style(self)
        self.initUI()

    def initUI(self):
        self.stl.get_background_style()
        table_widget = TableWidget(self)
        self.setCentralWidget(table_widget)


class TableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        stl = Style(self)

        tabs = stl.get_tab_style({'Меню':MenuTab(), 'Параметры': SetupTab(), 'График': GraphTab()})
        layout = stl.get_box_style(QVBoxLayout, tabs)

        self.setLayout(layout)


class MenuTab(QWidget):
    def __init__(self):
        super().__init__()
        self.stl = Style(self)
        self.initUI()

    def initUI(self):
        self.stl.get_background_style()

        label = self.stl.get_label_style('Добро пожаловать в BioRythms', 18)
        label.setAlignment(Qt.AlignCenter)
        button = self.stl.get_button_style('О программе', 12)

        vbox = QVBoxLayout(self)
        vbox.addWidget(label)
        vbox.addWidget(button)
        self.setLayout(vbox)

        button.clicked.connect(self.start)

    def start(self):
        pass


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
                     self.stl.get_button_style('Построить', 11)]
        edit_box = [self.stl.get_label_style('Введите ваше имя:', 10),
                    self.stl.get_line_edit_style(10),
                    self.stl.get_label_style('[*]Введите дату рождения: ', 10),
                    self.stl.get_date_edit_style(10),
                    self.stl.get_label_style('[*]Введите дату прогноза:', 10),
                    self.stl.get_date_edit_style(10)]

        gsetupbox_layout = self.stl.get_box_style(QGridLayout)
        for i in range(len(check_box)):
            gsetupbox_layout.addWidget(check_box[i], i, 0)
            gsetupbox_layout.addWidget(edit_box[i], i, 1)

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
    gw = MainWindow()
    gw.show()
    sys.exit(app.exec())

if __name__ == 'main_window':
    app = QApplication(sys.argv)
    gw = MainWindow()
    gw.show()
    sys.exit(app.exec())
