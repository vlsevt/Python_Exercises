"""Exam0."""
from typing import Optional, Any


def find_capital_letters(s: str) -> str:
    """
    Return only capital letters from the string.

    #1

    If there are no capital letters, return empty string.
    The string contains only latin letters (a-z and A-Z).
    The letters should be in the same order as they appear in the input string.

    find_capital_letters("ABC") => "ABC"
    find_capital_letters("abc") => ""
    find_capital_letters("aAbBc") => "AB"
    """
    new_string = ""
    for i in s:
        if i.islower():
            continue
        else:
            new_string += i
    return new_string


def close_far(a: int, b: int, c: int) -> bool:
    """
    Return if one value is "close" and other is "far".

    #2

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """
    if abs(a - b) <= 1 and abs(c - a) >= 2 and abs(c - b) >= 2 or abs(a - c) <= 1 and abs(b - a) >= 2 and abs(
            b - c) >= 2:
        return True
    else:
        return False


def get_names_from_results(results_string: str, min_result: int) -> list:
    """
    Given a string of names and scores, return a list of names where the score is higher than or equal to min_result.

    #3

    Results are separated by comma (,). Result contains a score and optionally a name.
    Score is integer, name can have several names separated by single space.
    Name part can also contain numbers and other symbols (except for comma).
    Return only the names which have the score higher or equal than min_result.
    The order of the result should be the same as in input string.

    get_names_from_results("ago 123,peeter 11", 0) => ["ago", "peeter"]
    get_names_from_results("ago 123,peeter 11,33", 10) => ["ago", "peeter"]  # 33 does not have the name
    get_names_from_results("ago 123,peeter 11", 100) => ["ago"]
    get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11) => ["ago", "peeter",  "kitty11!!"]
    get_names_from_results("ago 123,peeter 11,kusti riin 14", 12) => ["ago", "kusti riin"]
    """
    list_of_students_who_passed = []
    list_of_students = results_string.split(",")
    for i in list_of_students:
        if len(i.split(" ")) >= 2 and i.split(" ")[-1].isnumeric():
            if int(i.split(" ")[-1]) >= min_result:
                list_of_students_who_passed.append(" ".join(i.split(" ")[:-1]))
        else:
            continue
    return list_of_students_who_passed


def tic_tac_toe(game: list) -> int:
    """
    Find game winner.

    #4

    The 3x3 table is represented as a list of 3 rows, each row has 3 element (ints).
    The value can be 1 (player 1), 2 (player 2) or 0 (empty).
    The winner is the player who gets 3 of her pieces in a row, column or diagonal.

    There is only one winner or draw. You don't have to validate whether the game is in correct (possible) state.
    I.e. the game could have four 1s and one 0 etc.

    tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]) => 1
    tic_tac_toe([[1, 0, 1], [2, 1, 2], [2, 2, 0]]) => 0
    tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]]) => 2

    :param game
    :return: winning player id
    """
    for row in game:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return row[0]

    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col] and game[0][col] != 0:
            return game[0][col]

    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != 0:
        return game[0][0]
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] != 0:
        return game[0][2]

    return 0


def rainbows(field: str) -> int:
    """
    Count rainbows.

    #5

    Function has to be recursive.

    assert rainbows("rainbowThisIsJustSomeNoise") == 1  # Lisaks vikerkaarele on veel sümboleid
    assert rainbows("WoBniar") == 1  # Vikerkaar on tagurpidi ja sisaldab suuri tähti
    assert rainbows("rainbowobniar") == 1  # Kaks vikerkaart jagavad tähte seega üks neist ei ole valiidne

    :param field: string to search rainbows from
    :return: number of rainbows in the string
    """
    if not field:
        return 0
    if "rainbow" in field.lower():
        return 1 + rainbows(field.lower().replace("rainbow", "", 1))
    elif "rainbow" in field.lower()[::-1]:
        return 1 + rainbows(field.lower()[::-1].replace("rainbow", "", 1))
    else:
        return 0


def longest_substring(text: str) -> str:
    """
    Find the longest substring.

    #6

    Substring may not contain any character twice.
    CAPS and lower case chars are the same (a == A)
    In output, the case (whether lower- or uppercase) should remain.
    If multiple substrings have same length, choose first one.

    aaa -> a
    abc -> abc
    abccba -> abc
    babcdEFghij -> abcdEFghij
    abBcd => Bcd
    '' -> ''
    """
    char_lower_list = []
    char_list = []
    for char in text:
        if char.lower() not in char_lower_list:
            char_lower_list.append(char.lower())
            char_list.append(char)
    return "".join(char_list)


print(longest_substring("babcdEFghij"))


class Student:
    """Student class."""

    def __init__(self, name: str, average_grade: float, credit_points: int):
        """Initialize student."""
        self.credit_points = credit_points
        self.average_grade = average_grade
        self.name = name


def average_grade(grades: list):
    """Count an average grade."""
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0


def create_student(name: str, grades: list, credit_points: int) -> Student:
    """
    Create a new student where average grade is the average of the grades in the list.

    Round the average grade up to three decimal places.
    If the list of grades is empty, the average grade will be 0.
    """
    if not grades:
        return Student(name, 0, credit_points)
    else:
        return Student(name, average_grade(grades), credit_points)


def get_top_student_with_credit_points(students: list[Student], min_credit_points: int):
    students_list = []
    for student in students:
        if student.credit_points >= min_credit_points:
            students_list.append(student)
    if not students_list:
        return None
    return sorted(students_list, key=lambda grade: student.average_grade)[0]


def add_result_to_student(student: Student, grades_count: int, new_grade: int, credit_points) -> Student:
    new_sum = student.average_grade * grades_count
    new_average = (new_sum + new_grade) / (grades_count + 1)
    return Student(student.name, round(new_average, 3), student.credit_points + credit_points)


def get_ordered_students(students: list[Student]) -> list:
    return sorted(students, key=lambda student: (student.credit_points, student.average_grade, student.name),
                  reverse=True)


class Room:
    """Room."""

    def __init__(self, number: int, price: int):
        """Initialize room."""
        self.number = number
        self.price = price
        self.features = []
        self.booked = False

    def add_feature(self, feature: str) -> bool:
        """
        Add a feature to the room.

        Do not add the feature and return False if:
        - the room already has that feature
        - the room is booked.
        Otherwise, add the feature to the room and return True
        """
        if feature in self.features:
            return False
        if self.booked:
            return False
        self.features.append(feature)
        return True

    def get_features(self) -> list:
        """Return all the features of the room."""
        return self.features

    def get_price(self) -> int:
        """Return the price."""
        return self.price

    def get_number(self) -> int:
        """Return the room number."""
        return self.number


class Hotel:
    """Hotel."""

    def __init__(self):
        """Initialize hotel."""
        self.rooms = []

    def add_room(self, room: Room) -> bool:
        """
        Add room to hotel.

        If a room with the given number already exists, do not add a room and return False.
        Otherwise, add the room to hotel and return True.
        """
        if room not in self.rooms:
            self.rooms.append(room)
            return True
        else:
            return False

    def book_room(self, required_features: list) -> tuple[int, Any, Any] | None:
        """
        Book an available room which has the most matching features.

        Find a room which has most of the required features.
        If there are several with the same amount of matching features, return the one with the smallest room number.
        If there is no available rooms, return None
        """
        available_rooms = []
        for room in self.rooms:
            if not room.booked:
                matching_features = set(room.features) & set(required_features)
                available_rooms.append((len(matching_features), room.number, room))
        if not available_rooms:
            return None
        available_rooms = sorted(available_rooms, key=lambda available_room: (-available_room[0], available_room[1]))
        available_rooms[0][2].booked = True
        return available_rooms[0][2]

    def get_available_rooms(self) -> list:
        """Return a list of available (not booked) rooms."""
        return [room for room in self.rooms if not room.booked]

    def get_rooms(self) -> list:
        """Return all the rooms (both booked and available)."""
        return self.rooms

    def get_booked_rooms(self) -> list:
        """Return all the booked rooms."""
        return [room for room in self.rooms if room.booked]

    def get_feature_profits(self) -> dict:
        """
        Return a dict where key is a feature and value is the total price for the booked rooms which have the feature.

        Example:
            room1, price=100, features=a, b, c
            room2, price=200, features=b, c, d
            room3, price=400, features=a, c

        all the rooms are booked
        result:
        {
        'a': 500,
        'b': 300,
        'c': 700,
        'd': 200
        }
        """
        features_counter = {}
        for room in self.rooms:
            for feature in room.features:
                features_counter[feature] += room.price
        return features_counter

    def get_most_profitable_feature(self) -> Optional[str]:
        """
        Return the feature which profits the most.

        Use get_feature_profits() method to get the total price for every feature.
        Return the feature which has the highest value (profit).
        If there are several with the same max value, return the feature which is alphabetically lower (a < z)
        If there are no features booked, return None.
        """
        return sorted(self.get_feature_profits(), key=lambda feature: (-self.get_feature_profits().values(), self.get_feature_profits().keys()))[0]


if __name__ == '__main__':
    hotel = Hotel()
    room1 = Room(1, 100)
    room1.add_feature("tv")
    room1.add_feature("bed")
    room2 = Room(2, 200)
    room2.add_feature("tv")
    room2.add_feature("sauna")
    hotel.add_room(room1)
    hotel.add_room(room2)
    # TODO: try to add room with existing number, try to add existing feature to room
    assert hotel.get_rooms() == [room1, room2]
    assert hotel.get_booked_rooms() == []

    assert hotel.book_room(["tv", "president"]) == room1
    assert hotel.get_available_rooms() == [room2]
    assert hotel.get_booked_rooms() == [room1]

    assert hotel.book_room([]) == room2
    assert hotel.get_available_rooms() == []

    assert hotel.get_feature_profits() == {
        'tv': 300,
        'bed': 100,
        'sauna': 200
    }
    assert hotel.get_most_profitable_feature() == 'tv'

    # TODO: try to add a room so that two or more features have the same profit
