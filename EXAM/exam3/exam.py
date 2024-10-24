"""Exam3 (2023-01-10)."""
from typing import Optional

def split_string_into_ints(numbers: str) -> list:
    """
    Return list of integers from comma-separated string of integers.

    split_string_into_ints("1,2") => [1, 2]
    split_string_into_ints("") => []
    split_string_into_ints("0") => [0]
    split_string_into_ints("-1,-2,3") => [-1, -2, 3]
    """
    pass


def repeat_multiples(numbers: list) -> list:
    """
    Repeat every element divisible by 2 twice, and every element divisible by 3 three times.

    The element which is divisible by 2 and 3 should be repeated 4 times.

    repeat_multiples([1, 2, 3]) => [1, 2, 2, 3, 3, 3]
    repeat_multiples([1, 5, 7]) => [1, 5, 7]
    repeat_multiples([22, 33]) => [22, 22, 33, 33, 33]
    repeat_multiples([]) => []
    repeat_multiples([6]) => [6, 6, 6, 6]
    repeat_multiples([0, 2, 9]) => [0, 0, 0, 0, 2, 2, 9, 9, 9]
    """
    pass


def count_double_chars(s: str) -> int:
    """
    Count only double symbols.

    Count how many double symbols are in the text. You have to only count pairs.
    Therefore, a pair of symbols which is not preceded or followed by the same symbol.
    If there are three or more of the same symbol, then this is not a pair and doesn't count.
    Any printable symbol counts (letters, digits, punctuation, space etc.).

    assert count_double_chars("abc") == 0
    assert count_double_chars("aabc") == 1
    assert count_double_chars("aaabc") == 0  # (three "a"-s doesn't count)
    assert count_double_chars("aaaabc") == 0  # (four "a"-s also doesn't count)
    assert count_double_chars("aabbc") == 2
    assert count_double_chars("") == 0
    assert count_double_chars("abbcdd") == 2
    assert count_double_chars("aabbaa") == 3
    assert count_double_chars(",,!?") == 1
    assert count_double_chars("a  b  =") == 2
    """
    pass


def reverse_list(input_strings: list) -> list:
    """
    Reverse the list and elements except for "python" and "java" and everything between.

    Given list of strings, return new reversed list where each list element is
    reversed too. Do not reverse strings followed after element "python". If element is "java" -
    reverse mode is on again.
    P.S - "python" and "java" are not being reversed

    reverse_list(['apple', 'banana', 'onion']) -> ['noino', 'ananab', 'elppa']
    reverse_list(['lollipop', 'python', 'candy']) -> ['candy', 'python', 'popillol']
    reverse_list(['sky', 'python', 'candy', 'java', 'fly']) -> ['ylf', 'java', 'candy', 'python', 'yks']
    reverse_list(['sky', 'python', 'java', 'candy']) -> ['ydnac', 'java', 'python', 'yks']

    :param input_strings: list of strings
    :return: reversed list
    """
    pass


def substring(s: str, count: int) -> str:
    """
    Return first part of string with length of count.

    #06

    Function should be recursive, loops (for/while) are not allowed!
    count <= len(string)

    assert substring("hello", 2) == "he"
    assert substring("hi", 2) == "hi"
    assert substring("house", -1) == ""
    assert substring("house", 0) == ""

    :param s: input string.
    :param count: int, count <= len(string).
    :return: first count symbols from string.
    """
    pass


def plot_the_tangerines(integers: list[int]) -> str:
    """
    Create a bar graph with non-negative numbers.

    Recently you have noticed that your consumption of tangerines is too high.
    You want to monitor the situation so you try to make a bar graph of tangerines consumption in Excel.
    But Excel won't work, because you have just started using Linux.
    Oh well, it seems that you have to make your own program to plot graphs and do fancy calculations.

    Graph consists of scale (left) and stack of '#'s that represent integer in the list (consumed tangerines in a day).
    0 means stack of 0 '#', 1 means stack of 1 '#', 2 means stack of 2 '#' and so on.

    Graph max height should be the maximum value from the list, max is always at least 1.
    There is always at least one element in the list.
    Graph needs to be in a frame consisting of '|', '-' and '+' characters as shown in examples.
    There should be no newlines before or after the graph.


    plot_the_tangerines([1, 0, 2, 3, 4, 5, 4, 3, 2, 1, 0, 3, 2, 1]) =>
     +--------------+
    5|     #        |
    4|    ###       |
    3|   #####   #  |
    2|  #######  ## |
    1|# ######## ###|
    0+--------------+

    plot_the_tangerines([0]) =>
     +-+
    1+ +
    0+-+

    plot_the_tangerines([0, 0, 0, 0, 0, 0])) =>
     +------+
    1|      |
    0+------+

    plot_the_tangerines([1, 4, 5, 3, 1]) =>
     +-----+
    5|  #  |
    4| ##  |
    3| ### |
    2| ### |
    1|#####|
    0+-----+

    In case the maximum value is is more than 9, the left side should be wider, aligned to right:

       +-----
    100|
     99|
     ....
      9|#
      8|#
      ...
      0+-----
    """
    pass


class Student:
    """Represent student model."""

    def __init__(self, name: str, gpa: float, age: int):
        """
        Initialize student.

        Each student has name and gpa (Grade Point Average).

        :param name: student's name
        :param gpa: student's gpa
        :param age: student's age
        """
        self.age = age
        self.gpa = gpa
        self.name = name


class University:
    """Represent university model."""

    def __init__(self, name: str, gpa_required: float):
        """
        Initialize university.

        Each university has name and gpa_required.

        University should also have a database to keep and track all students.
        :param name: university name
        :param gpa_required: university required gpa
        """
        pass

    def can_enroll_student(self, student: Student) -> bool:
        """
        Check if student can be enrolled to university.

        Student can be successfully enrolled if:
            * he/she has required gpa (>=)
            * he/she is not already enrolled to this university
            * he/she is at least 16 years old
            * additionally, if student's name characters length is
            exactly 13 -> student can be added to university despite gpa (though still should not be
            already present in university and be younger)
        If the student cannot be enrolled, returns False. Otherwise returns True.

        :return: bool
        """
        pass

    def enroll_student(self, student: Student):
        """
        Enroll new student to university if possible.

        Before enrolling, you have to check whether student can be enrolled.

        :param student: Student
        Function does not return anything
        """
        pass

    def can_unenroll_student(self, student: Student) -> bool:
        """
        Check if student can leave from university.

        Student can be successfully leave if he/she actually studies in this university.

        Returns True, if the student can be unenrolled, False otherwise.

        :return: bool
        """
        pass

    def unenroll_student(self, student: Student):
        """
        Unenroll student from University if possible.

        Before unenrolling, you have to make sure the student can be unenrolled.
        Function does not return anything
        """
        pass

    def get_students(self) -> list:
        """
        Return a list of all students in current university.

        :return: list of Student objects
        """
        pass

    def get_student_highest_gpa(self) -> list:
        """
        Return a list of students (student) with the highest gpa.

        :return: list of Student objects
        """
        pass


class ComputerPart:
    """A computer part."""

    def __init__(self, name: str, cost: float):
        """
        Initialize computer part.

        Each computer part has a name and a cost.
        """
        pass

    def get_cost(self) -> float:
        """Return the cost of the computer part."""
        pass

    def __repr__(self) -> str:
        """Return the name of the computer part."""
        pass


class Computer:
    """A computer at an internet cafe."""

    def __init__(self, name: str, total_parts_needed: int):
        """
        Initialize computer.

        Each computer has name and the amount of parts required for it to function.

        A computer should also keep track of all the parts that are in it.
        :param name: computer name
        :param total_parts_needed: the amount of parts needed for the computer to function
        """
        pass

    def add_part(self, part: ComputerPart):
        """
        Add a part to the computer.

        The parts cost is also added to the computers cost.

        The part is not added if the computer is already working.
        """
        pass

    def get_parts_needed(self) -> int:
        """
        Return the amount of parts that is needed to fully build this computer.

        If the computer needs a total of 3 parts and currently has 1 part, this should return 2.
        """
        pass

    def is_working(self) -> bool:
        """Return if the computer has the correct amount of parts."""
        pass

    def get_parts(self) -> list[ComputerPart]:
        """
        Return a list of all parts that are in the computer.

        Parts should be in the same order as they were added.
        """
        pass

    def get_cost(self) -> float:
        """Return the cost of the computer."""
        pass

    def __repr__(self) -> str:
        """
        Return string representation of Computer.

        Returns string in form "A {name} for {cost}€ with {parts}"

        All the parts should be seperated with ", ".
        Parts should be in the same order as they were added.
        If there are no parts in the computer, there should be "nothing".
        Cost is always shown with 2 decimal places.

        Examples:
        "A hardcore gaming computer for 540.30€ with gtx1070, r5 2600, CX650F, EV860"
        "A pc for 0.00€ with nothing"
        """
        pass


class Customer:
    """A customer at an internet cafe."""

    def __init__(self, name: str, money: float):
        """
        Initialize customer.

        Each customer must have a name, money and it should also keep track of owned computers.
        """
        pass

    def can_buy_computer(self, computer: Computer) -> bool:
        """Return if this customer has enough money to buy a computer."""
        pass

    def buy_computer(self, computer: Computer) -> bool:
        """
        Buy a computer if it can be done.

        This customer loses money equal to the cost of the computer.

        Returns True or False whether the computer was bought.
        """
        pass

    def get_computers(self) -> list[Computer]:
        """Return all computers owned by this customer."""
        pass

    def __repr__(self) -> str:
        """
        Return string representation of a customer.

        Should be in format:
        "{name} with {money}€
        {computer1}
        {computer2}
        {computer3}
        ..."

        The money is always shown with 2 decimal places.

        example1:
        "Laura with 666.00€
        A hardcore gaming computer for 540.30€ with gtx1070, r5 2600, CX650F, EV860
        A pc for 0.00€ with nothing"

        example2:
        "Karl with 0.00€"
        """
        pass


class ComputerStore:
    """A store where people can buy computers."""

    def __init__(self):
        """Initialize computer store."""
        pass

    def add_computer(self, computer: Computer):
        """Add a computer to the store."""
        pass

    def add_part(self, part: ComputerPart):
        """Add a computer part to the storage of the store."""
        pass

    def get_computers(self) -> list[Computer]:
        """Return all computers in the stores as a list."""
        pass

    def get_parts(self) -> list[ComputerPart]:
        """Return all unused computer parts in the store."""
        pass

    def get_working_computers(self) -> list[Computer]:
        """Return all computers which are working."""
        pass

    def build_computer(self) -> Optional[Computer]:
        """
        Make the store build a computer.

        If the store has no non-functioning computers, return None.

        The store looks at the computer which have the least amount of parts missing.
        If two computers have the same amount of parts missing, then the store picks the one that is cheaper.
        (there aren't any cases where computers parts missing and costs are equal)

        example:
        computer1 costs 100 and 3 parts missing
        computer2 costs 300 and 3 parts missing
        computer3 costs 50 and 4 parts missing
        computer4 costs 10 and 0 parts missing (it is already functional)
        The store chooses to build computer1!

        If the store doesnt have enough spare parts to build a computer, return None.

        The store adds the cheapest available parts to the computer until it is built.

        If the computer is built successfully, return the built computer. Else return None.
        """
        pass

    def sell_customer_computer(self, customer: Customer):
        """
        Sell computer to customer.

        A customer walks into the store and wants the most expensive working computer that can be bought with their money.

        Note that the sold computer must work.

        If there are no such computers, the store tries to build a new computer.

        If a computer is successfully built and it is cheap enough to buy, then the customer buys that computer.
        """
        pass


if __name__ == '__main__':
    assert split_string_into_ints("1,2") == [1, 2]
    assert split_string_into_ints("") == []
    assert split_string_into_ints("-1,0") == [-1, 0]

    assert repeat_multiples([1, 2, 3]) == [1, 2, 2, 3, 3, 3]
    assert repeat_multiples([0, 1]) == [0, 0, 0, 0, 1]

    assert count_double_chars("abc") == 0
    assert count_double_chars("aabc") == 1
    assert count_double_chars("aaabc") == 0  # (three "a"-s doesn't count)
    assert count_double_chars("aaaabc") == 0  # (four "a"-s also doesn't count)
    assert count_double_chars("aabbc") == 2

    assert reverse_list(['apple', 'banana', 'onion']) == ['noino', 'ananab', 'elppa']
    assert reverse_list(['lollipop', 'python', 'candy']) == ['candy', 'python', 'popillol']
    assert reverse_list(['sky', 'python', 'candy', 'java', 'fly']) == ['ylf', 'java', 'candy', 'python', 'yks']

    assert substring("hello", 2) == "he"
    assert substring("hello", -1) == ""
    assert substring("", 0) == ""
    assert substring("world", 5) == "world"

    plot = plot_the_tangerines([0, 0, 0, 0, 0, 0])
    print(plot)
    assert plot == " +------+\n1|      |\n0+------+"

    plot = plot_the_tangerines([0, 2, 1, 3])
    print(plot)
    assert plot == " +----+\n" \
                   "3|   #|\n" \
                   "2| # #|\n" \
                   "1| ###|\n" \
                   "0+----+"

    # with high number, there are enough spaces in front
    plot = plot_the_tangerines([100, 0, 0, 0, 0, 0])
    print(plot)
    assert plot.startswith("   +------+\n100|#")

    # university
    university = University("taltech", 60)
    student = Student("Bob", 61, 18)
    print(university.can_enroll_student(student))  # True
    print(university.can_unenroll_student(student))  # False; student is not yet in university

    university.enroll_student(student)
    print(university.get_students())  # [student]
    print(university.get_student_highest_gpa())  # [student]; since this student is the only one

    print(university.can_unenroll_student(student))  # True
    university.unenroll_student(student)
    print(university.get_students())  # []

    # Start of OOP2 ComputerStore
    computer1 = Computer("pc", 3)
    computer1.add_part(ComputerPart("cpu", 200))
    computer1.add_part(ComputerPart("mobo", 60.5))
    computer1.add_part(ComputerPart("case", 70))

    assert computer1.get_cost() == 330.5
    assert computer1.is_working() is True

    computer2 = Computer("laptop", 3)
    computer2.add_part(ComputerPart("display", 160))
    computer2.add_part(ComputerPart("keyboard", 20))

    assert repr(computer2) == "A laptop for 180.00€ with display, keyboard"
    assert computer2.is_working() is False

    store = ComputerStore()
    store.add_part(ComputerPart("mousepad", 36))
    store.add_computer(computer1)
    store.add_computer(computer2)

    assert len(store.get_computers()) == 2  # 2 computers are in the store
    assert len(store.get_working_computers()) == 1  # 1 computer is working

    store.build_computer()  # add mousepad to laptop

    assert len(store.get_working_computers()) == 2  # both computers are working now

    laura = Customer("Laura", 1000)

    store.sell_customer_computer(laura)  # sell pc to laura

    assert len(store.get_computers()) == 1  # only laptop left in store
    assert repr(laura) == "Laura with 669.50€\nA pc for 330.50€ with cpu, mobo, case"  # Laura has a pc now