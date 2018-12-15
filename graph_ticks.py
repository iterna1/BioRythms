import calendar
import datetime


def main():
    birth_d = list(map(int, input('Введите дату (D/Y/M): ').split('/')))
    td = TimeDelta(birth_d)
    t = td.delta.days
    print(t)


class TimeDelta:
    def __init__(self, birth_date):
        self.birth_date = datetime.datetime(*birth_date[::-1])
        self.current_date = datetime.datetime.now()
        self.delta = self.current_date - self.birth_date

    def seconds(self):
        return self.delta.seconds

    def years(self):
        days = 0
        year = self.birth_date
        dy = 365
        count = [0, 0]
        if calendar.isleap(year.year):
            dy = 366
            count[1] += 1
        while days + dy < self.delta.days:
            days += dy
            bb = datetime.timedelta(days=dy)
            year = year + bb
            if calendar.isleap(year.year):
                dy = 366
                count[1] += 1
            else:
                dy = 365
            count[0] += 1
        return count

    def delta_birthday_today(self):
        return abs(self.birth_date.day - self.current_date.day)


if __name__ == '__main__':
    main()
