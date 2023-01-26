import unittest

from onepyece import interface


class TestAPI(unittest.TestCase):
    def test_unique_character(self):
        api_object = interface.API("characters", "id", "1")
        self.assertIsInstance(api_object, interface.API)
        self.assertEqual(api_object.resource, "1")
        self.assertEqual(api_object.id, 1)
        self.assertEqual(api_object.french_name, "Monkey D Luffy")

    def test_unique_character_with_wrong_resource_id(self):
        self.assertRaises(ValueError, interface.API, "characters", "id", "wrong")

    def test_unique_character_with_wrong_search(self):
        self.assertRaises(ValueError, interface.API, "characters", "wrong", "1")

    def test_unique_character_with_wrong_endpoint(self):
        self.assertRaises(ValueError, interface.API, "wrong", "id", "1")

    def test_multiple_result(self):
        api_object = interface.API("hakis", "name", "Haki")
        self.assertIsInstance(api_object, interface.API)
        self.assertIsInstance(api_object.results, list)
        self.assertEqual(api_object.resource, "Haki")
        self.assertRaises(AttributeError, getattr, api_object, "id")
        self.assertIsInstance(api_object.results[0], dict)
        self.assertEqual(api_object.results[0]["french_name"], "Haki de l'Observation")

    def test_count(self):
        api_object = interface.API("hakis")
        self.assertIsInstance(api_object, interface.API)
        self.assertEqual(api_object.count, 3)

    
