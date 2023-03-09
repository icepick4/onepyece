"""
Mother class of the API wrapper
"""
from .api import get_data
from .common import build_url, pretty_print


class API:
    """
    The API class

    This class is used to get data from the API and exploit data from it

    :param endpoint: The endpoint to get the data from
    :param search_term: The search to get the data from
    :param resource: The resource to get the data from
    :param object: If the object is an object or not
    :param data: The data object to use to create the object

    See https://api-onepiece.com/documentation for more information about URL
    """

    def __init__(self, endpoint=None, search_term=None, resource=None, data=None):
        self.endpoint = endpoint
        self.search_term = search_term
        self.resource = resource
        if self.endpoint is not None:
            self.url = build_url(endpoint, search_term, resource)
        if data is None:
            self.__load()
        else:
            self.url = None
            self.update_dict_recursively(data)

    def __repr__(self):
        if self.url is None:
            return f"API(object={self.__dict__})"
        if self.resource is not None:
            return (
                f"API(endpoint='{self.endpoint}',"
                f"search='{self.search_term}',"
                f"resource='{self.resource}',"
                f"url='{self.url}')"
            )
        if self.search_term is not None:
            return f"API(endpoint='{self.endpoint}', search='{self.search_term}', url='{self.url}')"
        return f"API(endpoint='{self.endpoint}', url='{self.url}')"

    def __str__(self):
        if getattr(self, "count", None) is not None:
            return f"Total {self.endpoint} found for this search: {self.count}."
        return pretty_print(self.__dict__)

    def __iter__(self):
        if getattr(self, "results", None) is not None:
            return iter(self.results)
        raise TypeError(f"Object of type {type(self)} is not iterable")

    def __getitem__(self, item):
        if getattr(self, "results", None) is not None:
            return self.results[item]
        raise TypeError(f"Object of type {type(self)} has no __getitem__ for unique result")

    def __len__(self):
        if getattr(self, "count", None) is not None:
            return self.count
        raise TypeError(f"Object of type {type(self)} has no len() for unique result")

    def __load(self):
        """
        Load the data from the API

        Set the attributes of the object with the data from the API

        :return: None
        """
        api_data = get_data(self.url)
        if api_data is None:
            raise ValueError(
                f"No data found for the given search:{self.search_term}"
                f" and resource_id:{self.resource}"
            )
        if isinstance(api_data, list) and len(api_data) > 1:
            self.results = [API(data=result) for result in api_data]
            self.count = len(api_data)
        elif isinstance(api_data, list) and len(api_data) == 1:
            self.__dict__.update(api_data[0])
        elif isinstance(api_data, dict):
            self.update_dict_recursively(api_data)
        elif isinstance(api_data, int):
            self.count = api_data
        else:
            raise ValueError(f"Unknown data type: {type(api_data)}")

    def update_dict_recursively(self, data):
        """
        Update the dict of the object recursively

        :param data: The data to update the dict with
        :return: None
        """
        for key, value in data.items():
            if isinstance(value, dict):
                self.__dict__[key] = API(data=value)
            elif isinstance(value, list):
                self.__dict__[key] = API(data=value[0])
            else:
                self.__dict__[key] = value

    def search(self, search, resource=None):
        """
        Search for a specific search term after initializing the API object
        """
        if self.search_term is None and self.resource is None:
            return API(self.endpoint, search, resource)
        raise ValueError(
            "You can't instantiate a search API object because you already have"
            f"{self.search_term} as search and {self.resource} as resource"
        )

    def edit_resource(self, resource):
        """
        Edit the resource of the API object
        Use this method after using the search method
        """
        if self.search_term is None:
            raise ValueError('You can\'t change the resource without'
                             ' search use the method search() first'
                             )
        temp_api = API(self.endpoint, self.search_term, resource)
        self.__dict__.update(temp_api.__dict__)
