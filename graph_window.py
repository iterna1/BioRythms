import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QFrame
from graph_ticks import TimeDelta, Ticks, get_current_date
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
        self.initUI()
        self.set_data()

    def initUI(self):
        self.check_box = [self.stl.get_label_style('Отображать:', 30),
                          self.stl.get_checkbox_style('Физический биоритм', 18, 'green'),
                          self.stl.get_checkbox_style('Эмоциональный биоритм', 18, 'red'),
                          self.stl.get_checkbox_style('Интеллектуальный биоритм', 18, 'blue'),
                          self.stl.get_checkbox_style('Среднее значение', 18, 'black'),
                          self.stl.get_button_style('Задать', 18)]
        self.edit_box = [self.stl.get_label_style('Введите ваше имя:', 18),
                         self.stl.get_line_edit_style(18),
                         self.stl.get_label_style('[*]Введите дату рождения: ', 18),
                         self.stl.get_date_edit_style(18),
                         self.stl.get_label_style('[*]Введите дату прогноза:', 18),
                         self.stl.get_date_edit_style(18)]
        lines = [self.stl.get_line_style(QFrame.HLine),
                 self.stl.get_line_style(QFrame.VLine),
                 self.stl.get_line_style(QFrame.HLine)]

        gsetupbox_layout = self.stl.get_box_style(QGridLayout)
        gsetupbox_layout.addWidget(lines[0], 0, 0, 2, 8)
        gsetupbox_layout.addWidget(lines[1], 1, 2, 7, 1)
        for i in range(len(self.check_box)):
            try:
                self.check_box[i].setAlignment(Qt.AlignHCenter)
            except AttributeError:
                pass
            finally:
                gsetupbox_layout.addWidget(self.check_box[i], i + 1, 0)
                gsetupbox_layout.addWidget(self.edit_box[i], i + 1, 5)
        gsetupbox_layout.addWidget(lines[2], 7, 0, 2, 8)


        self.setLayout(gsetupbox_layout)
        self.check_box[5].clicked.connect(self.set_data)

    def set_data(self):
        self.data = {'name': self.edit_box[1].text(),
                     'birth_date': self.edit_box[3].text(),
                     'forecast_date': self.edit_box[5].text(),
                     'phys': self.check_box[1].isChecked(),
                     'emo': self.check_box[2].isChecked(),
                     'intel': self.check_box[3].isChecked(),
                     'avrg': self.check_box[4].isChecked()}


class GraphTab(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.define_vars(data)
        self.stl = Style(self)
        self.initUI()

    def initUI(self):
        self.gbox_layout = self.stl.get_box_style(QGridLayout)
        self.draw(self.data)

    def define_vars(self, data):
        if data['name'] != '':
            self.user_name = data['name'].capitalize() + ', твой'
        else:
            self.user_name = 'Ваш'
        self.draw_phys = data['phys']
        self.draw_emo = data['emo']
        self.draw_intel = data['intel']
        self.draw_avrg = data['avrg']
        birth_date = list(map(int, data['birth_date'].split('.')))
        forecast_date = list(map(int, data['forecast_date'].split('.')))

        self.forecast_date_delta = TimeDelta(birth_date, forecast_date).get_delta()
        self.ticks = Ticks(self.forecast_date_delta.days)
        self.current_date_delta = TimeDelta(birth_date, get_current_date()).get_delta()
        self.todays_ticks = Ticks(self.current_date_delta.days)

        if self.ticks.days:
            # значения в прогнозируемый день
            self.f_phys = self.ticks.physical()[-1]
            self.f_emo = self.ticks.emotional()[-1]
            self.f_intel = self.ticks.intellectual()[-1]
            self.f_avrg = self.ticks.average()[-1]
            # значения сегодня
            self.c_phys = self.todays_ticks.physical()[-1]
            self.c_emo = self.todays_ticks.emotional()[-1]
            self.c_intel = self.todays_ticks.intellectual()[-1]
            self.c_avrg = self.todays_ticks.average()[-1]
        else:
            # значения в прогнозируемый день
            self.f_phys = 0
            self.f_emo = 0
            self.f_intel = 0
            self.f_avrg = 0
            # значения сегодня
            self.c_phys = 0
            self.c_emo = 0
            self.c_intel = 0
            self.c_avrg = 0

    def draw(self, data):
        self.define_vars(data)
        self.statement_forecast_day, self.statement_today, self.graphicsView = self.configure_graph()
        if not self.graphicsView:
            self.graphicsView = self.stl.get_label_style((self.user_name.rstrip('твой').rstrip('Ваш') +
                                                    'укажи параметры (в предыдущей вкладке)')
                                                    .capitalize(), 24)
            self.graphicsView.setAlignment(Qt.AlignCenter)
        self.gbox_layout.addWidget(self.graphicsView, 0, 0, 4, 10)
        k = 0
        for f, t in zip(self.statement_forecast_day, self.statement_today):
            try:
                f.setAlignment(Qt.AlignCenter)
                t.setAlignment(Qt.AlignCenter)
            except AttributeError:
                pass
            finally:
                self.gbox_layout.addWidget(f, 5, k)
                self.gbox_layout.addWidget(t, 6, k)
            k += 1

    def configure_graph(self):
        statement_today = []
        statement_forecast_day = []
        graphicsView = []
        if self.draw_phys:
            statement_today.extend([self.stl.get_line_style(QFrame.VLine)] +
                                   [self.stl.get_label_style('%f %s' % (self.c_phys, '%'), 12, color='green')])
            statement_forecast_day.extend([self.stl.get_line_style(QFrame.VLine)] +
                                          [self.stl.get_label_style('%f %s' % (self.f_phys, '%'), 12, color='green')])
        if self.draw_emo:
            statement_today.extend([self.stl.get_line_style(QFrame.VLine)] +
                                   [self.stl.get_label_style('%f %s' % (self.c_emo, '%'), 12, color='red')], )
            statement_forecast_day.extend([self.stl.get_line_style(QFrame.VLine)] +
                                          [self.stl.get_label_style('%f %s' % (self.f_emo, '%'), 12, color='red')])
        if self.draw_intel:
            statement_today.extend([self.stl.get_line_style(QFrame.VLine)] +
                                   [self.stl.get_label_style('%f %s' % (self.c_intel, '%'), 12, color='blue')])
            statement_forecast_day.extend([self.stl.get_line_style(QFrame.VLine)] +
                                          [self.stl.get_label_style('%f %s' % (self.f_intel, '%'), 12, color='blue')])
        if self.draw_avrg:
            statement_today.extend([self.stl.get_line_style(QFrame.VLine)] +
                                   [self.stl.get_label_style('%f %s' % (self.c_avrg, '%'), 12, color='black')])
            statement_forecast_day.extend([self.stl.get_line_style(QFrame.VLine)] +
                                   [self.stl.get_label_style('%f %s' % (self.f_avrg, '%'), 12, color='black')])

        if len(statement_today) > 4:
            graphicsView = PlotWidget(self)
            if self.draw_phys:
                graphicsView.plot(range(self.forecast_date_delta.days), self.ticks.physical(), pen='g')
            if self.draw_emo:
                graphicsView.plot(range(self.forecast_date_delta.days), self.ticks.emotional(), pen='r')
            if self.draw_intel:
                graphicsView.plot(range(self.forecast_date_delta.days), self.ticks.intellectual(), pen='b')
            if self.draw_avrg:
                graphicsView.plot(range(self.forecast_date_delta.days), self.ticks.average(), pen='w')
            statement_today = [self.stl.get_label_style('%s прогноз на сегодня'
                                                        % self.user_name, 12)] + statement_today
            statement_forecast_day = [self.stl.get_label_style('%s прогноз на указанную дату'
                                                               % self.user_name, 12)] + statement_forecast_day
            statement_today.append(self.stl.get_line_style(QFrame.VLine))
            statement_forecast_day.append(self.stl.get_line_style(QFrame.VLine))
        return statement_forecast_day, statement_today, graphicsView


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
