import unittest

from onepyece import interface


class TestAPI(unittest.TestCase):
    def test_unique_character(self):
        api_object = interface.API("characters", "id", 1)
        self.assertIsInstance(api_object, interface.API)
        self.assertEqual(api_object.resource, 1)
        self.assertEqual(api_object.id, 1)
        self.assertEqual(api_object.french_name, "Monkey D Luffy")

    def test_unique_character_with_wrong_resource_id(self):
        self.assertRaises(ValueError, interface.API, "characters", "id", "wrong")

    def test_unique_character_with_wrong_search(self):
        self.assertRaises(ValueError, interface.API, "characters", "wrong", 1)

    def test_unique_character_with_wrong_endpoint(self):
        self.assertRaises(ValueError, interface.API, "wrong", "id", 1)

    def test_multiple_result(self):
        api_object = interface.API("hakis", "name", "Haki")
        self.assertIsInstance(api_object, interface.API)
        self.assertIsInstance(api_object.results, list)
        self.assertEqual(api_object.resource, "Haki")
        self.assertRaises(AttributeError, getattr, api_object, "id")
        self.assertIsInstance(api_object.results[0], interface.API)
        self.assertEqual(api_object.results[0].french_name, "Haki de l'Observation")

    def test_count_implicit(self):
        api_object = interface.API("hakis")
        self.assertIsInstance(api_object, interface.API)
        self.assertEqual(api_object.count, 3)

    def test_count_implicit_with_search(self):
        api_object = interface.API("hakis", "name", "Haki")
        self.assertIsInstance(api_object, interface.API)
        self.assertEqual(api_object.count, 3)

    def test_count_explicit(self):
        api_object = interface.API("hakis", "count")
        self.assertIsInstance(api_object, interface.API)
        self.assertEqual(api_object.count, 3)

    def test_iterate_object(self):
        # Multiple results -> iterate
        api_object = interface.API("crews")
        self.assertIsInstance(api_object, interface.API)
        for result in api_object:
            self.assertIsInstance(result, interface.API)
        # Unique result -> do not iterate
        api_object = interface.API("crews", "id", 1)
        self.assertIsInstance(api_object, interface.API)
        self.assertRaises(TypeError, iter, api_object)

    def test_recursive_dict(self):
        api_object = interface.API('hakis', 'characters_id', 1)
        self.assertIsInstance(api_object[0].characters.haki_character, interface.API)

    def test_search_method(self):
        api_object = interface.API('characters').search('job', 'capitaine')
        self.assertEqual(api_object[1].french_name, 'Cavendish')

    def test_search_method_with_search(self):
        with self.assertRaises(ValueError):
            interface.API('characters', 'count').search('job', 'capitaine')

    def test_search_method_with_search_and_resource(self):
        with self.assertRaises(ValueError):
            interface.API('characters', 'status', 'décédé').search('job', 'capitaine')

    def test_edit_resource(self):
        api_object = interface.API('characters', 'name', 'luffy')
        self.assertEqual(api_object.french_name, 'Monkey D Luffy')
        api_object.edit_resource('zoro')
        self.assertEqual(api_object.french_name, 'Roronoa Zoro')

    def test_edit_resource_not_allowed(self):
        api_object = interface.API('characters', 'count')
        api_object_2 = interface.API('crews', 'yonko')
        with self.assertRaises(ValueError):
            api_object.edit_resource('zoro')
        with self.assertRaises(ValueError):
            api_object_2.edit_resource('zoro')
        
