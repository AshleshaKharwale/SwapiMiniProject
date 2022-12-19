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
from multiprocessing.pool import ThreadPool
from resources.films import Films
from utils.fetch_data import fetch_data
from models.datamodels.films import Films as Films_
from dal.sample import get_db_conn


if __name__ == "__main__":
    # pull data for the movie "A New Hope"
    film_data = Films().get_sample_data()
    film_data = Films_(**film_data)
    # pprint(film_data)

    # Replace the data for each of the endpoint listed in the JSON object
    #  and insert that data into respective database tables

    # fetching urls of each resource in film_1
    charlist = film_data.characters
    # planetlist = film_data.get("planets")
    # specieslist = film_data.get("species")
    # starshipslist = film_data.get("starships")
    # vehiclelist = film_data.get("vehicles")

    # fetching data for each resource endpoint from film_1
    pool = ThreadPool(10)
    char_data = pool.map(fetch_data, charlist)
    # planet_data = [fetch_data(planet) for planet in planetlist]
    # species_data = [fetch_data(species) for species in specieslist]
    # starship_data = [fetch_data(starship) for starship in starshipslist]
    # vehicle_data = [fetch_data(vehicle) for vehicle in vehiclelist]

    def remove_cross_reference(all_data_set):
        data = []
        for data_set in all_data_set:
            new_data = data_set.copy()
            for key, value in data_set.items():
                if isinstance(value, list):
                    new_data.pop(key)
            data.append(new_data)
        return data

    char_data = remove_cross_reference(char_data)
    # planet_data = remove_cross_reference(planet_data)
    # vehicle_data = remove_cross_reference(vehicle_data)
    # species_data = remove_cross_reference(species_data)
    # starship_data = remove_cross_reference(starship_data)

    def insert_into_table(table_name, data):
        with get_db_conn() as conn:
            cursor = conn.cursor()
            return cursor.execute(f"insert into {table_name} values ({data})")

    pprint(char_data)
    print(insert_into_table("characters", char_data))

