from .interface import API


def episode_by_id(resource):
    """
    Get episode by id

    See https://api-onepiece.com/documentation/5-episode for more information

    :param resource: id of the episode (int)
    :return: API unique object
    """
    return API("episodes", "id", resource)


def episode_by_title(resource):
    """
    Get episode by title

    See https://api-onepiece.com/documentation/5-episode for more information

    :param resource: title of the episode (str)
    :return: API list object (with episodes matching the title search)
    """
    return API("episodes", "title", resource)


def episode_by_saga_id(resource):
    """
    Get episode by saga id

    See https://api-onepiece.com/documentation/5-episode for more information

    :param resource: saga id of the episode (int)
    :return: API list object (with episodes matching the saga id search)
    """
    return API("episodes", "saga_id", resource)


def episode_by_arc_id(resource):
    """
    Get episode by arc id

    See https://api-onepiece.com/documentation/5-episode for more information

    :param resource: arc id of the episode (int)
    :return: API list object (with episodes matching the arc id search)
    """
    return API("episodes", "arc_id", resource)


def episode_by_arc_title(resource):
    """
    Get episode by arc title

    See https://api-onepiece.com/documentation/5-episode for more information

    :param resource: arc title of the episode (str)
    :return: API list object (with episodes matching the arc title search)
    """
    return API("episodes", "arc_title", resource)


def episode_by_saga_title(resource):
    """
    Get episode by saga title

    See https://api-onepiece.com/documentation/5-episode for more information

    :param resource: saga title of the episode (str)
    :return: API list object (with episodes matching the saga title search)
    """
    return API("episodes", "saga_title", resource)


def count_episodes():
    """
    Get count of episodes

    See https://api-onepiece.com/documentation/5-episode for more information

    :return: API unique object (with the count of episodes)
    """
    return API("episodes", "count")


def movie_by_id(resource):
    """
    Get movie by id

    See https://api-onepiece.com/documentation/7-movie for more information

    :param resource: id of the movie (int)
    :return: API unique object
    """
    return API("movies", "id", resource)


def movie_by_title(resource):
    """
    Get movie by title

    See https://api-onepiece.com/documentation/7-movie for more information

    :param resource: title of the movie (str)
    :return: API list object (with movies matching the title search)
    """
    return API("movies", "title", resource)


def count_movies():
    """
    Get count of movies

    See https://api-onepiece.com/documentation/7-movie for more information

    :return: API unique object (with the count of movies)
    """
    return API("movies", "count")


def tome_by_id(resource):
    """
    Get tome by id

    See https://api-onepiece.com/documentation/4-tome for more information

    :param resource: id of the tome (int)
    :return: API unique object
    """
    return API("tomes", "id", resource)


def tome_by_title(resource):
    """
    Get tome by title

    See https://api-onepiece.com/documentation/4-tome for more information

    :param resource: title of the tome (str)
    :return: API list object (with tomes matching the title search)
    """
    return API("tomes", "title", resource)


def count_tomes():
    """
    Get count of tomes

    See https://api-onepiece.com/documentation/4-tome for more information

    :return: API unique object (with the count of tomes)
    """
    return API("tomes", "count")


def chapter_by_id(resource):
    """
    Get chapter by id

    See https://api-onepiece.com/documentation/3-chapter for more information

    :param resource: id of the chapter (int)
    :return: API unique object
    """
    return API("chapters", "id", resource)


def chapter_by_title(resource):
    """
    Get chapter by title

    See https://api-onepiece.com/documentation/3-chapter for more information

    :param resource: title of the chapter (str)
    :return: API list object (with chapters matching the title search)
    """
    return API("chapters", "title", resource)


def chapter_by_tome_id(resource):
    """
    Get chapter by tome id

    See https://api-onepiece.com/documentation/3-chapter for more information

    :param resource: tome id of the chapter (int)
    :return: API list object (with chapters matching the tome id search)
    """
    return API("chapters", "tome_id", resource)


def chapter_by_tome(resource):
    """
    Get chapter by tome title

    See https://api-onepiece.com/documentation/3-chapter for more information

    :param resource: title of the tome (str)
    :return: API list object (with chapters matching the tome title search)
    """
    return API("chapters", "tome", resource)


def count_chapters():
    """
    Get count of chapters

    See https://api-onepiece.com/documentation/3-chapter for more information

    :return: API unique object (with the count of chapters)
    """
    return API("chapters", "count")


def arc_by_id(resource):
    """
    Get arc by id

    See https://api-onepiece.com/documentation/15-arc for more information

    :param resource: id of the arc (int)
    :return: API unique object
    """
    return API("arcs", "id", resource)


def arc_by_title(resource):
    """
    Get arc by title

    See https://api-onepiece.com/documentation/15-arc for more information

    :param resource: title of the arc (str)
    :return: API list object (with arcs matching the title search)
    """
    return API("arcs", "title", resource)


def arc_by_saga_id(resource):
    """
    Get arc by saga id

    See https://api-onepiece.com/documentation/15-arc for more information

    :param resource: saga id of the arc (int)
    :return: API list object (with arcs matching the saga id search)
    """
    return API("arcs", "saga_id", resource)


def count_arcs():
    """
    Get count of arcs

    See https://api-onepiece.com/documentation/15-arc for more information

    :return: API unique object (with the count of arcs)
    """
    return API("arcs", "count")


def saga_by_id(resource):
    """
    Get saga by id

    See https://api-onepiece.com/documentation/1-saga for more information

    :param resource: id of the saga (int)
    :return: API unique object
    """
    return API("sagas", "id", resource)


def saga_by_title(resource):
    """
    Get saga by title

    See https://api-onepiece.com/documentation/1-saga for more information

    :param resource: title of the saga (str)
    :return: API list object (with sagas matching the title search)
    """
    return API("sagas", "title", resource)


def count_sagas():
    """
    Get count of sagas

    See https://api-onepiece.com/documentation/1-saga for more information

    :return: API unique object (with the count of sagas)
    """
    return API("sagas", "count")


def haki_by_id(resource):
    """
    Get haki by id

    See https://api-onepiece.com/documentation/9-haki for more information

    :param resource: id of the haki (int)
    :return: API unique object
    """
    return API("hakis", "id", resource)


def haki_by_name(resource):
    """
    Get haki by name

    See https://api-onepiece.com/documentation/9-haki for more information

    :param resource: name of the haki (str)
    :return: API list object (with hakis matching the name search)
    """
    return API("hakis", "name", resource)


def haki_by_roman_name(resource):
    """
    Get haki by romanized name

    See https://api-onepiece.com/documentation/9-haki for more information

    :param resource: romanized name of the haki (str)
    :return: API list object (with hakis matching the romanized name search)
    """
    return API("hakis", "roman_name", resource)


def haki_by_characters_id(resource):
    """
    Get haki by character id

    See https://api-onepiece.com/documentation/9-haki for more information

    :param resource: id of the character who has the haki (int)
    :return: API list object (with hakis matching the character id search)
    """
    return API("hakis", "characters_id", resource)


def count_hakis():
    """
    Get count of hakis

    See https://api-onepiece.com/documentation/9-haki for more information

    :return: API unique object (with the count of hakis)
    """
    return API("hakis", "count")


def character_by_id(resource):
    """
    Get character by id

    See https://api-onepiece.com/documentation/13-character for more information

    :param resource: id of the character (int)
    :return: API unique object
    """
    return API("characters", "id", resource)


def character_by_name(resource):
    """
    Get character by name

    See https://api-onepiece.com/documentation/13-character for more information

    :param resource: name of the character (str)
    :return: API list object (with characters matching the name search)
    """
    return API("characters", "name", resource)


def character_by_job(resource):
    """
    Get character by job

    See https://api-onepiece.com/documentation/13-character for more information

    :param resource: job of the character (str)
    :return: API list object (with characters matching the job search)
    """
    return API("characters", "job", resource)


def character_by_bounty(resource):
    """
    Get character by bounty

    See https://api-onepiece.com/documentation/13-character for more information

    :param resource: bounty of the character (str) (ex: '1.000.000')
    :return: API list object (with characters matching the bounty search)
    """
    return API("characters", "bounty", resource)


def character_by_status(resource):
    """
    Get character by status

    See https://api-onepiece.com/documentation/13-character for more information

    :param resource: status of the character (str) (ex: 'vivant', 'mort')
    :return: API list object (with characters matching the status search)
    """
    return API("characters", "status", resource)


def character_by_size(resource):
    """
    Get character by size

    See https://api-onepiece.com/documentation/13-character for more information

    :param resource: size of the character (str) or (int) (ex: '180cm', 180)
    :return: API list object (with characters matching the size search)
    """
    return API("characters", "size", resource)


def character_by_crew_id(resource):
    """
    Get character by crew id

    See https://api-onepiece.com/documentation/13-character for more information

    :param resource: id of the crew of the character (int)
    :return: API list object (with characters matching the crew id search)
    """
    return API("characters", "crew_id", resource)


def character_by_fruit_id(resource):
    """
    Get character by fruit id

    See https://api-onepiece.com/documentation/13-character for more information

    :param resource: id of the fruit of the character (int)
    :return: API list object (with characters matching the fruit id search)
    """
    return API("characters", "fruit_id", resource)


def count_characters():
    """
    Get count of characters

    See https://api-onepiece.com/documentation/13-character for more information

    :return: API unique object (with the count of characters)
    """
    return API("characters", "count")


def dial_by_id(resource):
    """
    Get dial by id

    See https://api-onepiece.com/documentation/6-dial for more information

    :param resource: id of the dial (int)
    :return: API unique object
    """
    return API("dials", "id", resource)


def dial_by_name(resource):
    """
    Get dial by name

    See https://api-onepiece.com/documentation/6-dial for more information

    :param resource: name of the dial (str)
    :return: API list object (with dials matching the name search)
    """
    return API("dials", "name", resource)


def dial_by_type(resource):
    """
    Get dial by type

    See https://api-onepiece.com/documentation/6-dial for more information

    :param resource: type of the dial (str)
    :return: API list object (with dials matching the type search)
    """
    return API("dials", "type", resource)


def count_dials():
    """
    Get count of dials

    See https://api-onepiece.com/documentation/6-dial for more information

    :return: API unique object (with the count of dials)
    """
    return API("dials", "count")


def luffy_gear_by_id(resource):
    """
    Get luffy gear by id

    See https://api-onepiece.com/documentation/10-luffy-gear for more information

    :param resource: id of the luffy gear (int)
    :return: API unique object
    """
    return API("luffy/gears", "id", resource)


def luffy_gear_by_title(resource):
    """
    Get luffy gear by title

    See https://api-onepiece.com/documentation/10-luffy-gear for more information

    :param resource: title of the luffy gear (str)
    :return: API list object (with luffy gears matching the title search)
    """
    return API("luffy/gears", "title", resource)


def count_luffy_gears():
    """
    Get count of luffy gears

    See https://api-onepiece.com/documentation/10-luffy-gear for more information

    :return: API unique object (with the count of luffy gears)
    """
    return API("luffy/gears", "count")


def luffy_technique_by_id(resource):
    """
    Get luffy technique by id

    See https://api-onepiece.com/documentation/11-luffy-technique for more information

    :param resource: id of the luffy technique (int)
    :return: API unique object
    """
    return API("luffy/techniques", "id", resource)


def luffy_technique_by_name(resource):
    """
    Get luffy technique by name

    See https://api-onepiece.com/documentation/11-luffy-technique for more information

    :param resource: name of the luffy technique (str)
    :return: API list object (with luffy techniques matching the name search)
    """
    return API("luffy/techniques", "name", resource)


def luffy_technique_by_translation(resource):
    """
    Get luffy technique by translation

    See https://api-onepiece.com/documentation/11-luffy-technique for more information

    :param resource: translation of the luffy technique (str) (french translation)
    :return: API list object (with luffy techniques matching the translation search)
    """
    return API("luffy/techniques", "translation", resource)


def luffy_technique_by_gear_id(resource):
    """
    Get luffy technique by gear id

    See https://api-onepiece.com/documentation/11-luffy-technique for more information

    :param resource: id of the gear of the luffy technique (int)
    :return: API list object (with luffy techniques matching the gear id search)
    """
    return API("luffy/techniques", "gear_id", resource)


def count_luffy_techniques():
    """
    Get count of luffy techniques

    See https://api-onepiece.com/documentation/11-luffy-technique for more information

    :return: API unique object (with the count of luffy techniques)
    """
    return API("luffy/techniques", "count")


def locate_by_id(resource):
    """
    Get locate by id

    See https://api-onepiece.com/documentation/16-locate for more information

    :param resource: id of the locate (int)
    :return: API unique object
    """
    return API("locates", "id", resource)


def locate_by_name(resource):
    """
    Get locate by name

    See https://api-onepiece.com/documentation/16-locate for more information

    :param resource: name of the locate (str)
    :return: API list object (with locates matching the name search)
    """
    return API("locates", "name", resource)


def locate_by_sea(resource):
    """
    Get locate by sea

    See https://api-onepiece.com/documentation/16-locate for more information

    :param resource: sea of the locate (str)
    :return: API list object (with locates matching the sea search)
    """
    return API("locates", "sea", resource)


def locate_by_affiliation(resource):
    """
    Get locate by affiliation

    See https://api-onepiece.com/documentation/16-locate for more information

    :param resource: affiliation of the locate (str)
    :return: API list object (with locates matching the affiliation search)
    """
    return API("locates", "affiliation", resource)


def count_locates():
    """
    Get count of locates

    See https://api-onepiece.com/documentation/16-locate for more information

    :return: API unique object (with the count of locates)
    """
    return API("locates", "count")


def fruit_by_id(resource):
    """
    Get fruit by id

    See https://api-onepiece.com/documentation/2-fruit for more information

    :param resource: id of the fruit (int)
    :return: API unique object
    """
    return API("fruits", "id", resource)


def fruit_by_name(resource):
    """
    Get fruit by name

    See https://api-onepiece.com/documentation/2-fruit for more information

    :param resource: name of the fruit (str)
    :return: API list object (with fruits matching the name search)
    """
    return API("fruits", "name", resource)


def fruit_by_type(resource):
    """
    Get fruit by type

    See https://api-onepiece.com/documentation/2-fruit for more information

    :param resource: type of the fruit (str) (paramecia, zoan, zoan mythique, logia)
    :return: API list object (with fruits matching the type search)
    """
    return API("fruits", "type", resource)


def count_fruits():
    """
    Get count of fruits

    See https://api-onepiece.com/documentation/2-fruit for more information

    :return: API unique object (with the count of fruits)
    """
    return API("fruits", "count")


def sword_by_id(resource):
    """
    Get sword by id

    See https://api-onepiece.com/documentation/8-sword for more information

    :param resource: id of the sword (int)
    :return: API unique object
    """
    return API("swords", "id", resource)


def sword_by_name(resource):
    """
    Get sword by name

    See https://api-onepiece.com/documentation/8-sword for more information

    :param resource: name of the sword (str)
    :return: API list object (with swords matching the name search)
    """
    return API("swords", "name", resource)


def count_swords():
    """
    Get count of swords

    See https://api-onepiece.com/documentation/8-sword for more information

    :return: API unique object (with the count of swords)
    """
    return API("swords", "count")


def boat_by_id(resource):
    """
    Get boat by id

    See https://api-onepiece.com/documentation/14-boat for more information

    :param resource: id of the boat (int)
    :return: API unique object
    """
    return API("boats", "id", resource)


def boat_by_name(resource):
    """
    Get boat by name

    See https://api-onepiece.com/documentation/14-boat for more information

    :param resource: name of the boat (str)
    :return: API list object (with boats matching the name search)
    """
    return API("boats", "name", resource)


def boat_by_type(resource):
    """
    Get boat by type

    See https://api-onepiece.com/documentation/14-boat for more information

    :param resource: type of the boat (str) (pirate, gouvernement)
    :return: API list object (with boats matching the type search)
    """
    return API("boats", "type", resource)


def boat_by_crew_id(resource):
    """
    Get boat by crew id

    See https://api-onepiece.com/documentation/14-boat for more information

    :param resource: crew id of the boat (int)
    :return: API list object (with boats matching the crew id search)
    """
    return API("boats", "crew_id", resource)


def boat_by_captain_id(resource):
    """
    Get boat by captain id

    See https://api-onepiece.com/documentation/14-boat for more information

    :param resource: captain id of the boat (int)
    :return: API list object (with boats matching the captain id search)
    """
    return API("boats", "captain_id", resource)


def count_boats():
    """
    Get count of boats

    See https://api-onepiece.com/documentation/14-boat for more information

    :return: API unique object (with the count of boats)
    """
    return API("boats", "count")


def crew_by_id(resource):
    """
    Get crew by id

    See https://api-onepiece.com/documentation/12-crew for more information

    :param resource: id of the crew (int)
    :return: API unique object
    """
    return API("crews", "id", resource)


def crew_by_name(resource):
    """
    Get crew by name

    See https://api-onepiece.com/documentation/12-crew for more information

    :param resource: name of the crew (str)
    :return: API list object (with crews matching the name search)
    """
    return API("crews", "name", resource)


def crew_by_status(resource):
    """
    Get crew by status

    See https://api-onepiece.com/documentation/12-crew for more information

    :param resource: status of the crew (str) (inconnu, actif, inactif)
    :return: API list object (with crews matching the status search)
    """
    return API("crews", "status", resource)


def yonko_crews():
    """
    Get yonko crews

    See https://api-onepiece.com/documentation/12-crew for more information

    :return: API list object (with crews which are yonko)
    """
    return API("crews", "yonko")


def count_crews():
    """
    Get count of crews

    See https://api-onepiece.com/documentation/12-crew for more information

    :return: API unique object (with the count of crews)
    """
    return API("crews", "count")
