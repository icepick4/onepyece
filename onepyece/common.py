BASE_URL = "https://api.api-onepiece.com/"
ENDPOINTS = [
    "episodes",
    "movies",
    "tomes",
    "chapters",
    "arcs",
    "sagas",
    "hakis",
    "characters",
    "dials",
    "luffy/gears",
    "luffy/techniques",
    "locates",
    "swords",
    "boats",
    "crews",
]

def validate(endpoint):
    if endpoint not in ENDPOINTS:
        raise ValueError(f"Unknown API endpoint '{endpoint}'")
    return None

def build_url(endpoint, resource_id=None):
    validate(endpoint)
    if resource_id is not None:
        resource_id = cut_names(resource_id)
        return f"{BASE_URL}{endpoint}/search/name/{resource_id}"
    return f"{BASE_URL}{endpoint}"

def cut_names(name):
    return name.split(" / ")[0] if ' / ' in name else name