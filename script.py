# Project : The Boredless Tourist
# Date    : Sun 14 Jun 2020 05:28:59 AM IST


destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

# Retrieve the index of the traveler
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

# Retrieve the index of test traveler by matching with destinations
def get_traveler_location(traveler):
    traveler_destination       = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

# Empty list for every destination in destinations
attractions = [[] for destination in destinations]

# Add attraction to the list attraction from destination
def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
    except ValueError:
        return
    attractions_for_destinations = attractions[destination_index]
    attractions_for_destinations.append(attraction)
    return attractions_for_destinations

# Add more attraction to the list
add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# Find attractions according to intrests
def find_attractions(destination, interests):
    destination_index        = get_destination_index(destination)
    attractions_in_city      = attractions[destination_index]
    attractions_with_intrest = []
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags     = attraction[1]
        for intrest in interests:
            if attraction_tags.count(intrest):
                attractions_with_intrest.append(possible_attraction[0])
    return attractions_with_intrest

