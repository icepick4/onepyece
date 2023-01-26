import unittest

from onepyece import api


class TestGetData(unittest.TestCase):
    def test_get_data(self):
        data = api.get_data("characters")
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_get_data_with_search(self):
        data = api.get_data("characters", "id", "1")
        self.assertIsInstance(data, dict)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["french_name"], "Monkey D Luffy")
    
    def test_get_data_with_search_and_count(self):
        data = api.get_data("characters", "count")
        self.assertIsInstance(data, int)
        self.assertEqual(data, 760)

    def test_get_data_with_search_and_resource_id(self):
        data = api.get_data("characters", "name", "Monkey D Luffy")
        self.assertIsInstance(data, dict)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["french_name"], "Monkey D Luffy")