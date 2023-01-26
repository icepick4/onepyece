import unittest

from onepyece import common


class TestBuildURL(unittest.TestCase):
    def test_build_url_no_search(self, endpoint="characters"):
        url = common.build_url(endpoint)
        self.assertEqual(url, "https://api.api-onepiece.com/characters")

    def test_build_url_with_search(self, endpoint="characters", search="id", resource_id="1"):
        url = common.build_url(endpoint, search, resource_id)
        self.assertEqual(url, "https://api.api-onepiece.com/characters/1")

    def test_build_url_with_search_and_count(self, endpoint="characters", search="count"):
        url = common.build_url(endpoint, search)
        self.assertEqual(url, "https://api.api-onepiece.com/characters/count")

    def test_build_url_with_search_and_resource_id(self, endpoint="characters", search="name", resource_id="Monkey D Luffy"):
        url = common.build_url(endpoint, search, resource_id)
        self.assertEqual(url, "https://api.api-onepiece.com/characters/search/name/Monkey%20D%20Luffy")

    def test_build_url_with_search_and_resource_id_with_slash(self, endpoint="characters", search="name", resource_id="Baggy / Le Clown"):
        url = common.build_url(endpoint, search, resource_id)
        self.assertEqual(url, "https://api.api-onepiece.com/characters/search/name/Baggy")

    def test_build_url_with_search_and_resource_id_with_slash_and_space(self, endpoint="characters", search="name", resource_id="Baggy / Le Clown "):
        url = common.build_url(endpoint, search, resource_id)
        self.assertEqual(url, "https://api.api-onepiece.com/characters/search/name/Baggy")

    def test_build_url_by_title(self, endpoint="episodes", search="title", resource_id="Je suis Luffy !"):
        url = common.build_url(endpoint, search, resource_id)
        self.assertEqual(url, "https://api.api-onepiece.com/episodes/search/Je%20suis%20Luffy%20!")


class TestCheckParams(unittest.TestCase):
    """ Test the check_params function

    The None value is returned if the parameters are valid
    The ValueError is raised if the parameters are not valid
    """
    def test_endpoint(self, endpoint="characters"):
        self.assertEqual(common.check_params(endpoint), None)

    def test_endpoint_with_wrong_value(self, endpoint="wrong"):
        self.assertRaises(ValueError, common.check_params, endpoint)

    def test_search_no_resource(self, endpoint="characters", search="id"):
        self.assertRaises(ValueError, common.check_params, endpoint, search)

    def test_search_with_resource(self, endpoint="characters", search="id", resource_id="1"):
        self.assertEqual(common.check_params(endpoint, search, resource_id), None)

    def test_search_with_wrong_value(self, endpoint="characters", search="wrong", resource_id="1"):
        self.assertRaises(ValueError, common.check_params, endpoint, search, resource_id)

class TestConvertName(unittest.TestCase):
    def test_convert_name(self, name="Baggy / Le Clown"):
        self.assertEqual(common.convert_name(name), "Baggy")

    def test_convert_name_with_space(self, name="Baggy / Le Clown "):
        self.assertEqual(common.convert_name(name), "Baggy")
