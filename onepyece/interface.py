from .api import get_data
from .common import build_url, pretty_print


class API:
    def __init__(self, endpoint, search=None, resource=None):
        self.endpoint = endpoint
        self.search = search
        self.resource = resource
        self.url = build_url(endpoint, search, resource)
        self.load()

    def __repr__(self):
        return f"API(endpoint={self.endpoint}, resource_id={self.resource})"

    def __str__(self):
        if getattr(self, "results", None) is not None:
            for result in self.results:
                print(pretty_print(result))
            return ""
        if getattr(self, "count", None) is not None:
            return f"Total {self.endpoint} found: {self.count}"
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

    def load(self):
        api_data = get_data(self.url)
        if api_data is None:
            raise ValueError(f"No data found for the given search:{self.search} and resource_id:{self.resource}")
        elif isinstance(api_data, list) and len(api_data) > 1:
            self.results = api_data
            self.count = len(api_data)
        elif isinstance(api_data, list) and len(api_data) == 1:
            self.__dict__.update(api_data[0])
        elif isinstance(api_data, dict):
            self.__dict__.update(api_data)
        elif isinstance(api_data, int):
            self.count = api_data
        else:
            raise ValueError(f"Unknown data type: {type(api_data)}")
