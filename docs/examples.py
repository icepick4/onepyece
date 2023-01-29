import onepyece as op

# Find all Yonko crews
yonkos = op.yonko_crews()

for yonko in yonkos:
    print(f"{yonko.french_name} : {yonko.status}")
    # Get all characters from the Yonko crew
    characters = op.character_by_crew_id(yonko.id)
    for character in characters:
        print(f"{character.french_name} : {character.job}")

# Get a precise character
luffy = op.character_by_id(1)
print(f"{luffy.french_name} : {luffy.job}")

# Get locates by a search term
# Note that all functions with "by_name" in their name 
# return a list if the search term is not precise
locates = op.locate_by_name("Archipel")

# I can now discover all locates that contain the search term "Archipel"
for locate in locates:
    print(f"{locate.french_name}")

# Get implicit count of all characters for a precise crew
# Note that every multiple result query has a count attribute
# You can also use the len() function
print(op.character_by_crew_id(1).count)
print(len(op.character_by_crew_id(1)))

# Get explicit count of all fruits
print(op.count_fruits())







