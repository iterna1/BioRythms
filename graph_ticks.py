import datetime
import math


class Ticks:
    def __init__(self, days):
        self.days = range(days)
        self.pi = math.pi
        self.phases = (23, 28, 33)

    def physical(self):
        result = []
        for day in self.days:
            result.append(math.sin((2 * self.pi * day) / self.phases[0]) * 100)
        return result

    def emotional(self):
        result = []
        for day in self.days:
            result.append(math.sin((2 * self.pi * day) / self.phases[1]) * 100)
        return result

    def intellectual(self):
        result = []
        for day in self.days:
            result.append(math.sin((2 * self.pi * day) / self.phases[2]) * 100)
        return result


class TimeDelta:
    def __init__(self, birth_date, current_date):
        self.birth_date = self.get_date(birth_date)
        self.current_date = self.get_date(current_date)
        self.delta = self.get_delta()

    def get_date(self, birth_date):
        return datetime.datetime(*list(birth_date)[::-1])

    def get_delta(self):
        return self.current_date - self.birth_date

    def seconds(self):
        return self.delta.seconds


def main():
    td = TimeDelta([12, 3, 2002], [16, 12, 2018])
    days = td.get_delta().days
    now = Ticks(days)
    print(now.physical())
    print(now.emotional())
    print(now.intellectual())


if __name__ == '__main__':
    main()
