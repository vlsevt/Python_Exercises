"""Exam (2023-06-09)."""


def reverse_string_words(text: str) -> str:
    """
    Reverse each 3 letters in words.

    Given a string, from beginning to the end of the string reverse each 3 symbols in a row including spaces.

    reverse_string_words("abc") => "cba"
    reverse_string_words("living in a funny universe") => "vilgnini  a nuf yninureves"
    reverse_string_words("abcde") => "cbaed"
    reverse_string_words("  a") => "a  "
    reverse_string_words("   ") => "   "
    """
    chunks = []
    output_chunks = []
    for i in range(0, len(text), 3):
        chunk = text[i:i+3]
        chunks.append(chunk)
    for i in chunks:
        output_chunks.append(i[::-1])
    return "".join(output_chunks)


def sort_words_len_letters(text: str) -> list:
    """
    Sort words in text by their length and letters accordingly.

    First sort is length.
    Second sort is letters.

    sort_words_len_letters("abc ahsbd asgpba gasg asg asdg asdgasdg") => ['abc', 'asg', 'asdg', 'gasg', 'ahsbd',
                                                                               'asgpba', 'asdgasdg']
    sort_words_len_letters("a b c d e f g") => ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    sort_words_len_letters("g j y o n gf ds e s w bh ol tg") => ['e', 'g', 'j', 'n', 'o', 's', 'w', 'y', 'bh',
                                                                      'ds', 'gf', 'ol', 'tg']
    """
    return sorted(text.split(" "), key=lambda x: (len(x), x))


def find_target_by_two_elements(lst: list, target: int) -> list:
    """
    Find the target with all possible solutions using from 1 to 2 digits from the given list.

    Find every solution of a single digit.
    Find every solution that consists of 2 digits.

    In the result, all the single elements should come before all the two-element pairs.
    The order otherwise should be the same as in the list.

    Function must return a list of lists if any solution presents in given list, as in example:

    find_target_by_two_elements([1, 2, 3, 4, 5, 6, 1, 3], 6) => [[6], [1, 5], [2, 4], [3, 3], [5, 1]]
    find_target_by_two_elements([1, 2], 1) => [[1]]
    find_target_by_two_elements([1, 2, 1], 1) => [[1], [1]]
    find_target_by_two_elements([1, 2], 4) => [] # no solution, just return empty list
    find_target_by_two_elements([], 0) => []
    find_target_by_two_elements([1, 4, 5, 2, 7, 8, 9, 2, 0, 3], 7) => [[7],
                                                                 [4, 3],
                                                                 [5, 2],
                                                                 [5, 2],
                                                                 [7, 0]]
    """
    output_list = []
    for first in lst:
        if first == target:
            output_list.append([first])
    for first in lst:
        copy_list = lst.copy()
        copy_list.remove(first)
        for second in lst:
            if first + second == target and [first, first] not in output_list:
                output_list.append([first, second])
    return output_list


def reverse_string_recursion(text: str) -> str:
    """
    Return a reversed string.

    This function has to be written using recursion!
    reverse_string_recursion("Hello, world!") => "!dlrow ,olleH"
    reverse_string_recursion("abcdefghijklmnopqrstuvwxyz") => "zyxwvutsrqponmlkjihgfedcba"
    reverse_string_recursion("12345") => "54321"
    """
    if text == "":
        return ""
    else:
        return reverse_string_recursion(text[1:]) + text[0]


def char_frequency(text: str) -> list:
    """
    Return a list of tuples, where each tuple represents a character and frequency of it appearance in the text.

    Returning list must be sorted by:
    1) frequency
    2) characters
    """
    frequency_dict = {}

    for char in text:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    frequency_list = [(char, frequency) for char, frequency in frequency_dict.items()]
    sorted_list = sorted(frequency_list, key=lambda x: (x[1], x[0]))

    return sorted_list


def swap_biggest_lowest(text: str) -> str:
    """
    Return a string where the character with the lowest frequency goes first and the character with the highest frequency goes last.

    Characters must be sorted by frequency first and then by character itself.
    Moreover, in the returning string, character with the lowest frequency has to appear amount of time equal
    to the frequency of the character with the highest frequency.
    If the amount of unique characters in the text is not even, then the middle character appears with same frequency as originally.

    swap_biggest_lowest("sxacdysfcvsdrtdftaybatsyrvtaysdvf") => "bbbbbxxxxccccrrrrffffvvvaaaddttys"
    swap_biggest_lowest("CCCBBDA") => "AAADDBC"
    swap_biggest_lowest("ABBCCCDDDDEEEEE") => "AAAAABBBBCCCDDE"
    swap_biggest_lowest(
        "Rare but unique sense of joy while programming :)") => ")))))))):::::RRRbbbfffhhhjjjllppqqttwyagmsinorue "
    swap_biggest_lowest("BCA") => ABC
    swap_biggest_lowest("XXBZZCAYY") => AABBCCXYZ
    swap_biggest_lowest("XXBZZCYY") => BBCCXXYZ
    swap_biggest_lowest("CCCFBBA") => AAAFFBC
    """
    text_to_list = list(text)
    output_text = ""
    new_text = "".join(sorted(text_to_list, key=lambda char: (text.count(char), char), reverse=False))
    unique_text = ""
    for i in new_text:
        if i not in unique_text:
            unique_text += i
    for char in range(len(unique_text)):
        output_text += unique_text[char] * text.count(unique_text[-(char + 1)])
    return output_text


class Food:
    """Food class."""

    def __init__(self, name: str, vitality: float):
        """
        Initialize food.

        Vitality must be private param.(tip: use self.__)
        """
        self.name = name
        self.__vitality = vitality

    def get_vitality(self):
        """Return vitality."""
        return self.__vitality


class Customer:
    """Customer class."""

    def __init__(self, name: str, money: int, hunger: float):
        """
        Initialize customer.

        All parameters are private.(tip: use self.__)
        """
        self.__name = name
        self.__money = money
        self.__hunger = hunger

    def get_money(self):
        """Return money."""
        return self.__money

    def take_money(self, price):
        """Reduce amount of money of a customer."""
        self.__money -= price

    def get_name(self):
        """Return name."""
        return self.__name

    def get_hunger(self):
        """Return hunger."""
        return self.__hunger

    def reduce_hunger(self, food: Food):
        """Reduce hunger of a customer."""
        self.__hunger -= food.get_vitality()

    def eat(self, meal: list):
        """
        Process of eating, means there supposed to be used.

        Reduce_hunger to immediately see the result of eating food.
        Return the re-newed state (self.satisfied()) of a person.
        """
        for food in meal:
            self.reduce_hunger(food)
        return self.satisfied()

    def satisfied(self):
        """
        Return the re-newed state of a person, right after eating food.

        If after eating food:
        hunger >= 1 -> "I am totally satisfied!"
        hunger >= 0.6 -> "I am good."
        any other case -> "I would eat more."
        """
        if self.__hunger >= 1:
            return "I am totally satisfied!"
        elif self.__hunger >= 0.6:
            return "I am good."
        else:
            return "I would eat more."

class McDonalds:
    """McDonalds class."""

    def __init__(self, menu: dict):
        """
        Initialize McDonalds.

        Menu is a private param.(tip: use self.__)
        """
        self.__menu = menu

    def get_menu(self):
        """
        Return menu in following form.

        'Today you can order:
        Meal: Burger that will cost - 4
        Meal: Fries that will cost - 2'
        """
        output_string = ""
        for item in range(len(self.__menu)):
            output_string += f"Meal: {list(self.__menu.keys())[item]} that will cost - {self.__menu[item]}\n"
            output_string.rstrip()
        return output_string

    def order(self, customer: Customer, order: list):
        """
        Check if the order can be processed.

        First check if all the meals in the order are available in the menu.
        Then call the __pay_for_order to check if the overall cost of the order can be paid by a customer.

        NB! If not all the meals from order are in the menu, return -> 'Sorry but we don't have all the meals from your order.'
        """
        if all(item.name in menu for item in order):
            self.__pay_for_order(customer, sum([self.__menu.get(each) for each in order]))
        else:
            return f"Sorry but we don't have all the meals from your order."

    def __pay_for_order(self, customer: Customer, overall_price: int):
        """
        Check if the customer has enough money to pay for the meal.

        If customer has enough money, then take money from customer and return -> 'Enjoy your meal!'
        Else -> 'You need more money.'
        All parameters are restricted.(tip: use self.__)
        """
        if customer.get_money() >= overall_price:
            customer.take_money(overall_price)
            return "Enjoy your meal!"
        else:
            return "You need more money."

class Person:
    """Person class."""

    def __init__(self, name: str, age: int, grades: dict):
        """Initialize Person."""

    def get_grades(self):
        """
        Return the grades.

        Return the grades in the following form:

        'Math: 3
        Engl: 4
        Soci: 5' <- no new line at the end!!!
        """

    def __str__(self):
        """
        Return string representation of a person in following form.

        'Name: Ago
        Age: 18
        Grades: Math: 3
                Engl: 4  <- there is no spacing, same form as in get_grades.
                Soci: 5'
        """


class Student:
    """Student class."""

    def __init__(self, person: Person, year: int):
        """Initialize Student."""


class Pirate:
    """Pirate class."""

    def __init__(self, person: Person, boat: str):
        """Initialize Pirate."""

    def battle_roar(self):
        """Return the roar: 'Yahoho rome&gold'."""


class University:
    """University class."""

    def __init__(self, name: str, requirements: dict):
        """
        Initialize University.

        All the params are private.
        """

    def get_name(self):
        """Return the name of the University."""

    def get_requirements(self):
        """Return the requirements of the University."""

    def get_students(self):
        """Return the students of the University."""

    def register_student(self, person: Person):
        """
        Register student.

        Registers a student if:
        Student is over 18, otherwise -> 'Too young for our gang...'
        Student passes the requirements for the University -> return a string depending on if a person become a pirate or a student.
        """

    def __on_board(self, person: Person):
        """
        Return a battle roar of a newly created Pirate.

        If person passed math for at least 2, then boat of a new pirate is 'Black eye'
        If person passed Engl for at least 2, then boat of a new pirate is 'Language squad'
        Any other case boat of a new pirate is 'Whatever'
        """

    def __check_requirements(self, person: Person):
        """Person passes the check if any 3 subjects from University requirements are passed."""

    def __add_student(self, student: Student):
        """
        Add student to the students.

        Adds student to the students and return:
        'Welcome to the TTU, congratulations Ago', TTU is a name of a University and Ago is a name of a student.
        """

    def __congratulations(self, students: list):
        """
        Congratulate all the students who finished the University.

        'Congratulations our dear students:
        Ago
        Nick
        Jack'
        """

    def next_year(self):
        """
        Update students course.

        Updates students course.
        All the students who were on 3rd course are not updated, but removed from the university and added to the congratulation letter.
        Tip: Use __congratulations().
        If nobody ended the University, return ''.
        """


if __name__ == '__main__':
    assert reverse_string_words("abc") == "cba"
    assert reverse_string_words("living in a funny universe") == "vilgnini  a nuf yninureves"
    assert reverse_string_words("abcde") == "cbaed"
    assert reverse_string_words("  a") == "a  "
    assert reverse_string_words("   ") == "   "

    assert sort_words_len_letters("abc ahsbd asgpba gasg asg asdg asdgasdg") == ['abc', 'asg', 'asdg', 'gasg', 'ahsbd',
                                                                                 'asgpba', 'asdgasdg']
    assert sort_words_len_letters("a b c d e f g") == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    assert sort_words_len_letters("g j y o n gf ds e s w bh ol tg") == ['e', 'g', 'j', 'n', 'o', 's', 'w', 'y', 'bh',
                                                                        'ds', 'gf', 'ol', 'tg']

    assert reverse_string_recursion("Hello, world!") == "!dlrow ,olleH"
    assert reverse_string_recursion("abcdefghijklmnopqrstuvwxyz") == "zyxwvutsrqponmlkjihgfedcba"
    assert reverse_string_recursion("12345") == "54321"

    assert char_frequency("Hello, world!") == [(' ', 1),
                                               ('!', 1),
                                               (',', 1),
                                               ('H', 1),
                                               ('d', 1),
                                               ('e', 1),
                                               ('r', 1),
                                               ('w', 1),
                                               ('o', 2),
                                               ('l', 3)]
    assert char_frequency("racecar") == [('e', 1), ('a', 2), ('c', 2), ('r', 2)]

    assert swap_biggest_lowest("CCCBBDA") == "AAADDBC"
    assert swap_biggest_lowest("ABBCCCDDDDEEEEE") == "AAAAABBBBCCCDDE"
    assert swap_biggest_lowest("sxacdysfcvsdrtdftaybatsyrvtaysdvf") == "bbbbbxxxxccccrrrrffffvvvaaaddttys"

    # mcdonalds
    menu = {
        Food("Burger", 0.3): 4,
        Food("BigMac", 0.5): 7,
        Food("BigTasty", 0.7): 9,
        Food("Cheeseburger", 0.4): 5,
        Food("McChicken", 0.6): 6,
    }
    mc_donalds = McDonalds(menu)
    customer = Customer("Ago", 100, 0.1)
    f_order = [Food("Burger", 0.3)]
    s_order = [Food("BigMac", 0.5)]
    print(mc_donalds.order(customer, f_order))
    assert customer.eat(f_order) == "I would eat more."
    assert customer.get_money() == 96
    assert mc_donalds.order(customer, s_order) == "Enjoy your meal!"
    assert customer.get_money() == 89
    assert customer.eat(s_order) == "I am good."

    # student&pirate
    grades = {'Math': 5, 'Engl': 5, 'Esto': 5}
    person = Person('Ago', 18, grades)
    requirements = {'Math': 4, 'Engl': 3, 'Esto': 4, 'Biol': 5, 'Chem': 4}
    uni = University('TTU', requirements)
    assert uni.register_student(person) == "Welcome to the TTU, congratulations Ago!"
    assert type(uni.get_students()[0]) == Student
    assert uni.next_year() == ""
    assert uni.get_students()[0].year == 2
    assert uni.next_year() == ""
    assert uni.next_year() == "Congratulations our dear students:\nAgo"
    assert len(uni.get_students()) == 0
