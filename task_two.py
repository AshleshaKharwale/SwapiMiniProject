from typing import List
from utils.fetch_data import fetch_data

film1_url = "https://swapi.dev/api/films/1"


def write_output_to_file(filename: str, output: str) -> None:
    """
    Writes output to the existing file. If file doesn't exist, creates a file.
    :param filename: name of a file
    :param output: Data to write to a file
    :return: None
    """
    with open(filename, "w") as f:
        f.write(output)


def get_names(urls: List[str]) -> List[str]:
    """
    Extracts name from each url's json data and stores in list.
    Returns the list of names of each resource from film1.
    :param urls: list of urls of resources
    :return: list of names of each resource
    """
    names = []
    # [fetch_data(url).get('name') for url in urls]   - using list comprehension
    # list(map(lambda x: fetch_data(x).get('name'), urls))  - using higher order function map
    for url in urls:
        details = fetch_data(url)
        names.append(details.get('name'))  # extracting name from all details
    return names


def get_film_title(url: str) -> str:
    """
    Returns title of film1
    :param url: url of film1
    :return: title of film1
    """
    details = fetch_data(url)
    return details.get('title')


def do_task_two() -> None:
    """
    Gets names of characters, planets and vehicles from film1 and prints them.
    """
    data = fetch_data(film1_url)  # details of film1
    characters = data.get('characters')  # characters in film1
    planets = data.get('planets')  # planets in film1
    vehicles = data.get('vehicles')  # vehicles in film1

    print(f" Title of the film - {get_film_title(film1_url)}")
    print(f" Characters in the film - \n {get_names(characters)}")
    print(f" Planets in the film - \n {get_names(planets)}")
    print(f" Vehicles in the film - \n {get_names(vehicles)}")
