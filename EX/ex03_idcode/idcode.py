"""EX03 ID code."""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.
    You don't have to validate the ID-code here. If it has 11 numbers, then it is enough for now.

    :param text: string
    :return: string
    """
    # Write your code here
    num = ''
    for char in text:
        if char.isdigit():
            num += char
    if len(str(num)) > 11:
        return "Too many numbers!"
    elif len(str(num)) < 11:
        return "Not enough numbers!"
    else:
        return num


def the_first_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code only with the first algorithm.

    The first algorithm can be calculated with ID code's first 10 numbers.
    Each number must be multiplied with its corresponding digit
    (in this task, corresponding digits are: 1 2 3 4 5 6 7 8 9 1), after which all the values are summarized
    and divided by 11. The remainder of calculation should be the control number.

    If the remainder is less than 10 and equal to the last number of ID code,
    then that's the correct control number and the function should return the ID code.
    Otherwise, the control number is either incorrect or the second algorithm should be used.
    In this case, return "Needs the second algorithm!".

    If the string contains more or less than 11 numbers, return "Incorrect ID code!".
    In other case use the previous algorithm to get the code number out of the string
    and find out, whether its control number is correct.

    :param text: string
    :return: string
    """
    # Write your code here
    num = ''
    for char in text:
        if char.isdigit():
            num += char
    if len(num) != 11:
        return "Incorrect ID code!"
    else:
        check = ((int(num[0]) * 1 + int(num[1]) * 2 + int(num[2]) * 3 + int(num[3]) * 4 + int(num[4]) * 5 + int(num[5]) * 6 + int(num[6]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 1) % 11)
        if check < 10:
            if check == int(num[10]):
                return num
            else:
                return "Incorrect ID code!"
        else:
            return "Needs the second algorithm!"


if __name__ == '__main__':
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"

    print(the_first_control_number_algorithm(""))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("123456789123456789"))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("ID code is: 49403136526"))  # -> "49403136526"
    print(the_first_control_number_algorithm("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"
    print(the_first_control_number_algorithm("50412057633"))  # -> "50412057633"
    print(the_first_control_number_algorithm("Peeter's ID is euf50weird2fs0fsk51ef6t0s2yr7fyf4"))  # -> "Needs
    # the second algorithm! 50205160274"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    # Write your code here
    if 0 <= year_number <= 99:
        return True
    else:
        return False


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    # Write your code here
    if 0 < month_number <= 12:
        return True
    else:
        return False


def is_valid_birth_number(birth_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    # Write your code here
    if 0 < birth_number <= 999:
        return True
    else:
        return False


def is_valid_gender_number(gender_number: int) -> bool:
    """Check if the first number of ID code is correct."""
    # Write your code here
    if 0 < gender_number < 7:
        return True
    else:
        return False


def get_gender(gender: int) -> str:
    """Check the first number and find the person's gender."""
    if gender in (1, 3, 5):
        return "male"
    else:
        return "female"


if __name__ == '__main__':
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    for i in range(110):
        print(f"{i} {is_valid_year_number(i)}")

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True


def get_full_year(gender_number: int, year_number: int) -> int:
    """Define the 4-digit year when given person was born."""
    # Write your code here
    if year_number < 10:
        year_number = str(f"0{year_number}")
    if 1 <= gender_number <= 2:
        return int(f"18{year_number}")
    elif 3 <= gender_number <= 4:
        return int(f"19{year_number}")
    else:
        return int(f"20{year_number}")


def get_birth_place(birth_number: int) -> str:
    """Find the place where the person was born."""
    # Write your code here
    if is_valid_birth_number(birth_number):
        if 1 <= birth_number <= 10:
            return "Kuressaare"
        elif 11 <= birth_number <= 20 or 271 <= birth_number <= 370:
            return "Tartu"
        elif 21 <= birth_number <= 220 or 471 <= birth_number <= 710:
            return "Tallinn"
        elif 221 <= birth_number <= 270:
            return "Kohtla-Järve"
        elif 371 <= birth_number <= 420:
            return "Narva"
        elif 421 <= birth_number <= 470:
            return "Pärnu"
        else:
            return "undefined"
    else:
        return "Wrong input!"


def is_leap_year(year_number: int) -> bool:
    """Find out if it is a leap year."""
    if year_number % 400 == 0 or (year_number % 4 == 0 and year_number % 100 != 0):
        return True
    else:
        return False


if __name__ == '__main__':
    print("\nLeap year:")
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"
    print(get_birth_place(900))


def is_valid_control_number(id_code: str) -> bool:
    """Check if given value is correct for control number in ID code."""
    # Write your code here
    if the_first_control_number_algorithm(id_code) == "Incorrect ID code!":
        return False
    elif the_first_control_number_algorithm(id_code) == "Needs the second algorithm!":
        check = (int(id_code[0]) * 3 + int(id_code[1]) * 4 + int(id_code[2]) * 5 + int(id_code[3]) * 6 + int(id_code[4]) * 7 + int(id_code[5]) * 8 + int(id_code[6]) * 9 + int(id_code[7]) * 1 + int(id_code[8]) * 2 + int(id_code[9]) * 3) % 11
        if check == 10:
            check = 0
            if check == int(id_code[10]):
                return True
            else:
                return False
        elif check == int(id_code[10]):
            return True
        else:
            return False
    else:
        return True


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """Check if given value is correct for day number in ID code."""
    # Write your code here
    if is_valid_gender_number(gender_number) and is_valid_year_number(year_number) and is_valid_month_number(month_number):
        if month_number in (1, 3, 5, 7, 8, 10, 12):
            if day_number <= 31:
                return True
            else:
                return False
        elif month_number == 2:
            if is_leap_year(get_full_year(gender_number, year_number)):
                if day_number <= 29:
                    return True
                else:
                    return False
            else:
                if day_number <= 28:
                    return True
                else:
                    return False
        elif month_number in (4, 6, 9, 11):
            if day_number <= 30:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def is_id_valid(id_code: str) -> bool:
    """Check if given ID code is valid and return the result (True or False)."""
    # Write your code here
    if is_valid_control_number(id_code):
        if is_valid_day_number(int(id_code[0]), int(id_code[1:3]), int(id_code[3:5]), int(id_code[5:7])):
            if is_valid_birth_number(int(id_code[7:10])):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def get_data_from_id(id_code: str) -> str:
    """Get possible information about the person."""
    # Write your code here
    if is_id_valid(id_code):
        year_number = int(id_code[1:3])
        birth_number = int(id_code[7:10])
        return f"This is a {get_gender(int(id_code[0]))} born on {int(id_code[5])}{int(id_code[6])}.{int(id_code[3])}{int(id_code[4])}.{get_full_year(int(id_code[0]), year_number)} in {get_birth_place(birth_number)}."
    else:
        return "Given invalid ID code!"


if __name__ == '__main__':
    print("\nFull message:")
    print(get_data_from_id("36004030339"))  # -> "This is a female born on 27.08.1998 in Tallinn."

