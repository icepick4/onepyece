import unittest

from onepyece import api


class TestGetData(unittest.TestCase):
    def test_get_data(self):
        data = api.get_data("https://api.api-onepiece.com/v2/characters/en")
        self.assertIsInstance(data, list)

    def test_get_data_with_wrong_url(self):
        self.assertRaises(ValueError, api.get_data, "wrong")

    def test_get_data_empty_result(self):
        data = api.get_data("https://api.api-onepiece.com/v2/characters/en/4444")
        self.assertIsNone(data)
