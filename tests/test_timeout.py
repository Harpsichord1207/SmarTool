import time
import unittest

from src import timeout, TimeoutException


class TestTimeout(unittest.TestCase):

    def test_timeout(self):

        @timeout
        def f1():
            time.sleep(10)

        with self.assertRaises(TimeoutException):
            f1()

        @timeout(seconds=20)
        def f2():
            time.sleep(10)
            return True

        self.assertTrue(f2())
