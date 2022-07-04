import unittest

from src import Flatter


class TestRetry(unittest.TestCase):

    def test_flat_list(self):
        data = [1, (2, [3, 4, (5, 6)])]
        self.assertEqual(Flatter.flat_list(data), [1, 2, 3, 4, 5, 6])
        self.assertNotEqual(Flatter.flat_list(data), [1, 2, 3, 4, [5, 6]])

    def test_flat_dict(self):
        data = {1: 2}
        self.assertEqual(data, Flatter.flat_dict(data))

        data = {1: [2, 3]}
        self.assertEqual({'1_0': 2, '1_1': 3}, Flatter.flat_dict(data))

        data = {1: {2: 3}}
        self.assertEqual({'1_2': 3}, Flatter.flat_dict(data))

        data = {1: 2, 3: {4: 5, 6: [7, 8]}}
        self.assertEqual({1: 2, '3_4': 5, '3_6_0': 7, '3_6_1': 8}, Flatter.flat_dict(data))

        data = {
            'k1': 'v1',
            'k2_list': [
                {'v2': 'v3'},
                {'v4': 'v5'},
            ],
            'k3': {
                'k4': ['k5', {'k6': 'k7'}],
                'k8': 'k9'
            }
        }
        self.assertEqual(
            {
                'k1': 'v1',
                'k2_list_0_v2': 'v3',
                'k2_list_1_v4': 'v5',
                'k3_k4_0': 'k5',
                'k3_k4_1_k6': 'k7',
                'k3_k8': 'k9'
            },
            Flatter.flat_dict(data)
        )
