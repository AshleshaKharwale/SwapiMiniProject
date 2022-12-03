from utils.randgen import RandomCharacters
from utils.fetch_data import fetch_data

home_url = "https://swapi.dev"  # swapi website url
relative_url = "/api/people/{0}"  # magic string


def do_task_one():
    """
    Get details of 15 random characters in range [1,82]
    """
    for character in RandomCharacters():  # generating random character numbers from
        # 'RandomCharacters' generator
        absolute_url = home_url + relative_url.format(character)  # creating url for
        # each character in RandomCharacters() generator
        print(fetch_data(absolute_url))  # getting all details from character url
        print("------" * 24)
