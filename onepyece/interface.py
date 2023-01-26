from .api import get_data
from .common import build_url


class API:
    def __init__(self, endpoint, search, resource):
        self.endpoint = endpoint
        self.search = search
        self.resource = resource
        self.url = build_url(endpoint, search, resource)
        self.load()

    def __repr__(self):
        return f"API(endpoint={self.endpoint}, resource_id={self.resource})"

    def __str__(self):
        return str(self.resource)

    def __iter__(self):
        return iter(self.results)

    def load(self):
        api_data = get_data(self.url)
        if api_data is None:
            raise ValueError(f"No data found for the given search:{self.search} and resource_id:{self.resource}")
        elif isinstance(api_data, list):
            self.results = api_data
        else:
            self.__dict__.update(api_data)
