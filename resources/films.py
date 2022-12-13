from resources.base import ResourceBase
from utils.fetch_data import fetch_data


class Films(ResourceBase):
    """
    Resource class plural
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/films/"  # plural
        self.__films_range = [1, 6]

    @property
    def relative_url(self):
        return self.__relative_url

    @property
    def range(self):
        return self.__films_range

    # def films_range(self, start, end):
    #     self.__films_range = [start, end]

    @range.setter
    def range(self, new_range):
        start, end = new_range
        self.__films_range = [start, end]

    def get_count(self):
        plural_films_url = self.home_url + self.relative_url
        response = fetch_data(plural_films_url)
        return response.get("count")

    def get_resource_urls(self):
        resource_url = self.home_url + self.relative_url
        return resource_url

    def get_sample_data(self, id_="1"):
        sample_url = self.get_resource_urls() + id_
        return fetch_data(sample_url)


# f = Films()
# print(f.films_range)
# f.films_range = 2, 10
# print(f.films_range)
