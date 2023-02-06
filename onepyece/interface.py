import json

from .api import get_data
from .common import build_url, pretty_print


class API:
    def __init__(self, endpoint=None, search_term=None, resource=None, object=False, data_object=None):
        self.endpoint = endpoint
        self.search_term = search_term
        self.resource = resource
        self.object = object
        if endpoint is not None:
            self.url = build_url(endpoint, search_term, resource)
        if not object:
            self.__load()
        else:
            self.update_dict_recursively(data_object)


    def __repr__(self):
        if self.object:
            return f"API(object={self.__dict__})"
        if self.resource is not None:
            return f"API(endpoint='{self.endpoint}', search='{self.search_term}', resource='{self.resource}', url='{self.url}')"
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
        api_data = get_data(self.url)
        if api_data is None:
            raise ValueError(f"No data found for the given search:{self.search_term} and resource_id:{self.resource}")
        elif isinstance(api_data, list) and len(api_data) > 1:
            self.results = [API(object=True, data_object=result) for result in api_data]
            self.count = len(api_data)
        elif isinstance(api_data, list) and len(api_data) == 1:
            self.__dict__.update(api_data[0])
        elif isinstance(api_data, dict):
            self.update_dict_recursively(api_data)
        elif isinstance(api_data, int):
            self.count = api_data
        else:
            raise ValueError(f"Unknown data type: {type(api_data)}")

    def update_dict_recursively(self, data_object):
        for key, value in data_object.items():
            if isinstance(value, dict):
                self.__dict__[key] = API(object=True, data_object=value)
            elif isinstance(value, list):
                self.__dict__[key] = API(object=True, data_object=value[0])
            else:
                self.__dict__[key] = value

    def search(self, search, resource=None):
        if self.search_term is None and self.resource is None:
            return API(self.endpoint, search, resource)
        raise ValueError(f"You can't instantiate a search API object because you already have {self.search_term} as search and {self.resource} as resource")

    def edit_resource(self, resource):
        if self.search is None:
            raise ValueError('You can\'t change the resource without search use the method search()')
        self.__dict__ = API(self.endpoint, self.search_term, resource).__dict__
