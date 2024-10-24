"""Exam 10 (2023-06-13)."""


def double_char(original_string: str) -> str:
    """
    Return a string where every char in the original string is doubled.

    double_char("a") => "aa"
    double_char("ab") => "aabb"
    double_char("aa ") => "aaaa  "
    double_char("") => ""

    :param original_string: string
    :return: string where chars are doubled
    """
    output_string = ""
    for i in original_string:
        output_string += i * 2
    return output_string


def sort_numbers_as_reversed_strings(lst: list) -> list:
    """
    Sort given list by the numbers as reversed strings.

    sort_numbers_as_reversed_strings([10, 1, 34, 15, 47, 96, 24, 63, 22]) => [10, 1, 22, 63, 24, 34, 15, 96, 47]
    if you remove each first digits in numbers in return list, you can notice that we have: [0, 1, 2, 3, 4, 5, 6, 7]
    sort_numbers_as_reversed_strings([0, 21, 32, 13, 4, 55, 6]) => [0, 21, 32, 13, 4, 55, 6]
    """
    return sorted(lst, key=lambda x: str(x)[::-1])


def find_multiples(start: int, end: int, div: int, skip: int) -> list:
    """
    Find all the numbers from start to end, INCLUDING THE END, accordingly to the following rules.

    Each number added to the return list supposed to be divisible by div.
    During iteration skip exactly 'skip' amount of iterations.

    find_multiples(1, 10, 2, 3) => [4, 10]
    from 1 to 10 we have to find all the numbers that are divisible by 2 and skip 3 steps after each iteration.
    1 is not divisible by 2, after that we skip 3 iterations and get straight to 4 which is divisible by 2, skip again get 7, skip again get 10.

    find_multiples(5, 50, 10, 3) => [20, 50]
    """
    output_list = []
    for i in range(start, end + 1, skip):
        if i % div == 0:
            output_list.append(i)
    return output_list


def sum_between_25(numbers: list) -> int:
    """
    Return the sum of the numbers in the array which are between 2 and 5.

    Summing starts from 2 (not included) and ends at 5 (not included).
    The section can contain 2 (but cannot 5 as this would end it).
    There can be several sections to be summed.

    sum_between_25([1, 3, 6, 7]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6]) => 7
    sum_between_25([1, 2, 3, 4, 6, 6]) => 19
    sum_between_25([1, 3, 3, 4, 5, 6]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6, 1, 2, 9, 5, 6]) => 16
    sum_between_25([1, 2, 3, 2, 5, 5, 3, 5]) => 5

    :param numbers:
    :return:
    """
    output_sum_list = []
    flag = 0
    for i in numbers:
        if i == 2 and flag != 3:
            flag = 2
        elif i == 5:
            flag = 5
        if flag == 3 and i != 5:
            output_sum_list.append(i)
        if flag == 2:
            flag = 3
    return sum(output_sum_list)


def pair_star_recursive(s: str) -> str:
    """
    Compute a string where same adjacent symbols are separated by '*'.

    Given a string, compute recursively a new string where identical chars
    that are adjacent in the original string are separated from each other by a "*".

    pair_star_recursive("abc") => "abc"
    pair_star_recursive("aabc") => "a*abc"
    pair_star_recursive("aaac") => "a*a*ac"
    pair_star_recursive("") => ""
    pair_star_recursive("aaaa") => "a*a*a*a"
    """
    if s == "":
        return ""
    elif len(s) == 1:
        return s
    elif s[0] == s[1]:
        return s[0] + "*" + pair_star_recursive(s[1:])
    else:
        return s[0] + pair_star_recursive(s[1:])


def time_diff(start_time: str, end_time: str) -> str:
    """
    Return difference between two times.

    Times are given in the format "HH:MM",
    where HH is 2-digit hour and MM is 2-digit minutes' marker.
    The result is also in the format of "HH:MM".
    Difference basically means end_time - start_time.
    time_diff("10:00", "10:00") => "00:00"
    time_diff("10:00", "11:01") => "01:01"
    time_diff("10:00", "09:01") => "23:01"
    time_diff("10:00", "08:59") => "22:59"
    time_diff("10:01", "10:00") => "23:59"
    """
    start_time = start_time.split(":")
    end_time = end_time.split(":")
    output_list = [int(end_time[0]) - int(start_time[0]), int(end_time[1]) - int(start_time[1])]
    if output_list[1] < 0:
        output_list[0] -= 1
        output_list[1] = 60 + output_list[1]
    if output_list[0] < 0:
        output_list[0] = 24 + output_list[0]
    if len(str(output_list[0])) == 1:
        output_list[0] = "0" + str(output_list[0])
    if len(str(output_list[1])) == 1:
        output_list[1] = "0" + str(output_list[1])
    return f"{output_list[0]}:{output_list[1]}"


class Animal:
    """Animal."""

    def __init__(self, name: str, species: str, sound: str):
        """Initialize animal."""
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        """
        Return a sound that represents an animal.

        "Fluffy the Dog says Woof"
        Fluffy -> name
        Dog -> species
        Woof -> sound
        """
        return f"{self.name} the {self.species} says {self.sound}"


class Dog(Animal):
    """Dog."""

    def __init__(self, name, breed):
        """Initialize dog that is a child-class of Animal class."""
        super().__init__(name, "Dog", "Woof")
        self.breed = breed

    def wag_tail(self):
        """
        Return a name of a good doggo and breed if it's happy.

        "Fluffy the Corgi wags tail"
        Fluffy -> name
        Corgi -> breed
        """
        return f"{self.name} the {self.breed} wags tail"


class Cat(Animal):
    """Cat."""

    def __init__(self, name, color):
        """Initialize cat that is a child-class of Animal class."""
        super().__init__(name, "Cat", "Meow")
        self.color = color

    def purr(self):
        """
        Return a name of a good doggo and breed if it's happy.

        "Jorge the Purple cat purrs"
        Jorge -> name
        Purple -> color
        """
        return f"{self.name} the {self.color} {self.species.lower()} purrs"


class PetShop:
    """PetShop."""

    def __init__(self):
        """Initialize PetShop."""
        self.inventory = []

    def add_to_inventory(self, animal: Animal):
        """Add animal to inventory."""
        self.inventory.append(animal)

    def remove_from_inventory(self, animal: Animal):
        """Remove animal from inventory."""
        self.inventory.remove(animal)

    def list_inventory(self):
        """
        Return representation of a pet shop inventory.

        "Fluffy the Dog
        Jorge the Cat
        Peppa the Pig"
        """
        output_string = ""
        for i in self.inventory:
            output_string += f"{i.name} the {i.species}\n"
        output_string = output_string.rstrip("\n")
        return output_string

    def sell_pet(self, animal: Animal):
        """
        Sell a pet, remove it from inventory and write a regarding message.

        If animal is present in inventory -> "Fluffy the Dog has been sold"
        Else -> "Fluffy the Dog is not in inventory"
        """
        if animal in self.inventory:
            self.inventory.remove(animal)
            return f"{animal.name} the {animal.species} has been sold"
        else:
            return f"{animal.name} the {animal.species} is not in inventory"

    def give_treat(self, animal: Animal):
        """
        Give treat to an animal and write a regarding message.

        If animal is Dog -> "Fluffy the Dog wags tail for treat"
        If animal is Cat -> "Jorge the Purple cat purrs for treat"
        Else -> "Peppa the Pig doesn't like treats"
        """
        if animal.species == "Dog":
            return f"{animal.name} the {animal.breed} wags tail for treat"
        elif animal.species == "Cat":
            return f"{animal.name} the {animal.color} {animal.species.lower()} purrs for treat"
        else:
            return f"{animal.name} the {animal.species} doesn't like treats"


class Book:
    """Book."""

    def __init__(self, title: str, author: str, publisher: str, isbn: str):
        """Initialize book."""
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        """
        Return string representation of a book.

        "The Great Gatsby by F. Scott Fitzgerald"
        Name of the book and author.
        """
        return f"{self.title} by {self.author}"

    def check_out(self):
        """
        Check out a book if it is available.

        return true if available and change status to unavailable.
        else return false.
        """
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def check_in(self):
        """Change status of a book to available."""
        self.is_available = True


class Patron:
    """Patron."""

    def __init__(self, name: str):
        """Initialize Patron."""
        self.name = name
        self.books = []

    def __str__(self):
        """Return string representation of a name."""
        return self.name

    def check_out(self, book: Book):
        """
        Check out a book and adds to patron books.

        If book can be checked out return true,
        Else false
        """
        if book.is_available:
            self.books.append(book)
            return book.check_out()

    def return_book(self, book: Book):
        """
        Return a book, check it in and remove from patron books.

        If book can be returned return true,
        Else false
        """
        if book in self.books:
            book.check_in()
            self.books.remove(book)
            return True
        else:
            return False


class Library:
    """Library."""

    def __init__(self):
        """Initialize library."""
        self.books = []
        self.patrons = []

    def add_book(self, book: Book):
        """
        Add a book and return a greeting message.

        "New book available on our shelves:
         Title: The Great Gatsby
         Author: F. Scott Fitzgerald
         Publisher: Scribner's"
        """
        self.books.append(book)
        return f"New book available on our shells:\nTitle: {book.title}\nAuthor: {book.author}\nPublisher: {book.publisher}"

    def add_patron(self, patron: Patron):
        """
        Add patron to the list of patrons.

        return greeting message:
        "Warm welcome to our new patron: Ago"
        """
        self.patrons.append(patron)
        return f"Warm welcome to our new patron: {patron.name}"

    def remove_book(self, book: Book):
        """Remove book from books."""
        self.books.remove(book)

    def search_by_title(self, title: str):
        """Return all the books with the same title."""
        return [book for book in self.books if book.title == title]

    def search_by_author(self, author: str):
        """Return all the books with the same author."""
        return [book for book in self.books if book.author == author]

    def search_by_isbn(self, isbn: str):
        """Return all the books with the same isbn."""
        return [book for book in self.books if book.isbn == isbn]

    def search_available_books(self):
        """Return all the available books."""
        return [book for book in self.books if book.is_available]

    def search_books(self, search_query: [Book]):
        """
        Return all the books found alike the given books in the given list.

        All the books that have at least on of parameters:
        same author, same title, same isbn are the types of book that we are looking for.
        Do not return duplicates.
        """
        output_list = []
        for book_preference in search_query:
            for book in self.books:
                if book_preference.author == book.author:
                    output_list.append(book)
                elif book_preference.title == book.title:
                    output_list.append(book)
                elif book_preference.isbn == book.isbn:
                    output_list.append(book)
        return output_list

    def check_out_book(self, book: Book, patron: Patron):
        """
        Check out a book for a patron.

        Book can be checked out if it is present in the books and if patron is present among patrons.
        Also check if the book is available right now.
        Return True if available and don't forget to change it status to unavailable.
        Else return false.
        """
        if book in self.books and patron in self.patrons and book.is_available:
            book.is_available = False
            return True
        else:
            return False

    def return_book(self, book: Book, patron: Patron):
        """
        Return book back to books.

        Book can be returned if it is one of the library books and if patreon present among library patrons.
        Don't forget to change books status and return True if successful.
        Else return false.
        """
        if book in self.books and patron in self.patrons:
            book.is_available = True
            return True
        else:
            return False


if __name__ == '__main__':
    # assert double_char("ab") == "aabb"
    # assert double_char("") == ""
    #
    # assert sort_numbers_as_reversed_strings([10, 1, 34, 15, 47, 96, 24, 63, 22]) == [10, 1, 22, 63, 24, 34, 15, 96, 47]
    # assert sort_numbers_as_reversed_strings([0, 21, 32, 13, 4, 55, 6]) == [0, 21, 32, 13, 4, 55, 6]
    #
    # assert find_multiples(1, 10, 2, 1) == [2, 4, 6, 8, 10]
    # assert find_multiples(1, 20, 3, 2) == [3, 9, 15]
    #
    # assert sum_between_25([1, 2, 3, 4, 5, 6]) == 7
    # assert sum_between_25([1, 2, 3, 4, 6, 6]) == 19
    #
    # assert pair_star_recursive("abc") == "abc"
    # assert pair_star_recursive("aaa") == "a*a*a"
    #
    # assert time_diff("10:00", "11:00") == "01:00"
    # assert time_diff("10:02", "11:01") == "00:59"
    # assert time_diff("10:02", "10:00") == "23:58"
    #
    # # # pet shop
    # # fido = Animal("Fido", "Dog", "Bark")
    # # buddy = Dog("Buddy", "Golden Retriever")
    # # whisper = Cat("Whisper", "Tabby")
    # #
    # # pet_shop = PetShop()
    # # assert fido.make_sound() == "Fido the Dog says Bark"
    # # assert buddy.wag_tail() == "Buddy the Golden Retriever wags tail"
    # # assert whisper.purr() == "Whisper the Tabby cat purrs"
    # #
    # # pet_shop.add_to_inventory(fido)
    # # assert pet_shop.list_inventory() == "Fido the Dog"
    # # pet_shop.add_to_inventory(buddy)
    # # print(pet_shop.list_inventory())  # "Fido the Dog
    # # #  Buddy the Dog"
    # # assert pet_shop.sell_pet(fido) == "Fido the Dog has been sold"
    # # assert pet_shop.sell_pet(whisper) == "Whisper the Cat is not in inventory"
    # #
    # # assert pet_shop.give_treat(fido) == "Fido the Golden Retriever wags tail for treat"
    # # assert pet_shop.give_treat(whisper) == "Whisper the Tabby cat purrs for treat"
    #
    # # library catalog
    # book1 = Book("1", "1", "1", "1")
    # book2 = Book("2", "2", "2", "2")
    # book3 = Book("3", "3", "3", "3")
    #
    # patron1 = Patron("Ago")
    # patron2 = Patron("Jorge")
    # patron3 = Patron("Hank")
    #
    # assert book1.__str__() == "1 by 1"
    # assert book1.publisher == "1"
    # assert book1.isbn == "1"
    # assert book1.is_available is True
    #
    # assert patron1.__str__() == "Ago"
    # assert patron1.books == []
    #
    # library1 = Library()
    #
    # print(library1.add_book(book1))
    # # "New book available on our shelves:
    # #  Title: 1
    # #  Author: 1
    # #  Publisher: 1"
    # library1.add_book(book2)
    # library1.add_book(book3)
    #
    # assert library1.add_patron(patron1) == "Warm welcome to our new patron: Ago"
    # assert patron1.check_out(book1) is True
    # assert len(library1.books) == 3
    # library1.remove_book(book1)
    # assert len(library1.books) == 2
    #
    # assert len(library1.search_by_title("1")) == 0
    # assert len(library1.search_by_title("2")) == 1
    #
    # assert len(library1.search_by_author("1")) == 0
    # assert len(library1.search_by_author("2")) == 1
    #
    # assert len(library1.search_by_isbn("1")) == 0
    # assert len(library1.search_by_isbn("3")) == 1
    #
    # assert len(library1.search_available_books()) == 2
    #
    # assert len(library1.search_books([book1, book2, book3])) == 2
    #
    # assert library1.check_out_book(book2, patron1) is True
    # assert library1.check_out_book(book2, patron2) is False
    #
    # assert library1.return_book(book2, patron1) is True
    # assert len(patron1.books) == 0
    # assert book2.is_available is True

    new_list = list(range(1, 10))
    print(new_list)
