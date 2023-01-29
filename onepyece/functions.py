from .interface import API


def episode_by_id(resource):
    return API("episodes", "id", resource)


def episode_by_title(resource):
    return API("episodes", "title", resource)


def episode_by_saga_id(resource):
    return API("episodes", "saga_id", resource)


def episode_by_arc_id(resource):
    return API("episodes", "arc_id", resource)


def count_episodes():
    return API("episodes", "count")


def movie_by_id(resource):
    return API("movies", "id", resource)


def movie_by_title(resource):
    return API("movies", "title", resource)


def count_movies():
    return API("movies", "count")


def tome_by_id(resource):
    return API("tomes", "id", resource)


def tome_by_title(resource):
    return API("tomes", "title", resource)


def count_tomes():
    return API("tomes", "count")


def chapter_by_id(resource):
    return API("chapters", "id", resource)


def chapter_by_title(resource):
    return API("chapters", "title", resource)


def chapter_by_tome_id(resource):
    return API("chapters", "tome_id", resource)


def chapter_by_tome(resource):
    return API("chapters", "tome", resource)


def count_chapters():
    return API("chapters", "count")


def arc_by_id(resource):
    return API("arcs", "id", resource)

# This functions is not working because the API link is not working
# def arc_by_title(resource):
#     return API("arcs", "title", resource)


def arc_by_saga_id(resource):
    return API("arcs", "saga_id", resource)


def count_arcs():
    return API("arcs", "count")


def saga_by_id(resource):
    return API("sagas", "id", resource)


def saga_by_title(resource):
    return API("sagas", "title", resource)


def count_sagas():
    return API("sagas", "count")


def haki_by_id(resource):
    return API("hakis", "id", resource)


def haki_by_name(resource):
    return API("hakis", "name", resource)


def haki_by_roman_name(resource):
    return API("hakis", "roman_name", resource)


def haki_by_characters_id(resource):
    return API("hakis", "characters_id", resource)


def count_hakis():
    return API("hakis", "count")


def character_by_id(resource):
    return API("characters", "id", resource)


def character_by_name(resource):
    return API("characters", "name", resource)


def character_by_job(resource):
    return API("characters", "job", resource)


def character_by_bounty(resource):
    return API("characters", "bounty", resource)


def character_by_status(resource):
    return API("characters", "status", resource)


def character_by_size(resource):
    return API("characters", "size", resource)


def character_by_crew_id(resource):
    return API("characters", "crew_id", resource)


def character_by_fruit_id(resource):
    return API("characters", "fruit_id", resource)


def count_characters():
    return API("characters", "count")


def dial_by_id(resource):
    return API("dials", "id", resource)


def dial_by_name(resource):
    return API("dials", "name", resource)


def dial_by_type(resource):
    return API("dials", "type", resource)


def count_dials():
    return API("dials", "count")


def luffy_gear_by_id(resource):
    return API("luffy/gears", "id", resource)


def luffy_gear_by_title(resource):
    return API("luffy/gears", "title", resource)


def count_luffy_gears():
    return API("luffy/gears", "count")


def luffy_technique_by_id(resource):
    return API("luffy/techniques", "id", resource)


def luffy_technique_by_name(resource):
    return API("luffy/techniques", "name", resource)


def luffy_technique_by_translation(resource):
    return API("luffy/techniques", "translation", resource)


def luffy_technique_by_gear_id(resource):
    return API("luffy/techniques", "gear_id", resource)


def count_luffy_techniques():
    return API("luffy/techniques", "count")


def locate_by_id(resource):
    return API("locates", "id", resource)


def locate_by_name(resource):
    return API("locates", "name", resource)


def locate_by_sea(resource):
    return API("locates", "sea", resource)


def locate_by_affiliation(resource):
    return API("locates", "affiliation", resource)


def count_locates():
    return API("locates", "count")


def fruit_by_id(resource):
    return API("fruits", "id", resource)


def fruit_by_name(resource):
    return API("fruits", "name", resource)


def fruit_by_type(resource):
    return API("fruits", "type", resource)


def count_fruits():
    return API("fruits", "count")


def sword_by_id(resource):
    return API("swords", "id", resource)


def sword_by_name(resource):
    return API("swords", "name", resource)


def count_swords():
    return API("swords", "count")


def boat_by_id(resource):
    return API("boats", "id", resource)


def boat_by_name(resource):
    return API("boats", "name", resource)


def boat_by_type(resource):
    return API("boats", "type", resource)


def boat_by_crew_id(resource):
    return API("boats", "crew_id", resource)


def boat_by_captain_id(resource):
    return API("boats", "captain_id", resource)


def count_boats():
    return API("boats", "count")


def crew_by_id(resource):
    return API("crews", "id", resource)


def crew_by_name(resource):
    return API("crews", "name", resource)


def crew_by_status(resource):
    return API("crews", "status", resource)


def yonko_crews():
    return API("crews", "yonko")


def count_crews():
    return API("crews", "count")
