# Project : The Boredless Tourist
# Date    : Sun 14 Jun 2020 05:28:59 AM IST


destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

# Retrieve the index of the traveler
def get_destination(destination):
    destination_index = destinations.index(destination)
    return destination_index

# Retrieve the index of test traveler by matching with destinations
def get_traveler_location(traveler):
    traveler_destination       = traveler[1]
    traveler_destination_index = get_destination(traveler_destination)
    return traveler_destination_index
