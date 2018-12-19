import sys

import numpy as np
import pyqtgraph as pg
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QFrame
from style import Style
from time_works import TimeDelta, Ticks, get_current_date, human_format

pg.setConfigOption('background', '#F5F5DC')
pg.setConfigOption('foreground', '#A52A2A')


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
        self.st.check_box[5].clicked.connect(self.change_graph)
        tabs = self.stl.get_tab_style({'Меню': self.mt, 'Параметры': self.st, 'Результат': self.gt})
        layout = self.stl.get_box_style(QVBoxLayout, tabs)
        self.setLayout(layout)

    def change_graph(self):
        self.data = self.st.data
        self.gt.graphics_view.close()
        self.gt.initUI(self.data)


class MenuTab(QWidget):
    def __init__(self):
        super().__init__()
        self.stl = Style(self)
        self.initUI()

    def initUI(self):
        self.bio_theory = ['\n\tБиологические ритмы - периодически повторяющиеся изменения характера и интенсивности'
                           ' биологических процессов и явлений. Они свойственны живой материи на всех уровнях её'
                           ' организации - от молекулярных и субклеточных до биосферы. Являются фундаментальным'
                           ' процессом в живой природе. Человек, как биологический объект, в своей ежедневной жизни'
                           ' подвержен влиянию биологических ритмов в полной мере. Биоритмы воздействуют на все аспекты'
                           ' его жизнедеятельности: активность, выносливость, уровень иммунитета, мыслительные'
                           ' способности и прочие качества.\n\tСуществует теория, что человек со дня рождения находится'
                           ' в трёх биологических ритмах (биоритмах): физическом, эмоциональном и интеллектуальном.'
                           ' Это не зависит от каких либо других факторов.',

                           '\n\tФизический цикл равен 23 дням. Он определяет энергию человека, его силу, выносливость,'
                           ' координацию движения. Эмоциональный цикл равен 28 дням и обусловливает состояние'
                           ' нервной системы и настроение. Интеллектуальный цикл равен 33 дням и определяет'
                           ' творческую способность личности.\n\tЛюбой из циклов состоит из двух полупериодов,'
                           ' положительного и отрицательного.\n\tКритические дни, это те дни, когда кривая биоритма'
                           ' пересекает нулевую отметку. В этот момент влияние данного биоритма на человека имеет'
                           ' непредсказуемый характер. Если одну и ту же нулевую точку пересекают одновременно две или'
                           ' три синусоиды, то такие «двойные» или «тройные» критические дни особенно опасны.']

        self.prog_theory = ['\n\n\n\tBioRythms: Версия 1.1.0 | Автор: fortun.ik@yandex.ru\n\n\n\n\n\n\tРуководство'
                            ' пользователя представлено\n\tна следующей странице.',

                            '\tБиоритмы человека - реальная возможность повысить свои способности, возможности,'
                            ' эффективность своих действий, благодаря заранее определенной линии поведения. Попробуйте'
                            ' исследовать свои биоритмы, используя BioRythms!\n\tДля того, чтобы получить прогноз на'
                            ' какую-либо дату необходимо:\n— Указать дату рождения.\n— Указать дату прогноза.'
                            ' (Дату, на которую Вы планируете получить прогноз. Также является "ограничителем" графика)'
                            '.\n— Выбрать те биоритмы, значения которых хотите получить (см. Биоритмы).\n'
                            '— Нажать на кнопку "Задать" и перейти во вкладку с графиком (навигационное меню приложения'
                            ' находится вверху).\n'
                            '— По желанию можно нажать на полученный результат, чтобы программа проанализировала его']

        self.show_bt = False
        self.show_pt = False
        self.menu_txt = ['\n\tДобро пожаловать в BioRythms.\n\n'
                         '\tВ этом меню Вы можете получить\n'
                         '\tнеобходимую информацию о\n'
                         '\tбиоритмах или этой программе.']

        self.info1 = self.stl.get_button_style('Биоритмы', 30)
        self.info2 = self.stl.get_button_style('BioRythms', 30)
        self.page_num = self.stl.get_button_style('<->', 30, bgs_color='#483D8B', bgc_color='#483D8B')
        self.text = self.stl.get_plain_text_line(self.menu_txt[0], 30)
        lines = [self.stl.get_line_style(QFrame.HLine), self.stl.get_line_style(QFrame.HLine)]
        vbox = self.stl.get_box_style(QGridLayout)
        vbox.addWidget(lines[0], 0, 0, 1, 5)
        vbox.addWidget(self.text, 1, 0, 1, 5)
        vbox.addWidget(self.info1, 2, 0, 1, 2)
        vbox.addWidget(self.page_num, 2, 2, 1, 1)
        vbox.addWidget(self.info2, 2, 3, 1, 2)

        self.setLayout(vbox)
        self.info1.clicked.connect(self.show_page)
        self.info2.clicked.connect(self.show_page)
        self.page_num.clicked.connect(self.show_page)

    def show_page(self):
        sender = self.sender()
        menu = False
        if sender.text() == 'Биоритмы':
            info_list = self.bio_theory
        elif sender.text() == 'BioRythms':
            info_list = self.prog_theory
        else:
            info_list = self.menu_txt
            menu = True
        ln = len(info_list)
        try:
            if (self.show_bt and sender.text() == 'BioRythms')\
                    or (self.show_pt and sender.text() == 'Биоритмы')\
                    or menu:
                raise ValueError
            pn = int(self.page_num.text()[0])
            if pn == ln:
                raise ValueError
        except ValueError:
            pn = 0
        self.text.setPlainText(info_list[pn])
        if not menu:
            self.page_num.setText('%i/%i' % (pn + 1, ln))
            self.text.setFont(QFont('Arial', 16))
        else:
            self.page_num.setText('<->')
            self.text.setFont(QFont('Calibri', 30, QFont.Bold))
        if sender.text() == 'Биоритмы':
            self.show_pt, self.show_bt = False, True
        elif sender.text() == 'BioRythms':
            self.show_pt, self.show_bt = True, False
        else:
            self.show_pt, self.show_bt = False, False


class SetupTab(QWidget):
    def __init__(self):
        super().__init__()
        self.stl = Style(self)
        self.initUI()
        self.set_data()

    def initUI(self):
        self.check_box = [self.stl.get_button_style('[*]Отображать:', 30),
                          self.stl.get_checkbox_style(' Физический биоритм', 18, 'green'),
                          self.stl.get_checkbox_style(' Эмоциональный биоритм', 18, 'red'),
                          self.stl.get_checkbox_style(' Интеллектуальный биоритм', 18, 'blue'),
                          self.stl.get_checkbox_style(' Среднее значение', 18, 'black'),
                          self.stl.get_button_style('Задать', 18)]
        self.edit_box = [self.stl.get_button_style('Ваше имя:', 20),
                         self.stl.get_line_edit_style(16),
                         self.stl.get_button_style('[*]Дата рождения: ', 20),
                         self.stl.get_date_edit_style(20),
                         self.stl.get_button_style('[*]Дата прогноза:', 20),
                         self.stl.get_date_edit_style(20)]
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
        self.gbox_layout = self.stl.get_box_style(QGridLayout)
        self.initUI(data)

    def initUI(self, data):
        try:
            data['name']
        except TypeError:
            self.graphics_view = data
            self.show_graph = False
        else:
            self.graphics_view = pg.PlotWidget(self)
            self.define_vars(data)
            self.show_graph = True
            self.data = data
        self.statement_forecast_day, self.statement_today = self.configure_graph()
        self.gbox_layout.addWidget(self.graphics_view, 0, 0, 3, 9)
        k = 0
        for f, t in zip(self.statement_forecast_day, self.statement_today):
            self.gbox_layout.addWidget(f, 6, k)
            self.gbox_layout.addWidget(t, 7, k)
            k += 2

        self.statement_today[0].clicked.connect(self.info)
        self.statement_today[1].clicked.connect(self.info)
        self.statement_today[2].clicked.connect(self.info)
        self.statement_today[3].clicked.connect(self.info)
        self.statement_today[4].clicked.connect(self.info)
        self.statement_forecast_day[0].clicked.connect(self.info)
        self.statement_forecast_day[1].clicked.connect(self.info)
        self.statement_forecast_day[2].clicked.connect(self.info)
        self.statement_forecast_day[3].clicked.connect(self.info)
        self.statement_forecast_day[4].clicked.connect(self.info)

    def define_vars(self, data):
        self.user_name = data['name'].capitalize()
        self.draw_phys = data['phys']
        self.draw_emo = data['emo']
        self.draw_intel = data['intel']
        self.draw_avrg = data['avrg']
        self.birth_date = list(map(int, data['birth_date'].split('.')))
        self.forecast_date = list(map(int, data['forecast_date'].split('.')))

        self.forecast_date_delta = TimeDelta(self.birth_date, self.forecast_date).get_delta()
        self.ticks = Ticks(self.forecast_date_delta.days)
        self.current_date = get_current_date()
        self.current_date_delta = TimeDelta(self.birth_date, self.current_date).get_delta()
        self.todays_ticks = Ticks(self.current_date_delta.days)

        # значения в прогнозируемый день
        if self.ticks.discrets:
            self.f_phys = self.ticks.physical()[-1]
            self.f_emo = self.ticks.emotional()[-1]
            self.f_intel = self.ticks.intellectual()[-1]
            self.f_avrg = self.ticks.average()[-1]
        else:
            self.f_phys = 0
            self.f_emo = 0
            self.f_intel = 0
            self.f_avrg = 0
        # значения сегодня
        if self.todays_ticks.discrets:
            self.c_phys = self.todays_ticks.physical()[-1]
            self.c_emo = self.todays_ticks.emotional()[-1]
            self.c_intel = self.todays_ticks.intellectual()[-1]
            self.c_avrg = self.todays_ticks.average()[-1]
        else:
            self.c_phys = 0
            self.c_emo = 0
            self.c_intel = 0
            self.c_avrg = 0

    def configure_graph(self):
        g_c = '#8FBC8F'
        r_c = '#FA8072'
        be_c = '#B0E0E6'
        bl_c = '#A9A9A9'
        if self.draw_phys:
            g_c = '#006400'
        if self.draw_emo:
            r_c = '#8B0000'
        if self.draw_intel:
            be_c = '#483D8B'
        if self.draw_avrg:
            bl_c = 'black'
        statement_today = [self.stl.get_button_style(' %s ' % human_format(self.current_date), 14),
                           self.stl.get_button_style(' %f %s ' % (self.c_phys, '%'), 12,
                                                     bgc_color='#8FBC8F', bgs_color='#8FBC8F',
                                                     txt_color=g_c),
                           self.stl.get_button_style(' %f %s ' % (self.c_emo, '%'), 12,
                                                     bgc_color='#FA8072', bgs_color='#FA8072',
                                                     txt_color=r_c),
                           self.stl.get_button_style(' %f %s ' % (self.c_intel, '%'), 12,
                                                     bgc_color='#B0E0E6', bgs_color='#B0E0E6',
                                                     txt_color=be_c),
                           self.stl.get_button_style(' %f %s ' % (self.c_avrg, '%'), 12,
                                                     bgc_color='#A9A9A9', bgs_color='#A9A9A9',
                                                     txt_color=bl_c)]

        statement_forecast_day = [self.stl.get_button_style(' %s ' % human_format(self.forecast_date), 14),
                                  self.stl.get_button_style(' %f %s ' % (self.f_phys, '%'), 12,
                                                            bgc_color='#8FBC8F', bgs_color='#8FBC8F',
                                                            txt_color=g_c),
                                  self.stl.get_button_style(' %f %s ' % (self.f_emo, '%'), 12,
                                                            bgc_color='#FA8072', bgs_color='#FA8072',
                                                            txt_color=r_c),
                                  self.stl.get_button_style(' %f %s ' % (self.f_intel, '%'), 12,
                                                            bgc_color='#B0E0E6', bgs_color='#B0E0E6',
                                                            txt_color=be_c),
                                  self.stl.get_button_style(' %f %s ' % (self.f_avrg, '%'), 12,
                                                            bgc_color='#A9A9A9', bgs_color='#A9A9A9',
                                                            txt_color=bl_c)]

        try:
            self.graphics_view.plot(list(range(-10, 0)) + list(self.ticks.discrets) +
                                    list(range(len(self.ticks.discrets), len(self.ticks.discrets) + 10)),
                                    np.zeros(shape=len(self.ticks.discrets) + 20), pen=(165, 42, 42))
        except Exception as e:
            pass
        else:
            if self.draw_phys:
                self.graphics_view.plot(self.ticks.discrets, self.ticks.physical(), pen='g')
            if self.draw_emo:
                self.graphics_view.plot(self.ticks.discrets, self.ticks.emotional(), pen='r')
            if self.draw_intel:
                self.graphics_view.plot(self.ticks.discrets, self.ticks.intellectual(), pen='b')
            if self.draw_avrg:
                self.graphics_view.plot(self.ticks.discrets, self.ticks.average(), pen='k')
        return statement_forecast_day, statement_today

    def info(self):
        sender = self.sender()
        if not self.show_graph:
            self.initUI(self.data)
            self.show_graph = True
        else:
            self.graphics_view.close()
            self.show_graph = False

            text = self.get_sender_info(sender)  # получаем информацию по конкретной кнопке
            self.initUI(text)

    def get_sender_info(self, sender):
        if self.user_name != '':
            name = '%s, ' % self.user_name
        else:
            name = ''
        # Если сегодняшняя дата
        if sender == self.statement_today[0]:
            txt = self.stl.get_plain_text_line(('%sэто сегодняшняя дата. \n\n\n\n\n\n[Нажми на кнопку ещё раз, чтобы'
                                                ' увидеть график]' % name).capitalize(), 24)
            txt.setFont(QFont('Arial', 24))
            return txt
        # Если дата прогноза
        elif sender == self.statement_forecast_day[0]:
            txt = self.stl.get_plain_text_line(('%sэто та дата, которую ты выбрал в качестве "даты прогноза" в'
                                                ' предыдущем меню.\n\n\n\n\n[Нажми на кнопку ещё раз, чтобы увидеть'
                                                ' график]'
                                                % name).capitalize(), 24)
            txt.setFont(QFont('Arial', 24))
            return txt
        # Если это не кнопки с датами
        else:
            # Определяем состояние данного биоритма
            num = float(sender.text()[1:-2])
            positive, negative, neutral = False, False, False
            if num > 0:
                positive = True
            elif num < 0:
                negative = True
            else:
                neutral = True
            # Определяем информацию по биоритму
            if sender in (self.statement_today[1], self.statement_forecast_day[1]):  # Физический
                if positive:
                    txt = self.stl.get_plain_text_line('Положительная фаза физического биоритма — благоприятный период'
                                                       ' для занятий, связанных с физической нагрузкой.  Максимальная'
                                                       ' энергия, сила, выносливость, наивысшая устойчивость к'
                                                       ' воздействию экстремальных факторов. Вы бодры, энергичны и ваша'
                                                       ' физическая активность высока.\n\n\n[Нажми на кнопку ещё раз,'
                                                       ' чтобы увидеть график]', 22)
                elif negative:
                    txt = self.stl.get_plain_text_line('В отрицательной фазе физического биоритма Вы чувствуете упадок'
                                                       ' физических сил. Работа, какой бы легкой она ни была, утомляет.'
                                                       ' Пониженный физический тонус, быстрая утомляемость, некоторое'
                                                       ' снижение сопротивляемости организма к заболеваниям. Ваше'
                                                       ' физическое состояние оставляет желать лучшего. После обеда вас'
                                                       ' одолевает сонливость.\n[Нажми на кнопку ещё раз, чтобы увидеть'
                                                       ' график]', 22)
                elif neutral:
                    txt = self.stl.get_plain_text_line('Критические дни физического биоритма обычно проявляются в'
                                                       ' резкой перемене самочувствия. Нестабильность физического'
                                                       ' состояния. Существует вероятность травм, аварий, обострений'
                                                       ' хронических заболеваний, головной боли. Проявляя физическую'
                                                       ' активность мы не обращаем внимания на появившиеся болевые'
                                                       ' ощущения и дискомфорт. Между тем, это — сигналы о'
                                                       ' неблагополучии, чреватом риском получения серьезной травмы.\n'
                                                       '[Нажми на кнопку ещё раз, чтобы увидеть график]',
                                                       22)

                txt.setFont(QFont('Arial', 22))
                return txt
            elif sender in (self.statement_today[2], self.statement_forecast_day[2]):  # Эмоциональный
                if positive:
                    txt = self.stl.get_plain_text_line('Положительную фазу эмоционального биоритма можно'
                                                       ' охарактеризовать такими словами как, энтузиазм и отличное'
                                                       ' настроение. Вам удается без особых усилий регулировать'
                                                       ' эмоциональное состояние и блокировать попытки внешнего'
                                                       ' психологического давления. Вы открыты для общения и способны'
                                                       ' адекватно воспринимать собеседников.\n\n[Нажми на кнопку ещё'
                                                       ' раз, чтобы увидеть график]', 22)
                elif negative:
                    txt = self.stl.get_plain_text_line('В отрицательной фазе эмоционального биоритма вы будете'
                                                       ' становиться менее общительным, но более унылым,'
                                                       ' раздражительным и чувствительным к вещам, которые обычно вас'
                                                       ' особо не тревожили. Повышенная напряженность, часто плохое'
                                                       ' настроение. Негативные эмоции берут верх над разумом. Это'
                                                       ' период, когда человек особенно склонен оказываться в неловких'
                                                       ' ситуациях.\n[Нажми на кнопку ещё раз, чтобы увидеть график]', 22)
                elif neutral:
                    txt = self.stl.get_plain_text_line('В критические дни эмоционального биоритма вы склонны к'
                                                       ' неуместным шуткам и резким замечаниям. Эмоциональная'
                                                       ' неустойчивость, склонность к снижению реакций, угнетенному'
                                                       ' состоянию, ссорам. Что-то не так и вы впадаете в бешенство,'
                                                       ' когда биоритм меняется на отрицательную фазу. Ваши шутки'
                                                       ' вызывают обиду, малейшие замечания в вашу сторону вызывают'
                                                       ' встречную агрессию и т.д.\n\n[Нажми на кнопку ещё раз, чтобы'
                                                       ' увидеть график]', 22)
                txt.setFont(QFont('Arial', 22))
                return txt
            elif sender in (self.statement_today[3], self.statement_forecast_day[3]):  # Интеллектуальный
                if positive:
                    txt = self.stl.get_plain_text_line('В положительной фазе интеллектуального биоритма вами руководит'
                                                       ' здравый смысл и у вас один шаг до гениальности. Вы чувствуете'
                                                       ' себя в прекрасной творческой форме, вам хочется поупражнять'
                                                       ' свой, как вы считаете, недостаточно загруженный мозг.'
                                                       ' Интеллектуальное состояние достигает наивысшего уровня,'
                                                       ' простые задачи решаются легко и без раздумий.\n'
                                                       '[Нажми на кнопку ещё раз, чтобы увидеть график]', 22)
                elif negative:
                    txt = self.stl.get_plain_text_line('В негативной фазе интеллектуального биоритма умственная'
                                                       ' деятельность замедляется. Процесс мышления вялый, прерывистый.'
                                                       ' Восприятие тускнеет, заметно отсутствие концентрации, а'
                                                       ' решение даже простых задач требует серьезных усилий.\n\n\n\n'
                                                       '[Нажми на кнопку ещё раз, чтобы увидеть график]', 22)
                elif neutral:
                    txt = self.stl.get_plain_text_line('В критические дни интеллектуального биоритма мыслительные'
                                                       ' способности человека могут сыграть с ним злую шутку.'
                                                       ' Склонность к снижению внимания, ошибочным заключениям,'
                                                       ' ухудшению запоминания. В эти дни лучше воздержаться от'
                                                       ' принятия ответственных решений.\n\n\n[Нажми на кнопку ещё раз,'
                                                       ' чтобы увидеть график]', 22)
                txt.setFont(QFont('Arial', 22))
                return txt
            elif sender in (self.statement_today[4], self.statement_forecast_day[4]):  # Среднее значение
                txt = self.stl.get_plain_text_line('Среднее значение трёх биоритмов: физического, эмоционального и'
                                                   ' интелектуального\n\n\n\n\n\n\n[Нажми на кнопку ещё раз, чтобы'
                                                   ' увидеть график]', 22)
                txt.setFont(QFont('Arial', 22))
                return txt


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
