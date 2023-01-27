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


def haki_by_roman_name(resource_id):
    return API("hakis", "roman_name", resource_id)


def count_hakis():
    return API("hakis", "count")


def character_by_id(resource_id):
    return API("characters", "id", resource_id)


def character_by_name(resource_id):
    return API("characters", "name", resource_id)


def character_by_job(resource_id):
    return API("characters", "job", resource_id)


def character_by_bounty(resource_id):
    return API("characters", "bounty", resource_id)


def character_by_status(resource_id):
    return API("characters", "status", resource_id)


def character_by_size(resource_id):
    return API("characters", "size", resource_id)


def count_characters():
    return API("characters", "count")


def dial_by_id(resource_id):
    return API("dials", "id", resource_id)


def dial_by_name(resource_id):
    return API("dials", "name", resource_id)


def dial_by_type(resource_id):
    return API("dials", "type", resource_id)


def count_dials():
    return API("dials", "count")


def luffy_gear_by_id(resource_id):
    return API("luffy/gears", "id", resource_id)


def luffy_gear_by_title(resource_id):
    return API("luffy/gears", "title", resource_id)


def count_luffy_gears():
    return API("luffy/gears", "count")


def luffy_technique_by_id(resource_id):
    return API("luffy/techniques", "id", resource_id)


def luffy_technique_by_name(resource_id):
    return API("luffy/techniques", "name", resource_id)


def luffy_technique_by_translation(resource_id):
    return API("luffy/techniques", "translation", resource_id)


def count_luffy_techniques():
    return API("luffy/techniques", "count")


def locate_by_id(resource_id):
    return API("locates", "id", resource_id)


def locate_by_name(resource_id):
    return API("locates", "name", resource_id)


def locate_by_sea(resource_id):
    return API("locates", "sea", resource_id)


def locate_by_affiliation(resource_id):
    return API("locates", "affiliation", resource_id)


def count_locates():
    return API("locates", "count")


def fruit_by_id(resource_id):
    return API("fruits", "id", resource_id)


def fruit_by_name(resource_id):
    return API("fruits", "name", resource_id)


def fruit_by_type(resource_id):
    return API("fruits", "type", resource_id)


def count_fruits():
    return API("fruits", "count")


def sword_by_id(resource_id):
    return API("swords", "id", resource_id)


def sword_by_name(resource_id):
    return API("swords", "name", resource_id)


def count_swords():
    return API("swords", "count")


def boat_by_id(resource_id):
    return API("boats", "id", resource_id)


def boat_by_name(resource_id):
    return API("boats", "name", resource_id)


def boat_by_type(resource_id):
    return API("boats", "type", resource_id)


def boat_by_crew_id(resource_id):
    return API("boats", "crew_id", resource_id)


def boat_by_captain_id(resource_id):
    return API("boats", "captain_id", resource_id)


def count_boats():
    return API("boats", "count")


def crew_by_id(resource_id):
    return API("crews", "id", resource_id)


def crew_by_name(resource_id):
    return API("crews", "name", resource_id)


def crew_by_status(resource_id):
    return API("crews", "status", resource_id)


def count_crews():
    return API("crews", "count")
