import json

URL = "https://api.api-onepiece.com/"
ENDPOINTS = {
    "episodes": ["id", "count", "title"],
    "movies": ["id", "count", "title"],
    "tomes": ["id", "count", "title"],
    "chapters": ["id", "count", "title"],
    "arcs": ["id", "count", "title"],
    "sagas": ["id", "count", "title"],
    "hakis": ["id", "count", "name", "roman_name"],
    "characters": ["id", "count", "name", "job", "bounty", "status", "size"],
    "dials": ["id", "count", "name", "type"],
    "luffy/gears": ["id", "count", "title"],
    "luffy/techniques": ["id", "count", "name", "translation"],
    "locates": ["id", "count", "name", "sea", "affiliation"],
    "fruits": ["id", "count", "type"],
    "swords": ["id", "count", "name"],
    "boats": ["id", "count", "name", "type", "crew_id", "captain_id"],
    "crews": ["id", "count", "name", "status"],
}

STRING_SEARCHES = ["name", "job", "bounty", "status", "size", "type"]
ID_SEARCHES = ["crew_id", "captain_id"]


def check_params(endpoint, search=None, resource_id=None):
    if endpoint not in ENDPOINTS:
        raise ValueError(f"Unknown API endpoint '{endpoint}'")
    if search is not None and search not in ENDPOINTS[endpoint]:
        raise ValueError(f"Unknown search '{search}' for endpoint '{endpoint}'")
    if search is not None and search != "count" and resource_id is None:
        raise ValueError("Resource ID is required for this search")
    if resource_id is not None and not isinstance(resource_id, str):
        raise ValueError("Resource ID must be a string")
    return None


def build_url(endpoint, search=None, resource_id=None):
    check_params(endpoint, search, resource_id)
    if search is not None:
        if resource_id is not None:
            resource_id = convert_name(resource_id)
            return adding_search(endpoint, search, resource_id)
        return f"{URL}{endpoint}/count"
    return f"{URL}{endpoint}"


def adding_search(endpoint, search, resource_id=None):
    if search in STRING_SEARCHES:
        return f"{URL}{endpoint}/search/{search}/{resource_id}"
    elif search in ID_SEARCHES:
        return f"{URL}{endpoint}/search/{search[:-3]}/{resource_id}"
    elif search == "title":
        return f"{URL}{endpoint}/search/{resource_id}"
    return f"{URL}{endpoint}/{resource_id}"


def convert_name(name):
    if ' / ' in name:
        name = name.split(" / ")[0]
    return name.replace(" ", "%20")


def pretty_print(data):
    return json.dumps(data, indent=4)
