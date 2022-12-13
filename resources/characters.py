from resources.base import ResourceBase
from utils.fetch_data import fetch_data


class Characters(ResourceBase):
    """
    Resource class plural
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/people/"  # plural
        self.__character_range = [1, 82]

    @property
    def relative_url(self):
        return self.__relative_url

    @property
    def range(self):
        return self.__character_range

    @range.setter
    def range(self, new_range):
        start, end = new_range[0], new_range[1]
        self.__character_range = [start, end]

    def get_count(self):
        plural_character_url = self.home_url+self.relative_url  # plural
        response = fetch_data(plural_character_url)
        return response.get("count")

    def get_resource_urls(self):
        resource_url = self.home_url + self.relative_url
        return resource_url

    def get_sample_data(self, id_="1"):
        sample_url = self.get_resource_urls() + id_
        return fetch_data(sample_url)


# c = Characters()
# print(c.get_resource_urls())
# print(c.range)
# c.range = [2,10]
# print(c.range)