"""

TODO

1. pull data for the movie "A New Hope"

2. Replace the data for each of the endpoint listed in the JSON object
 and insert that data into respective database tables
 (using following instructions)

    (For example - "A New Hope" has following resource endpoints)
        - characters
        - planets
        - vehicles
        - starships
        - species

3. Convert height and weight in each character to standard units

4. You have to remove all cross-referencing URLs from each resource

"""

from pprint import pprint
from resources.films import Films
from utils.fetch_data import fetch_data


if __name__ == "__main__":
    # pull data for the movie "A New Hope"
    film_data = Films().get_sample_data()
    pprint(film_data)

    # Replace the data for each of the endpoint listed in the JSON object
    #  and insert that data into respective database tables

    # fetching urls of each resource in film_1
    charlist = film_data.get("characters")
    planetlist = film_data.get("planets")
    specieslist = film_data.get("species")
    starshipslist = film_data.get("starships")
    vehiclelist = film_data.get("vehicles")

    # fetching data for each resource endpoint from film_1
    char_data = [fetch_data(char) for char in charlist]
    planet_data = [fetch_data(planet) for planet in planetlist]
    species_data = [fetch_data(species) for species in specieslist]
    starship_data = [fetch_data(starship) for starship in starshipslist]
    vehicle_data = [fetch_data(vehicle) for vehicle in vehiclelist]



