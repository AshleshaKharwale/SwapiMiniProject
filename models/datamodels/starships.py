from models.basemodel import Base
from typing import List, Union
from pprint import pprint


class Starships(Base):
    name: str
    model: str
    manufacturer: str
    cost_in_credits: Union[int, str]
    length: Union[int, float, str]
    max_atmosphering_speed: Union[int, str]
    crew: Union[int, str]
    passengers: Union[int, str]
    cargo_capacity: int
    consumables: str
    hyperdrive_rating: float
    MGLT: int
    starship_class: str
    pilots: List[str]
    films: List[str]


if __name__ == "__main__":
    star_data = {
        "name": "CR90 corvette",
        "model": "CR90 corvette",
        "manufacturer": "Corellian Engineering Corporation",
        "cost_in_credits": "3500000",
        "length": "150",
        "max_atmosphering_speed": "950",
        "crew": "30-165",
        "passengers": "600",
        "cargo_capacity": "3000000",
        "consumables": "1 year",
        "hyperdrive_rating": "2.0",
        "MGLT": "60",
        "starship_class": "corvette",
        "pilots": [],
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/6/"
        ],
        "created": "2014-12-10T14:20:33.369000Z",
        "edited": "2014-12-20T21:23:49.867000Z",
        "url": "https://swapi.dev/api/starships/2/"
    }

    star_obj = Starships(**star_data)
    pprint(dict(star_obj))
