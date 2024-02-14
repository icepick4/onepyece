import unittest

from onepyece import common, interface


class TestBuildURL(unittest.TestCase):
    """ Test the build_url function
    The url is built from the endpoint, the search and the resource
    """
    def setUp(self):
        self.BASE_URL = "https://api.api-onepiece.com/v2/"

    def test_url_no_search(self, endpoint="characters"):
        url = common.build_url(endpoint, "en",)
        self.assertEqual(url, f"{self.BASE_URL}characters/en")

    def test_url_with_search(self, endpoint="characters", search="id", resource=1):
        url = common.build_url(endpoint, "en", search, resource)
        self.assertEqual(url, f"{self.BASE_URL}characters/en/1")

    def test_url_with_search_and_count(self, endpoint="characters", search="count"):
        url = common.build_url(endpoint, "en", search)
        self.assertEqual(url, f"{self.BASE_URL}characters/en/count")

    def test_url_with_search_and_resource_id(self, endpoint="characters", search="name", resource="Monkey D Luffy"):
        url = common.build_url(endpoint, "en", search, resource)
        self.assertEqual(url, f"{self.BASE_URL}characters/en/search?name=Monkey%20D%20Luffy")

    def test_url_with_search_and_with_slash(self, endpoint="characters", search="name", resource="Baggy / Le Clown"):
        url = common.build_url(endpoint, "en", search, resource)
        self.assertEqual(url, f"{self.BASE_URL}characters/en/search?name=Baggy")

    def test_url_search_with_slash_and_space(self, endpoint="characters", search="name", resource="Baggy / Le Clown "):
        url = common.build_url(endpoint, "en", search, resource)
        self.assertEqual(url, f"{self.BASE_URL}characters/en/search?name=Baggy")

    def test_url_by_title(self, endpoint="episodes", search="title", resource="Je suis Luffy !"):
        url = common.build_url(endpoint, "en", search, resource)
        self.assertEqual(url, f"{self.BASE_URL}episodes/en/search?title=Je%20suis%20Luffy%20!")

    def test_url_search_other_id(self, endpoint="boats", search="crew_id", resource=1):
        url = common.build_url(endpoint, "en", search, resource)
        self.assertEqual(url, f"{self.BASE_URL}boats/en/crew/1")


class TestCheckParams(unittest.TestCase):
    """ Test the check_params function
    The None value is returned if the parameters are valid
    The ValueError is raised if the parameters are not valid
    """

    def test_endpoint(self, endpoint="characters"):
        self.assertEqual(common.check_params(endpoint), None)

    def test_endpoint_with_wrong_value(self, endpoint="wrong"):
        self.assertRaises(ValueError, common.check_params, endpoint, "en")

    def test_search_no_resource(self, endpoint="characters", search="id"):
        self.assertRaises(ValueError, common.check_params, endpoint, "en", search)

    def test_search_with_resource(self, endpoint="characters", search="id", resource=1):
        self.assertEqual(common.check_params(endpoint, "en", search, resource), None)

    def test_search_with_wrong_value(self, endpoint="characters", search="wrong", resource=1):
        self.assertRaises(ValueError, common.check_params, endpoint, "en", search, resource)


class TestConvertName(unittest.TestCase):
    def test_convert_resource(self, name="Baggy / Le Clown"):
        self.assertEqual(common.convert_resource(name), "Baggy")

    def test_convert_resource_with_space(self, name="Baggy / Le Clown "):
        self.assertEqual(common.convert_resource(name), "Baggy")


class TestEndpointsSearches(unittest.TestCase):
    def test_endpoints(self):
        """Testing if all combinations of endpoints and searches return some data.
        The ValueError means that resource doesnt exist but the endpoint and search are valid
        """
        resource = "123456798123456789"
        for endpoint in common.ENDPOINTS:
            for search in common.ENDPOINTS[endpoint]:
                self.assertRaises(ValueError, interface.API, endpoint, search, resource)
