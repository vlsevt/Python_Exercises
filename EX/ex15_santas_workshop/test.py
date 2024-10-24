"""File for testing purposes."""


import pytest
from main import World, Child, Gift, Retrieve, read_data_from_url


URLS = ['https://iti0102-2020.pages.taltech.ee/info/files/ex15_nice_list.csv', 'https://iti0102-2020.pages.taltech.ee/info/files/ex15_naughty_list.csv']
WISH_LIST = 'https://iti0102-2020.pages.taltech.ee/info/files/ex15_wish_list.csv'


def test_write_data_to_list_nice():
    """Test."""
    world = World()
    world.write_data_to_list(URLS[0])
    assert world.people is not []


def test_write_data_to_list_naughty():
    """Test."""
    world = World()
    world.write_data_to_list(URLS[1])
    assert world.people is not []


def test_write_data_to_list_error():
    """Test."""
    world = World()
    with pytest.raises(Exception, match='Input must be in URL format.'):
        world.write_data_to_list([])
        world.write_data_to_list(1235)
        world.write_data_to_list('hello world')


def test_add_gifts_to_children_nice():
    """Test."""
    world = World()
    world.write_data_to_list(URLS[0])
    world.add_gifts_to_children(WISH_LIST)
    assert 0 != len(world.people[2].gifts)
    assert 0 != len(world.people[40].gifts)


def test_add_gifts_to_children_naughty():
    """Test."""
    world = World()
    world.write_data_to_list(URLS[1])
    world.add_gifts_to_children(WISH_LIST)
    assert world.people[4].gifts == []
    assert world.people[20].gifts == []


def test_add_gifts_to_children_error():
    """Test."""
    world = World()
    world.write_data_to_list(URLS[0])
    with pytest.raises(Exception, match='Wish List cannot be anything else but list.'):
        world.add_gifts_to_children([])
        world.add_gifts_to_children(1234)
        world.add_gifts_to_children('hello world')


def test_read_data_from_url():
    """Test."""
    assert read_data_from_url(URLS[0]) is not None
    assert read_data_from_url(URLS[1]) is not None


def test_read_data_from_url_error():
    """Test."""
    assert None is read_data_from_url('')
    assert None is read_data_from_url(None)


def test_request_data_no_spaces():
    """Test."""
    crayons = Retrieve('Crayons')
    assert 'gift' in crayons.request_data()


def test_request_data_one_space():
    """Test."""
    toy_truck = Retrieve('Toy truck')
    assert 'gift' in toy_truck.request_data()


def test_request_data_multiple_spaces():
    """Test."""
    very_long_name = Retrieve('Magic: The Gathering Commander Legends booster box')
    assert 'gift' in very_long_name.request_data()


def test_request_data_error():
    """Test."""
    toy_error = Retrieve('toy')
    flippers_error = Retrieve('flippers')
    assert 'gift' not in toy_error.request_data()
    assert 'gift' not in flippers_error.request_data()


def test_set_info():
    """Test."""
    plushie = Gift('Polar bear plushie')
    plushie.set_info()
    assert 15 == plushie.cost
    assert 2 == plushie.production_time
    assert 200 == plushie.weight


def test_present_with_no_info():
    """Test."""
    gwent = Gift('Gwent')
    gwent.set_info()
    assert None is gwent.cost
    assert None is gwent.production_time
    assert None is gwent.weight


def test_add_presents_one_present():
    """Test."""
    wishes = read_data_from_url(WISH_LIST)
    ben = Child('Ben', 'Australia', False)
    ben.add_presents(wishes)
    assert 'Polar bear plushie' == ben.gifts[0].name


def test_add_presents_multiple_presents():
    """Test."""
    wishes = read_data_from_url(WISH_LIST)
    libby = Child('Libby', 'United Kingdom', False)
    libby.add_presents(wishes)
    assert 3 == len(libby.gifts)


def test_add_presents_nice():
    """Test."""
    wishes = read_data_from_url(WISH_LIST)
    maria = Child('Maria', 'Canada', False)
    maria.add_presents(wishes)
    assert 2 == len(maria.gifts)


def test_add_presents_naughty():
    """Test."""
    wishes = read_data_from_url(WISH_LIST)
    felix = Child('Felix', 'Estonia', True)
    felix.add_presents(wishes)
    assert 0 == len(felix.gifts)
