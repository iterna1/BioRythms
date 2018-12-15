import datetime


class BadDateFormat(Exception):
    pass


class TimeDelta:
    def __init__(self, birth_date):
        self.birth_date = self.birth_date(birth_date)
        self.current_date = self.current_date()
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

    def current_date(self):
        return datetime.datetime.now()

    def get_delta(self):
        return self.current_date - self.birth_date

    def seconds(self):
        return self.delta.seconds


def main():
    birth_d = input('Введите дату (D/Y/M): ')
    td = TimeDelta(birth_d)
    print(td.get_delta().days)


if __name__ == '__main__':
    main()
