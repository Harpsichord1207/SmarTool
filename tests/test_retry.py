import random
import unittest

from src import retry


class TestRetry(unittest.TestCase):

    def test_retry(self):

        @retry
        def add(a, b):
            1 / random.choice([0, 0, 1])
            return a + b

        add(1, 2)
