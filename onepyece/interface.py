from .api import get_data
from .common import build_url


class API:
    def __init__(self, endpoint, resource_id):
        self.endpoint = endpoint
        self.resource_id = resource_id
        self.result = {}
        self.load()

    def __repr__(self):
        return f"API(endpoint={self.endpoint}, resource_id={self.resource_id})"

    def __str__(self):
        return str(self.result["french_name"])

    def load(self):
        self.result = get_data(self.endpoint, self.resource_id)


class APIList:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.name = self.endpoint.replace("/", " ").title()
        self.results = []
        self.load()

    def __repr__(self):
        return f"APIList(endpoint={self.endpoint})"

    def __str__(self):
        return str(self.name)

    def __iter__(self):
        return iter(self.results)

    def load(self):
        data = get_data(self.endpoint)
        for resource in data:
            resource_id = resource["french_name"]
            api = API(self.endpoint, resource_id)
            self.results.append(api)
