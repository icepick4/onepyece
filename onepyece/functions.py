from .interface import API


def episode_by_id(resource_id):
    return API("episodes", "id", resource_id)

def episode_by_title(resource_id):
    return API("episodes", "title", resource_id)

def count_episodes():
    return API("episodes", "count")

def movie_by_id(resource_id):
    return API("movies", "id", resource_id)

def movie_by_title(resource_id):
    return API("movies", "title", resource_id)

def count_movies():
    return API("movies", "count")

def tome_by_id(resource_id):
    return API("tomes", "id", resource_id)

def tome_by_title(resource_id):
    return API("tomes", "title", resource_id)

def count_tomes():
    return API("tomes", "count")

def chapter_by_id(resource_id):
    return API("chapters", "id", resource_id)

def chapter_by_title(resource_id):
    return API("chapters", "title", resource_id)

def count_chapters():
    return API("chapters", "count")

def arc_by_id(resource_id):
    return API("arcs", "id", resource_id)

def arc_by_title(resource_id):
    return API("arcs", "title", resource_id)

def count_arcs():
    return API("arcs", "count")

def saga_by_id(resource_id):
    return API("sagas", "id", resource_id)

def saga_by_title(resource_id):
    return API("sagas", "title", resource_id)

def count_sagas():
    return API("sagas", "count")

def haki_by_id(resource_id):
    return API("hakis", "id", resource_id)

def haki_by_name(resource_id):
    return API("hakis", "name", resource_id)

def count_hakis():
    return API("hakis", "count")

def character_by_id(resource_id):
    return API("characters", "id", resource_id)

def character_by_name(resource_id):
    return API("characters", "name", resource_id)

def count_characters():
    return API("characters", "count")








