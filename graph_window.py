import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout
from graph_ticks import TimeDelta, Ticks
from pyqtgraph import PlotWidget
from style import Style


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stl = Style(self)
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('BioRythms')
        self.setFixedSize(810, 500)
        self.table_widget = TableWidget(self)
        self.setCentralWidget(self.table_widget)


class TableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.stl = Style(self)
        self.stl.get_background_style()
        self.initUI()

    def initUI(self):
        self.mt = MenuTab()
        self.st = SetupTab()
        self.data = self.st.data
        self.gt = GraphTab(self.data)
        tabs = self.stl.get_tab_style({'Меню': self.mt, 'Параметры': self.st, 'Результат': self.gt})
        layout = self.stl.get_box_style(QVBoxLayout, tabs)
        self.setLayout(layout)
        self.st.check_box[5].clicked.connect(self.change_graph)


    def change_graph(self):
        self.data = self.st.data
        self.gt.draw(self.data)


class MenuTab(QWidget):
    def __init__(self):
        super().__init__()
        self.stl = Style(self)
        self.initUI()

    def initUI(self):
        label = self.stl.get_label_style('Добро пожаловать в BioRythms', 40)
        label.setAlignment(Qt.AlignCenter)
        button = self.stl.get_button_style('О программе', 30)

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
        self.set_data()

    def initUi(self):
        self.check_box = [self.stl.get_label_style('Отображать:', 20),
                          self.stl.get_checkbox_style('Физический биоритм', 16, 'green'),
                          self.stl.get_checkbox_style('Эмоциональный биоритм', 16, 'red'),
                          self.stl.get_checkbox_style('Интеллектуальный биоритм', 16, 'blue'),
                          self.stl.get_checkbox_style('Среднее значение', 16, 'black'),
                          self.stl.get_button_style('Построить', 16)]
        self.edit_box = [self.stl.get_label_style('Введите ваше имя:', 16),
                         self.stl.get_line_edit_style(16),
                         self.stl.get_label_style('[*]Введите дату рождения: ', 16),
                         self.stl.get_date_edit_style(16),
                         self.stl.get_label_style('[*]Введите дату прогноза:', 16),
                         self.stl.get_date_edit_style(16)]

        gsetupbox_layout = self.stl.get_box_style(QGridLayout)
        for i in range(len(self.check_box)):
            gsetupbox_layout.addWidget(self.check_box[i], i, 0)
            gsetupbox_layout.addWidget(self.edit_box[i], i, 1)

        self.setLayout(gsetupbox_layout)
        self.check_box[5].clicked.connect(self.set_data)

    def set_data(self):
        self.data = {'name': self.edit_box[1].text(),
                     'birth_date': self.edit_box[3].text(),
                     'forecast_date': self.edit_box[5].text(),
                     'phys': self.check_box[1].isChecked(),
                     'emo': self.check_box[2].isChecked(),
                     'intel': self.check_box[3].isChecked(),
                     'average': self.check_box[4].isChecked()}


class GraphTab(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.define_vars(data)
        self.stl = Style(self)
        self.initUI()

    def initUI(self):
        statement = [self.stl.get_label_style('Ваше текущее физическое состояние%s: %f'
                                              % (self.user_name, self.phys), 14),
                     self.stl.get_label_style('Ваше текущее эмоциональное состояние%s: %f'
                                              % (self.user_name, self.emo), 14),
                     self.stl.get_label_style('Ваше текущее интеллектуальное состояние%s: %f'
                                              % (self.user_name, self.intel), 14)]


        self.gbox_layout = self.stl.get_box_style(QGridLayout)
        self.draw(self.data)
        for i in range(len(statement)):
            self.gbox_layout.addWidget(statement[i], i + 1, 0)

    def define_vars(self, data):
        self.phys = 50
        self.emo = 25
        self.intel = 0
        if data['name'] != '':
            self.user_name = ', ' + data['name']
        else:
            self.user_name = data['name']
        birth_date = list(map(int, data['birth_date'].split('.')))
        forecast_date = list(map(int, data['forecast_date'].split('.')))
        self.td = TimeDelta(birth_date, forecast_date)
        self.delta = self.td.get_delta()
        self.ticks = Ticks(self.delta.days)

    def draw(self, data):
        self.define_vars(data)
        graphicsView = PlotWidget(self)
        graphicsView.plot(range(self.delta.days), self.ticks.physical(), pen='g')
        graphicsView.plot(range(self.delta.days), self.ticks.emotional(), pen='r')
        graphicsView.plot(range(self.delta.days), self.ticks.intellectual(), pen='b')
        self.gbox_layout.addWidget(graphicsView, 0, 0)


class Communicate(Exception):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Communicate()
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
