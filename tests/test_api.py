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



class TestBuildURL(unittest.TestCase):
    def test_build_url_no_search(self, endpoint="characters"):
        url = api.build_url(endpoint)
        self.assertEqual(url, "https://api.api-onepiece.com/characters")

    def test_build_url_with_search(self, endpoint="characters", search="id", resource_id="1"):
        url = api.build_url(endpoint, search, resource_id)
        self.assertEqual(url, "https://api.api-onepiece.com/characters/1")

    def test_build_url_with_search_and_count(self, endpoint="characters", search="count"):
        url = api.build_url(endpoint, search)
        self.assertEqual(url, "https://api.api-onepiece.com/characters/count")

    def test_build_url_with_search_and_resource_id(self, endpoint="characters", search="name", resource_id="Monkey D Luffy"):
        url = api.build_url(endpoint, search, resource_id)
        self.assertEqual(url, "https://api.api-onepiece.com/characters/search/name/Monkey%20D%20Luffy")

    def test_build_url_with_search_and_resource_id_with_slash(self, endpoint="characters", search="name", resource_id="Baggy / Le Clown"):
        url = api.build_url(endpoint, search, resource_id)
        self.assertEqual(url, "https://api.api-onepiece.com/characters/search/name/Baggy")

    def test_build_url_with_search_and_resource_id_with_slash_and_space(self, endpoint="characters", search="name", resource_id="Baggy / Le Clown "):
        url = api.build_url(endpoint, search, resource_id)
        self.assertEqual(url, "https://api.api-onepiece.com/characters/search/name/Baggy")

    def test_build_url_by_title(self, endpoint="episodes", search="title", resource_id="Je suis Luffy !"):
        url = api.build_url(endpoint, search, resource_id)
        self.assertEqual(url, "https://api.api-onepiece.com/episodes/search/Je%20suis%20Luffy%20!")
