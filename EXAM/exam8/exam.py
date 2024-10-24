"""Exam8 (2023-05-20)."""
import random


def sum_of_nonadjacent_even_numbers(lst: list) -> int:
    """
    Find the sum of even numbers inside the list which stay separately from other even numbers.

    sum_of_nonadjacent_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) => 30
    sum_of_nonadjacent_even_numbers([1, 2]) => 2
    sum_of_nonadjacent_even_numbers([1, 2, 3]) => 2
    sum_of_nonadjacent_even_numbers([1, 2, 4]) => 0
    sum_of_nonadjacent_even_numbers([1, 2, 4, 6]) => 0
    sum_of_nonadjacent_even_numbers([1, 2, 3, 4]) => 6
    sum_of_nonadjacent_even_numbers([1, 3, 5, 7, 9]) => 0
    sum_of_nonadjacent_even_numbers([2, 4, 6, 8, 10]) => 0
    """
    previous_num = 1
    current_sum = 0

    for num in range(len(lst) - 1):
        if previous_num % 2 != 0 and lst[num] % 2 == 0 and lst[num + 1] % 2 != 0:
            current_sum += lst[num]
        previous_num = lst[num]
    if lst[-1] % 2 == 0 and lst[-2] % 2 != 0:
        current_sum += lst[-1]
    return current_sum

    # even_sum = 0
    # is_prev_even = False
    # is_cur_even = False
    # is_next_even = False
    # nxt = 0
    # for (cur, nxt) in itertools.pairwise(lst):
    #     is_cur_even = cur % 2 == 0
    #     is_next_even = nxt % 2 == 0
    #
    #     if not is_prev_even and is_cur_even and not is_next_even:
    #         even_sum += cur
    #
    #     is_prev_even = is_cur_even
    # else:
    #     if not is_cur_even and is_next_even:
    #         even_sum += nxt
    #
    # return even_sum


def most_vowels_in_string(text: str) -> int:
    """
    Find the most frequent vowel in the text.

    most_vowels_in_string('aaeeiioouu') => 2
    most_vowels_in_string('abcabcedgiut') => 2
    most_vowels_in_string('aaaaaeui') => 5
    most_vowels_in_string('') => 0
    most_vowels_in_string('    ') => 0
    """
    text = text.lower()
    return max(text.count('a'), text.count('e'), text.count('i'), text.count('o'), text.count('u'))


def sum_of_digits(text: str) -> int:
    """
    Find the sum of the integers inside the text.

    Text can contain positive and negative integers from 0-9.
    First integer is always positive, so text always begins as: "1+...", "0-...".
    Must be done using recursion!!!

    sum_of_digits('1+2+3+4+5') => 15 - 1 + (2 + (3 + (4 + (5))))
    sum_of_digits('1+2+3-4-5') => -3
    sum_of_digits('1-2-3-4-5') => -13 - 1 - (2 - (3 -(4 - (5))))
    recursion:
    base case - return num - no operators - 1 len
    recurse case - return num operator recurse - even len > 1
    """
    if text == '':
        return 0
    elif text[0].isdigit():
        return int(text[0]) + sum_of_digits(text[1:])
    elif text[0] == '-':
        return -int(text[1]) + sum_of_digits(text[2:])
    elif text[0] == '+':
        return int(text[1]) + sum_of_digits(text[2:])


def euclid_game(text: str) -> str:
    """
    Find the winner of the euclid's game.

    Take string of form: "25 7".
    Each move, subtract maximum multiple of lesser number from greater number.
    If after move one of numbers become 0, the player who made this move is returned as a winner.

    euclid_game("25 7") => "Gert"
    euclid_game("10000000 3") => "Gert"
    euclid_game("1 1") => "Ago"
    """
    ago, gert = [int(i) for i in text.split(" ")]
    while ago != 0 and gert != 0:
        if ago >= gert:
            ago -= gert * (ago // gert)
        else:
            gert -= ago * (gert // ago)
    return "Ago" if gert else "Gert"


def sort_numbers(text: str) -> str:
    """
    Find all the odd and even numbers inside the text.

    Return the string where first written all the odd numbers sorted in ascending order, then even numbers also in ascending order.

    sort_numbers("12345") => "133355555224444"
    sort_numbers("1329574") => "1333555557777777999999999224444"
    sort_numbers("1223") => "13332222"
    sort_numbers("     ") => ""
    sort_numbers("") => ""
    """
    if not all(char.isdigit() for char in text):
        return ""
    odds = []
    evens = []
    for i in text:
        n = int(i)
        if n % 2 == 0:
            for num in range(n):
                evens.append(i)
        else:
            for num in range(n):
                odds.append(i)
    return "".join(sorted(odds)) + "".join(sorted(evens))


def find_sum_pairs(lst: list, target: int) -> list:
    """
    Find 2 digits in list that sum up to target.

    Given a list of digits, you have to search through list and find
    minimal and maximal digits that sum up to target.

    find_sum_pairs([1, 2, 3, 4, 5], 6) => [1, 5], answer [2, 4] is not accepted
    find_sum_pairs([2, 1, 1, 3, 2, 5], 4) => [1, 3]
    find_sum_pairs([1, 3, 5, 7, 9], 12) => [3, 9]
    find_sum_pairs([2, 3, 1, 2, 3, 4, 5], 6) => [1, 5]
    """
    pairs = []
    for first in lst:
        copy_list = lst.copy()
        copy_list.remove(first)
        for second in copy_list:
            if first + second == target:
                pairs.append([first, second])

    if pairs:
        return sorted(sorted(pairs, key=lambda x: abs(x[0] - x[1]), reverse=True)[0])
    else:
        return []


class Fruit:
    """Fruit."""

    def __init__(self, name, points):
        """
        Initialize fruit.

        :param name: name of a fruit
        :param points: points for fruit
        """
        self.name = name
        self.points = points

    def fruit_info(self):
        """
        Return fruit info as follows.

        Name: Avocado | Points: 100
        """
        return f"Name: {self.name} | Points: {self.points}"


class Player:
    """Player."""

    def __init__(self, name: str):
        """
        Initialize player.

        :param name: name of a player
        :param cut_fruits: fruits cut during the game
        :param score: score for the cut fruits
        """
        self.__name = name
        self.__cut_fruits = []
        self.__score = 0

    def add_cut_fruit(self, fruit: Fruit):
        """
        Add to the cut_fruits a fruit that was cut.

        Update the score of a player in this function as well using __update_score() function.
        """
        self.__cut_fruits.append(fruit)
        self.__update_score(fruit)

    def __update_score(self, fruit: Fruit):
        """Update players score."""
        self.__score += fruit.points

    def get_score(self):
        """Return the score of a player."""
        return self.__score

    def get_info(self):
        """
        Return players info as follows.

        "Name: Ago
        Score: 100"
        """
        return f"Name: {self.__name}\nScore: {self.__score}"


class Client:
    """Client."""

    def __init__(self, name, age, gender, annual_income):
        """
        Initialize client.

        :param name: str
        :param age: int
        :param gender: str
        :param annual_income: int
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.annual_income = annual_income

    def get_client_info(self):
        """
        Return information about the client in following order.

        "Name: Ago
        Age: 30
        Gender: Male
        Annual Income: 60000"
        """
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nAnnual Income: {self.annual_income}"


class BankAccount:
    """BankAccount."""

    def __init__(self, client, account_number, balance=0):
        """
        Initialize bank account.

        :param client: client
        :param account_number: str, must consist of 5 char!
        :param balance: int
        """
        self.__client = client
        self.account_number = account_number
        self.__balance = balance

    def get_client(self):
        """Return the client."""
        return self.__client

    def get_balance(self):
        """Return the balance."""
        return self.__balance

    def deposit(self, amount):
        """
        Return message after successful deposit.

        "Deposited 100 successfully. Current balance: 1100"
        """
        self.__balance = self.__balance + amount
        return f"Deposited {amount} successfully. Current balance: {self.__balance}"

    def withdraw(self, amount):
        """
        Return message after successful or not withdrawal.

        successful -> "Withdrawn 100 successfully. Current balance: 1000"
        not successful -> "Insufficient balance"
        """
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawn {amount} successfully. Current balance: {self.__balance}"
        else:
            return f"Insufficient balance"

    def check_balance(self):
        """
        Return message that represents balance state.

        "Current balance: 1000"
        """
        return f"Current balance: {self.__balance}"

    def account_info(self):
        """
        Return message that represents account state.

        "Name: Ago
        Account number: 12345
        Balance: 1000"
        """
        this_client = self.get_client()
        return f"Name: {this_client.name}\nAccount number: {self.account_number}\nBalance: {self.__balance}"


class Bank:
    """Bank."""

    def __init__(self, name: str):
        """
        Initialize bank.

        :param name: str
        :param accounts: list
        """
        self.name = name
        self.__accounts = []

    def register_client(self, client: Client):
        """
        Register a client if.

        1) it's age above or equal to 18.
        2) it's balance have sufficient amount of annual income to pay a register fee equal to 100 euro.
        so, when a new client is registered, instantly 100 euros must be withdrawn from its account.
        successful registration -> "Registration was successful!"
        not successful registration, due to lack of annual income -> "Registration was not successful, due to lack of annual income!"
        not successful registration, due to age shortage -> "Registration was not successful, due to age shortage!"
        """
        if client.age < 18:
            return "Registration was not successful, due to age shortage!"
        elif client.annual_income < 100:
            return "Registration was not successful, due to lack of annual income!"
        else:
            self.__create_new_account(client)
            return "Registration was successful!"

    def __create_new_account(self, client: Client):
        """Create a random account_number and return a new BankAccount."""
        new_account = BankAccount(client, random.randint(10000, 99999), client.annual_income)
        new_account.withdraw(100)
        self.__accounts.append(new_account)
        return new_account

    def get_accounts(self):
        """Return accounts as list."""
        return self.__accounts

    def get_bank_info(self):
        """
        Return information about bank, it's name and amount of customers in the following form.

        "Name: SEB
        Amount of accounts: 100"
        """
        return f"Name: {self.name}\nAmount of accounts: {len(self.__accounts)}"


def find_the_richest_person(bank: Bank) -> str:
    """
    Find the richest person.

    Given a Bank, find the richest person in this Bank and return its client information.

    find_the_richest_person(Bank) ->
    "Name: Ago
    Age: 18
    Gender: Male
    Annual Income: 50000"
    """
    account_list = bank.get_accounts()
    return sorted(account_list, key=lambda person: person.get_balance(), reverse=True)[0].get_client().get_client_info()


def find_the_poorest_person(bank: Bank) -> str:
    """
    Find the poorest person.

    Given a Bank, find the poorest person in this Bank and return its client information.

    find_the_poorest_person(Bank) ->
    "Name: Ago
    Age: 18
    Gender: Male
    Annual Income: 1000"
    """
    account_list = bank.get_accounts()
    return sorted(account_list, key=lambda person: person.get_balance())[0].get_client().get_client_info()


if __name__ == '__main__':
    # sum_of_nonadjacent_even_numbers
    assert sum_of_nonadjacent_even_numbers([2, 1]) == 2
    assert sum_of_nonadjacent_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
    assert sum_of_nonadjacent_even_numbers([1, 2]) == 2
    assert sum_of_nonadjacent_even_numbers([1, 2, 3]) == 2
    assert sum_of_nonadjacent_even_numbers([1, 2, 4]) == 0
    assert sum_of_nonadjacent_even_numbers([1, 2, 4, 6]) == 0
    assert sum_of_nonadjacent_even_numbers([1, 2, 3, 4]) == 6
    assert sum_of_nonadjacent_even_numbers([1, 3, 5, 7, 9]) == 0
    assert sum_of_nonadjacent_even_numbers([2, 4, 6, 8, 10]) == 0

    # most_vowels_in_string
    assert most_vowels_in_string('aaeeiioouu') == 2
    assert most_vowels_in_string('abcabcedgiut') == 2
    assert most_vowels_in_string('aaaaaeui') == 5
    assert most_vowels_in_string('') == 0
    assert most_vowels_in_string('    ') == 0

    # sum_of_digits
    assert sum_of_digits('1+2+3+4+5') == 15
    assert sum_of_digits('1+2+3-4-5') == -3
    assert sum_of_digits('1-2-3-4-5') == -13

    # euclid_game

    assert euclid_game("25 7") == "Gert"
    assert euclid_game("10000000 3") == "Gert"
    assert euclid_game("1 1") == "Ago"

    # sort_numbers
    assert sort_numbers("12345") == "133355555224444"
    assert sort_numbers("1329574") == "1333555557777777999999999224444"
    assert sort_numbers("1223") == "13332222"
    assert sort_numbers("     ") == ""
    assert sort_numbers("") == ""

    # find_sum_pairs
    assert find_sum_pairs([1, 2, 3, 4, 5], 6) == [1, 5]
    assert find_sum_pairs([2, 1, 1, 3, 2, 5], 4) == [1, 3]
    assert find_sum_pairs([1, 3, 5, 7, 9], 12) == [3, 9]
    assert find_sum_pairs([2, 3, 1, 2, 3, 4, 5], 6) == [1, 5]

    # fruit ninja
    player1 = Player("John")
    orange = Fruit("Orange", 20)
    banana = Fruit("Banana", 5)
    grapefruit = Fruit("Grapefruit", 15)
    bad_fruit = Fruit("Bad Fruit", -10)
    player1.add_cut_fruit(banana)
    player1.add_cut_fruit(orange)
    player1.add_cut_fruit(grapefruit)
    player1.add_cut_fruit(bad_fruit)
    player1.get_score()  # 30
    player1.get_info()
    # Name: John
    # Score: 30

    # Client
    test_client = Client("Ago", 30, "Male", 1000000)
    print(test_client.get_client_info())
    # Name: Ago
    # Age: 30
    # Gender: Male
    # Annual Income: 1000000

    # Bank/BankAccount
    test_bank = Bank("Seb")
    print(test_bank.get_accounts())  # []
    print(test_bank.get_bank_info())
    # Name: Seb
    # Amount of accounts: 0
    print(test_bank.register_client(test_client))  # "Registration was successful!"
    print(test_bank.get_bank_info())
    # Name: Seb
    # Amount of accounts: 1
    test_bank_account = test_bank.get_accounts()[-1]
    print(test_bank_account.deposit(100))  # Deposited 100 successfully. Current balance: 1000000
    print(test_bank_account.withdraw(1000000))  # Withdrawn 1000000 successfully. Current balance: 0
    print(test_bank_account.withdraw(1000000))  # Insufficient balance3
    print(test_bank_account.check_balance())  # Current balance: 0
    print(test_bank_account.account_info())
    # Name: Ago
    # Account number: '5 digits!'
    # Balance: 0
    print(len(test_bank_account.account_info().split("\n")[1].split(": ")[1]))  # 5

    # richest/poorest
    test_bank = Bank("SEB")
    test_clients = [
        Client("Ago", 18, "Male", 50000),
        Client("Gert", 19, "Male", 40000),
        Client("Heisenberg", 20, "Male", 30000),
        Client("Eren", 21, "Male", 20000),
        Client("Levi", 22, "Male", 10000)
    ]
    for client in test_clients:
        test_bank.register_client(client)
    print(find_the_richest_person(test_bank))
    # Name: Ago
    # Age: 18
    # Gender: Male
    # Annual Income: 50000
    print(find_the_poorest_person(test_bank))
    # Name: Levi
    # Age: 22
    # Gender: Male
    # Annual Income: 10000
