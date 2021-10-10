import random
import unittest

from src import retry


class TestRetry(unittest.TestCase):

    def test_retry_with_no_parameter(self):

        @retry
        def add(a, b):
            1 / random.choice([0, 1, 1])
            return a + b

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add.__name__, 'add')

    def test_retry_with_parameters(self):

        @retry(times=100, delay=0.1)
        def add(a, b):
            1 / random.choice([0, 0, 0, 0, 0, 0, 1])
            return a + b

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add.__name__, 'add')

    def test_retry_with_catch_error(self):

        @retry(times=100, delay=0.1, catch_error=ZeroDivisionError)
        def add(a, b):
            1 / random.choice([0, 0, 0, 0, 0, 0, 1])
            return a + b

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add.__name__, 'add')

        @retry(times=100, delay=0.1, catch_error=ValueError)
        def add(a, b):
            1 / random.choice([0, 0, 0, 0, 0, 0, 1])
            return a + b

        with self.assertRaises(ZeroDivisionError):
            add(1, 2)

    def test_retry_with_ignore_error(self):

        @retry(times=100, delay=0.1, ignore_error=ValueError)
        def add(a, b):
            1 / random.choice([0, 0, 0, 0, 0, 0, 1])
            return a + b

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add.__name__, 'add')

        @retry(times=100, delay=0.1, ignore_error=[ZeroDivisionError])
        def add(a, b):
            1 / random.choice([0, 0, 0, 0, 0, 0, 1])
            return a + b

        with self.assertRaises(ZeroDivisionError):
            add(1, 2)

        @retry(times=3, delay=0.1, ignore_error=[ZeroDivisionError, TypeError])
        def add(a, b):
            1 / random.choice([0, 0, 0, 0, 0, 0, 1])
            return a + b

        with self.assertRaises(TypeError):
            add(1)
