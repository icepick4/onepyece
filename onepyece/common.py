import json

URL = "https://api.api-onepiece.com/"
ENDPOINTS = {
    "episodes": ["id", "count", "title", "saga_id", "arc_id"],
    "movies": ["id", "count", "title"],
    "tomes": ["id", "count", "title"],
    "chapters": ["id", "count", "title", "tome_id"],
    "arcs": ["id", "count", "saga_id"],
    "sagas": ["id", "count", "title"],
    "hakis": ["id", "count", "name", "roman_name", "characters_id"],
    "characters": ["id", "count", "name", "job", "bounty", "status", "size", "crew_id", "fruit_id"],
    "dials": ["id", "count", "name", "type"],
    "luffy/gears": ["id", "count", "title"],
    "luffy/techniques": ["id", "count", "name", "translation", "gear_id"],
    "locates": ["id", "count", "name", "sea", "affiliation"],
    "fruits": ["id", "count", "type"],
    "swords": ["id", "count", "name"],
    "boats": ["id", "count", "name", "type", "crew_id", "captain_id"],
    "crews": ["id", "count", "name", "status", "yonko"],
}

STRING_SEARCHES = ["name", "job", "bounty", "status", "size", "type", "roman_name", "sea", "affiliation"]
ID_SEARCHES = ["crew_id", "captain_id"]
NO_SEARCH_ID_SEARCHES = ["saga_id", "arc_id", "characters_id", "gear_id", "tome_id", "fruit_id", "crew_id"]
NO_RESOURCE_SEARCHES = ["count", "yonko"]


def check_params(endpoint, search=None, resource=None):
    if endpoint not in ENDPOINTS:
        raise ValueError(f"Unknown API endpoint '{endpoint}'")
    if search is not None and search not in ENDPOINTS[endpoint]:
        raise ValueError(f"Unknown search '{search}' for endpoint '{endpoint}'")
    if search is not None and search not in NO_RESOURCE_SEARCHES and resource is None:
        raise ValueError("Resource is required for this search")
    if resource is not None and "id" in search and not isinstance(resource, int):
        raise ValueError("Resource must be an integer for this search")
    return None


def build_url(endpoint, search=None, resource=None):
    check_params(endpoint, search, resource)
    if search is not None:
        if resource is not None:
            resource = convert_resource(resource)
            return adding_search(endpoint, search, resource)
        return f"{URL}{endpoint}/{search}"
    return f"{URL}{endpoint}"


def adding_search(endpoint, search, resource=None):
    if search in STRING_SEARCHES:
        return f"{URL}{endpoint}/search/{search}/{resource}"
    elif search in NO_SEARCH_ID_SEARCHES and endpoint not in ['boats', 'arcs']:
        return f"{URL}{endpoint}/{search[:-3]}/{resource}"
    elif search in ID_SEARCHES:
        return f"{URL}{endpoint}/search/{search[:-3]}/{resource}"
    elif search == "title":
        return f"{URL}{endpoint}/search/{resource}"
    return f"{URL}{endpoint}/{resource}"


def convert_resource(resource):
    if isinstance(resource, int):
        return resource
    if ' / ' in resource:
        resource = resource.split(" / ")[0]
    return resource.replace(" ", "%20")


def pretty_print(data):
    def convert_to_dict(obj):
        return obj.__dict__
    
    json_string = json.dumps(data, indent=4, ensure_ascii=False, default=convert_to_dict).encode("utf8").decode()
    return json_string
