"""Exam5 (2023-01-14)."""


def count_camel_case_words(text: str) -> int:
    """
    Count the words in the text.

    The text uses camel case. There are no spaces between words.
    Each new word starts with a capital letter.
    The first word can start with a small or a capital letter.

    count_camel_case_words("hello") => 1
    count_camel_case_words("") => 0
    count_camel_case_words("helloWorld") => 2
    count_camel_case_words("HelloWorld") => 2
    count_camel_case_words("aBC") => 3
    count_camel_case_words("ABC") => 3
    count_camel_case_words("a") => 1
    count_camel_case_words("What") => 1
    """
    pass


def odd_index_sum(nums: list) -> int:
    """
    Find sum of elements with odd indices.

    odd_index_sum([1, 2, 3]) => 2
    odd_index_sum([]) => 0
    odd_index_sum([1]) => 0
    odd_index_sum([2, 3]) => 3
    odd_index_sum([0, -1, -4, -3]) => -4
    odd_index_sum([0, -1, -4, -3, 6, 7]) => 3
    """
    pass


def prettify_string(input_string: str) -> str:
    """
    Prettify string.

    - After every punctuation (,.!?:;-) there should be at least one space.
    - Every sentence should start with an uppercase letter.
    - Sentence starts after .!?
    - Also in the beginning of the string a new sentence starts

    There are no consecutive punctuation in the input string.

    Examples:
    "Hello,I am the input of this function.please make me pretty!" => "Hello, I am the input of this function. Please
    make me pretty!"
    "there should be space after me-and also space after me;next sentence should be capitalized! i need to be capitalized but
    no new space should be added." => "There should be space after me- and also space after me; next sentence should be capitalized! I need to be capitalized but
    no new space should be added."
    """
    output_string = ""
    for i in range(len(input_string)):
        if not input_string[i].isdigit() and not input_string[i].isalpha():


    input_string.replace(".", ". ")
    input_string.replace(",", ", ")
    input_string.replace("!", "! ")
    input_string.replace("?", "? ")
    input_string.replace(":", "; ")
    input_string.replace("-", "- ")
    input_string.replace("  ", " ")


print(prettify_string("there should be space after me-and also space after me;next sentence should be capitalized! i need to be capitalized but no new space should be added."))
def get_max_nums(nums: list) -> list:
    """
    Return list with maximum numbers from the original list.

    print(get_max_nums([1, 2, 34, 4, 5, 34, 34])) => [34, 34, 34]
    print(get_max_nums([-1, -1, -1, -1, -1, -6])) => [-1, -1, -1, -1, -1]
    print(get_max_nums([3, 4, 5, 6, 3])) => [6]
    print(get_max_nums([6])) => [6]
    print(get_max_nums([])) => []

    :param nums: list of integers.
    :return: list of maximum numbers from the original list.
    """
    pass


def mirror_ends(s: str) -> str:
    """
    Return the first non-matching symbol pair from both ends.

    The function has to be recursive. No loops allowed!

    Starting from the beginning and end, find the first symbol pair which does not match.
    If the input string is a palindrome (the same in reverse) then return "" (empty string).

    mirror_ends("abc") => "ac"
    mirror_ends("aba") => ""
    mirror_ends("abca") => "bc"
    mirror_ends("abAAca") => "bc"
    mirror_ends("") => ""
    """
    pass


def invert_repetitions(s: str) -> str:
    """
    Remove repeated characters and repeat single characters.

    Repeated character (2 or more consecutive same characters) has to be replaced with single character.

    Easier option: repeat single characters twice. (gives 60% points)

    Harder option: add 1 additional character each time you need to repeat the same char.
    "abbabba" => "aabaaabaaaa"
    The first time "a" becomes "aa", the second time it becomes "aaa", and then "aaaa" etc.

    Result of empty string is also empty string.

    Examples:
    '' -> ''
    'a' -> 'aa'
    'aa' -> 'a'
    'aaaaaaa' -> 'a'
    'bc' -> 'bbcc'
    'bcc' -> 'bbc'
    'bbc' -> 'bcc'
    'bbcbcc' -> 'bccbbc'
    'kloo' -> 'kkllo'
    'ababbab' -> 'aabbaabaabb' (easier) or 'aabbaaabaaaabbb' (harder)
    """
    pass


class Car:
    """Represent car model."""

    def __init__(self, color: str, make: str, engine_size: int):
        """
        Initialize car.

        :param color: car color
        :param make: car make
        :param engine_size: car engine size
        """
        self.color = color
        self.make = make
        self.engine_size = engine_size


class Service:
    """Represent car service model."""

    def __init__(self, name: str, max_car_num: int):
        """
        Initialize service.

        Car service should also have a database to keep and track all cars standing in queue for repair.
        :param name: service name
        :param max_car_num: max car number service can take for repair at one time
        """
        pass

    def can_add_to_service_queue(self, car: Car) -> bool:
        """
        Check if it is possible to add car to service queue.

        Car can be added if:
        1. after adding new car, total car number in service does not exceed max_car_number (allowed car number in service)
        2. there is no car with the same color and make present in this service (yes, this world works this way).

        If car can be added, return True. Otherwise return False.
        """
        pass

    def add_car_to_service_queue(self, car: Car):
        """
        Add car to service if it is possible.

        The function does not return anything.
        """
        pass

    def get_service_cars(self) -> list:
        """Get all cars is service."""
        pass

    def repair(self) -> Car:
        """
        Repair car in service queue.

        Normally, the first car in queue is repaired.
        However, if there is a car in queue which color + make characters length is exactly 13 ->
        this car is chosen and is repaired (might be multiple suitable cars -> choose any).
        After the repair, car is no longer in queue (is removed).
        :return: chosen and repaired car
        """
        pass

    def get_the_car_with_the_biggest_engine(self) -> list:
        """
        Return a list of cars (car) with the biggest engine size.

        :return: car (cars) with the biggest engine size
        """
        pass


class Species(Enum):
    """Different species."""

    Dragon = 1
    Vampire = 2
    Beast = 3


class Monster:
    """Monster class."""

    def __init__(self, species: Species, bounty: int):
        """Initialize monster."""
        pass

    def get_species(self) -> Species:
        """Return the species of the monster."""
        pass

    def get_bounty(self) -> int:
        """Return the bounty for this monster."""
        pass

    def is_alive(self) -> bool:
        """Whether the monster is alive."""
        pass

    def slay(self) -> bool:
        """
        Slay the monster.

        If monster is already dead, return False.
        Otherwise kill the monster and return True.
        """
        pass

    def __repr__(self) -> str:
        """
        Return string representation.

        "A {species} worth {bounty} coins"
        """
        pass


class Village:
    """
    Village class.

    Village starts with 100 money and 0 age.
    Each day population is lowered by 1 for each monster in the village.
    Population cannot be lower than 0.
    If the population is 0, witcher cannot work there.
    """

    def __init__(self, name: str, initial_population: int):
        """Initialize village."""
        pass

    def get_name(self) -> str:
        """Return name of the village."""
        pass

    def get_population(self) -> int:
        """Return population of the village."""
        pass

    def get_monsters(self) -> list:
        """
        Return a list of monsters bothering the village.

        If there are no population, no monsters are not bothering the village.
        """
        pass

    def add_monster(self, monster: Monster) -> None:
        """Add monster to the village."""
        pass

    def add_money(self, amount) -> None:
        """Add money to the village."""
        pass

    def advance_day(self) -> None:
        """
        Advance time by one day.

        The age of the village is increased by one.
        """
        pass

    def pay(self, amount: int) -> bool:
        """
        Pay the required amount.

        If the village does not have enough money, return False.
        Otherwise spend the amount and return True.
        """
        pass

    def __repr__(self) -> str:
        """
        Return string representation of the village.

        "{name}, population {population}, age {age}"
        """
        pass


class Witcher:
    """
    Witcher class.

    Witcher starts with 0 money.
    """

    def __init__(self, name: str, school: str):
        """Initialize witcher."""
        pass

    def get_money(self) -> int:
        """Return the amount of money the witcher has."""
        pass

    def get_slain(self) -> list:
        """Return a list of slain monsters in the order they are slain."""
        pass

    def get_hunted_species(self) -> list:
        """
        Return a list of Species objects of the slain monsters ordered alphabetically.

        Each value should be in the list once, so there can be max 3 objects in the result.
        """
        pass

    def hunt_most_expensive(self, village: Village) -> bool:
        """
        Hunt the most expensive monster.

        Try to hunt the most expensive monster (the one who has the highest bounty) in the given village.
        The monster is slain and then the village tries to pay the witcher.
        If there is a monster to kill and the village can pay the money, return True.
        Otherwise return False.
        The monster is slain even if there is no money to pay.
        """
        pass

    def __repr__(self) -> str:
        """
        Return string representation.

        "{name} of {school} school with {number of monsters} monsters slain"
        """
        pass


if __name__ == '__main__':
    assert count_camel_case_words("") == 0
    assert count_camel_case_words("helloWorld") == 2
    assert count_camel_case_words("ABC") == 3

    assert odd_index_sum([]) == 0
    assert odd_index_sum([1]) == 0
    assert odd_index_sum([1, 2]) == 2
    assert odd_index_sum([1, 2, 4, 3]) == 5

    assert prettify_string("Hello,I am the input of this function.please make me pretty!") \
           == "Hello, I am the input of this function. Please make me pretty!"

    assert get_max_nums([1, 2, 3]) == [3]
    assert get_max_nums([]) == []
    assert get_max_nums([1, 2, 34, 4, 5, 34, 34]) == [34, 34, 34]

    assert mirror_ends("abc") == "ac"
    assert mirror_ends("abca") == "bc"
    assert mirror_ends("abcba") == ""

    assert invert_repetitions("") == ""
    assert invert_repetitions("a") == "aa"
    assert invert_repetitions("aa") == "a"
    assert invert_repetitions("11122") == "12"
    assert invert_repetitions("aabaab") == "abbabb"

    # Car service

    car = Car("blue", "honda", 1800)
    service = Service("autoLUX", 5)

    print(service.can_add_to_service_queue(car))  # True
    service.add_car_to_service_queue(car)
    print(service.get_service_cars())  # [car]

    car2 = Car("blue", "honda", 1500)

    print(service.can_add_to_service_queue(
        car2))  # False; since there is already car in service with the same make and color

    # Witcher
    tallinn = Village("Tallinn", 7)
    godzilla_species = Species.Beast
    godzilla = Monster(godzilla_species, 200)
    print(godzilla.get_species() == Species.Beast)  # True
    print(str(godzilla.get_species()))  # Species.Beast
    modzilla = Monster(Species.Dragon, 200)
    dracula = Monster(Species.Vampire, 100)
    frankenstein = Monster(Species.Beast, 300)
    tallinn.add_monster(godzilla)
    tallinn.add_monster(modzilla)
    tallinn.add_monster(dracula)
    tallinn.add_monster(frankenstein)

    print(tallinn.get_population())  # 7
    tallinn.advance_day()
    tallinn.add_money(500)
    print(tallinn.get_population())  # 3
    ago = Witcher("Ago", "TalTech")
    print(ago.hunt_most_expensive(tallinn))  # True
    print(ago.get_money())  # 300
    print(tallinn.get_monsters())  # [A Beast worth 200 coins, A Dragon worth 200 coins, A Vampire worth 100 coins]
    print(ago.hunt_most_expensive(tallinn))  # True
    print(ago.get_money())  # 500
    print(tallinn.get_monsters())  # [A Dragon worth 200 coins, A Vampire worth 100 coins]
    print(ago.hunt_most_expensive(tallinn))  # False
    print(ago.get_money())  # 500
    print(ago.hunt_most_expensive(tallinn))  # True
    print(tallinn.get_monsters())  # []

    print(ago.get_hunted_species())  # [<Species.Beast: 3>, <Species.Dragon: 1>, <Species.Vampire: 2>]
    print(ago.get_hunted_species()[0] == Species.Beast)  # True

    # enum examples
    species_list = [Species.Beast, Species.Vampire, Species.Beast]
    print(species_list[0] == species_list[1])  # False
    print(species_list[0] == species_list[2])  # True
