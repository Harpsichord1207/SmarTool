import datetime
import unittest

from src import DTUtil


class TestDTUtil(unittest.TestCase):

    fmt1 = "%Y-%m-%d"

    def test_add_month(self):
        d = datetime.datetime.strptime("2022-04-01", self.fmt1)
        self.assertEqual("2022-05-01", DTUtil.add_month(d).strftime(self.fmt1))
        self.assertEqual("2023-04-01", DTUtil.add_month(d, months=12).strftime(self.fmt1))
        self.assertEqual("2023-05-01", DTUtil.add_month(d, months=13).strftime(self.fmt1))

        d = datetime.datetime.strptime("2020-02-29", self.fmt1)
        self.assertEqual("2022-03-01", DTUtil.add_month(d, months=24).strftime(self.fmt1))

    def test_first_day_of_month(self):
        d = datetime.datetime.strptime("2022-04-03", self.fmt1)
        self.assertEqual("2022-04-01", DTUtil.first_day_of_month(d).strftime(self.fmt1))

    def test_last_day_of_month(self):
        d = datetime.datetime.strptime("2022-04-01", self.fmt1)
        self.assertEqual(DTUtil.last_day_of_month(d).strftime(self.fmt1), "2022-04-30")
        self.assertIn(DTUtil.last_day_of_month().strftime(self.fmt1)[-2:], ['28', '29', '30', '31'])
