import unittest

from onepyece import api


class TestGetData(unittest.TestCase):
    def test_get_data(self):
        data = api.get_data("characters")
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
