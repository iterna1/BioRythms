import datetime
import math


class BadDateFormat(Exception):
    pass


class Ticks:
    def __init__(self, days):
        self.days = days
        self.pi = math.pi
        self.phases = (23, 28, 33)

    def physical(self):
        return math.sin((2 * self.pi * self.days) / self.phases[0]) * 100

    def emotional(self):
        return math.sin((2 * self.pi * self.days) / self.phases[1]) * 100

    def intellectual(self):
        return math.sin((2 * self.pi * self.days) / self.phases[2]) * 100


class TimeDelta:
    def __init__(self, birth_date, current_date):
        self.birth_date = self.birth_date(birth_date)
        self.current_date = self.current_date(current_date)
        self.delta = self.get_delta()

    def birth_date(self, birth_date):
        try:
            if birth_date.count('/') != 2:
                raise BadDateFormat

            birth_date = birth_date.split('/')

            if not ''.join(birth_date).isdigit():
                raise BadDateFormat
            birth_date = map(int, birth_date)

        except BadDateFormat:
            raise BadDateFormat('Введите дату в формате ДД/ММ/ГГГГ')
        else:
            return datetime.datetime(*list(birth_date)[::-1])

    def current_date(self, current_date):
        try:
            if current_date.count('/') != 2:
                raise BadDateFormat
            current_date = current_date.split('/')

            if not ''.join(current_date).isdigit():
                raise BadDateFormat
            current_date = map(int, current_date)

        except BadDateFormat:
            raise BadDateFormat('Введите дату в формате ДД/ММ/ГГГГ')
        else:
            return datetime.datetime(*list(current_date)[::-1])

    def get_delta(self):
        return self.current_date - self.birth_date

    def seconds(self):
        return self.delta.seconds


def main():
    birth_d = input('Введите дату рождения (D/Y/M): ')
    current_d = input('Введите дату прогноза (D/Y/M): ')
    td = TimeDelta(birth_d, current_d)
    days = td.get_delta().days
    now = Ticks(days)
    print(now.physical())
    print(now.emotional())
    print(now.intellectual())


if __name__ == '__main__':
    main()
