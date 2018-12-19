import datetime
import math


def get_current_date():
    return list(map(int, str(datetime.datetime.now()).split()[0].split('-')))[::-1]


def human_format(p_lst):
    r_str = ''
    for i in p_lst:
        if i < 10:
            r_str += '0%i.' % i
        else:
            r_str += '%i.' % i
    return r_str.rstrip('.')


class Ticks:
    def __init__(self, days):
        self.discrets = range(days + 1)
        self.pi = math.pi
        self.phases = (23, 28, 33)

    def physical(self):
        result = []
        for disc in self.discrets:
            result.append((math.sin((2 * self.pi * disc) / self.phases[0]) * 100))
        return result

    def emotional(self):
        result = []
        for disc in self.discrets:
            result.append((math.sin((2 * self.pi * disc) / self.phases[1]) * 100))
        return result

    def intellectual(self):
        result = []
        for disc in self.discrets:
            result.append((math.sin((2 * self.pi * disc) / self.phases[2]) * 100))
        return result

    def average(self):
        result = []
        phys = self.physical()
        emo = self.emotional()
        intel = self.intellectual()
        for i in self.discrets:
            result.append((phys[i] + emo[i] + intel[i]) / 3)
        return result


class TimeDelta:
    def __init__(self, birth_date, current_date):
        self.birth_date = self.get_date(birth_date)
        self.current_date = self.get_date(current_date)
        self.delta = self.get_delta()

    def get_date(self, date):
        return datetime.datetime(*list(date)[::-1])

    def get_delta(self):
        return self.current_date - self.birth_date

    def seconds(self):
        return self.delta.seconds


def main():
    td = TimeDelta([1, 1, 1000], [11, 11, 1111])
    days = td.get_delta().days
    now = Ticks(days)
    print(now.physical()[-1])
    print(now.emotional()[-1])
    print(now.intellectual()[-1])


if __name__ == '__main__':
    main()
