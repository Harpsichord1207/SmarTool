import datetime


class DTUtil:

    @classmethod
    def add_month(cls, date: datetime.datetime = None, months: int = 1):
        if date is None:
            date = datetime.datetime.today()
        target_month = date.month + int(months)
        return date.replace(year=date.year+target_month // 12, month=target_month % 12)

    @classmethod
    def first_day_of_month(cls, date: datetime.datetime = None):
        if date is None:
            date = datetime.datetime.today()
        return date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    @classmethod
    def last_day_of_month(cls, date: datetime.datetime = None):
        if date is None:
            date = datetime.datetime.today()
        return cls.first_day_of_month(cls.add_month(date)) - datetime.timedelta(days=1)
