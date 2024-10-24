"""Santa workshop."""

import codecs
import csv
from pathlib import Path
import urllib.parse
from urllib.request import urlopen
import requests

URLS = ['https://iti0102-2020.pages.taltech.ee/info/files/ex15_nice_list.csv', 'https://iti0102-2020.pages.taltech.ee/info/files/ex15_naughty_list.csv']
WISH_LIST = 'https://iti0102-2020.pages.taltech.ee/info/files/ex15_wish_list.csv'


def read_data_from_url(url: str) -> list:
    """Read csv from file and return the reader."""
    if not url:
        return None

    result = []
    response = urlopen(url)
    reader = csv.reader(codecs.iterdecode(response, 'utf-8'))

    for row in reader:
        result += [[cell for cell in row]]
    return result


class Gift:
    """Present."""

    def __init__(self, name: str):
        """Init."""
        self.name = name.lstrip(' ')
        self.cost = None
        self.production_time = None
        self.weight = None

    def __repr__(self):
        """Represent."""
        return f'{self.name}'

    def set_info(self):
        """Set gift info."""
        response = Retrieve(self.name).request_data()
        if 'material_cost' in response.keys():
            self.cost = response['material_cost']
            self.production_time = response['production_time']
            self.weight = response['weight_in_grams']


class Retrieve:
    """Get data from API."""

    def __init__(self, gift_name: str):
        """Init."""
        self.gift_name = urllib.parse.quote(gift_name)
        self.api_link = 'https://cs.ttu.ee/services/xmas/gift?name='

    def request_data(self):
        """Request data."""
        gift_url = self.api_link + self.gift_name
        return requests.get(gift_url).json()


class Child:
    """Child class."""

    def __init__(self, name: str, country: str, naughty: bool):
        """Init."""
        self.name = name
        self.country = country
        self.naughty = naughty
        self.gifts = []

    def __repr__(self):
        """Represent the kid."""
        return f'{"Naughty" if self.naughty else "Nice"} {self.name} in {self.country} got {self.gifts}\n'

    def add_presents(self, wish_list: list):
        """Add presents."""
        gifts = list(filter(lambda x: x[0] == self.name, wish_list))[0][1:] if self.naughty is False else None
        if gifts is not None:
            for gift in gifts:
                gift_object = Gift(gift)
                gift_object.set_info()
                self.gifts += [gift_object]


def read_naughty_list() -> list[Child]:
    """Read naughty list."""
    with open(Path('data', 'ex15_naughty_list.csv')) as naughty_file:
        reader = csv.reader(naughty_file, delimiter=',', skipinitialspace=True)
        return [Child(name, country, True) for name, country in reader]


def read_nice_list() -> list[Child]:
    """Read nice list."""
    with open(Path('data', 'ex15_nice_list.csv')) as nice_file:
        reader = csv.reader(nice_file, delimiter=',', skipinitialspace=True)
        return [Child(name, country, False) for name, country in reader]


def read_wish_list() -> dict[Child]:
    """Read the wish list."""
    # Read the list of nice children
    nice_children = read_nice_list()
    # Read the list of naughty children
    naughty_children = read_naughty_list()

    # Create a dictionary of children
    children_by_name = {}
    for child in nice_children + naughty_children:
        children_by_name[child.name] = child

    with open(Path('data', 'ex15_wish_list.csv')) as wish_file:
        reader = csv.reader(wish_file, delimiter=',', skipinitialspace=True)
        children = {}
        for name, *gift in reader:
            # Check if the child is in the list of nice children
            if name in children_by_name:
                children[name] = gift
        return children


class World:
    """World class."""

    def __init__(self):
        """Init."""
        self.people = []

    def write_data_to_list(self, url):
        """Add people to list."""
        if not url or type(url) is not str or 'http' not in url:
            raise Exception('Input must be in URL format.')

        data = read_data_from_url(url)
        naughty = False if 'nice' in url else True
        for n in data:
            child = Child(n[0], n[1], naughty)
            self.people += [child]

    def add_gifts_to_children(self, wish_list: str):
        """Add gifts to child."""
        if not wish_list or type(wish_list) is not str or 'http' not in wish_list:
            raise Exception('Wish List cannot be anything else but list.')
        wishes = read_data_from_url(wish_list)

        for child in self.people:
            child.add_presents(wishes)
