"""If you're going to perform recursion, you need to use recursion."""


def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.

    loop_reverse("hey") => "yeh"
    loop_reverse("aaa") => "aaa"
    loop_reverse("") => ""
    loop_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    reversed_character_list = []
    character_list = list(s)
    if s:
        for x in range(len(s)):
            if x != 0:
                reversed_character_list.append(character_list[x - (2 * x)])
        reversed_character_list.append(character_list[0])
        reversed_string = ''.join(reversed_character_list)
        return reversed_string
    else:
        return ""


def recursive_reverse(s: str) -> str:
    """
    Reverse a string using recursion.

    recursive_reverse("hey") => "yeh"
    recursive_reverse("aaa") => "aaa"
    recursive_reverse("") => ""
    recursive_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    if len(s) == 0:
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    loop_sum(0) => 0
    loop_sum(3) => 6
    loop_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    num_list = []
    for num in range(n):
        num_list.append(num + 1)
    return sum(num_list)


def recursive_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.

    recursive_sum(0) => 0
    recursive_sum(3) => 6
    recursive_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    if n == 0:
        return n
    else:
        return n + recursive_sum(n - 1)


def countdown(n: int):
    """
    Write a simple recursive function that returns a list of numbers that count down from n.

    countdown(5) -> [5, 4, 3, 2, 1, 0]
    countdown(8) -> [8, 7, 6, 5, 4, 3, 2, 1, 0]
    countdown(-1) -> []

    :param n: start
    :return: countdown sequence
    """
    if n < 0:
        return []
    elif n == 0:
        return [0]
    else:
        return [n] + countdown(n - 1)


def add_commas(n: int):
    """
    Add commas into a number.

    In representing large numbers, from the right side to the left,
    English texts usually use commas to separate each group of three digits in front of the decimal.

    Your challenge is to output a number n formatted with commas.

    add_commas(1245) -> '1,245'
    add_commas(123456789) -> '123,456,789'
    add_commas(1011) -> '1,011'

    :param n: int
    :return: string of the formatted int
    """
    num_list = list(add_commas_reversed(n))
    if num_list[-1] == ",":
        num_list.pop()
    num_list.reverse()
    return ''.join(num_list)


def add_commas_reversed(n):
    """Add commas, but reversed."""
    n = str(n)
    if len(n) == 0:
        return n
    elif len(n) % 3 == 0:
        return add_commas_reversed(n[1:]) + n[0] + ","
    else:
        return add_commas_reversed(n[1:]) + n[0]


def sum_digits_recursive(number) -> int:
    """
    Return the sum of the digits in number.

    Given a non-negative int n, return the sum of its digits recursively (no loops).

    sum_digits_recursive(123) => 6
    sum_digits_recursive(1) => 1
    sum_digits_recursive(0) => 0
    sum_digits_recursive(999) => 27

    Hint: turn the number into string and take one digit at a time.

    :param number: non-negative number
    :return: sum of digits in the number
    """
    number = str(number)
    if len(number) == 0:
        return 0
    else:
        return int(sum_digits_recursive(number[1:])) + int(number[0])


def pair_star_recursive(s: str) -> str:
    """
    Add star between identical adjacent chars.

    Given a string, compute recursively a new string
    where identical chars that are adjacent in the original string
    are separated from each other by a "*".

    pair_star_recursive("abc") => "abc"
    pair_star_recursive("aa") => "a*a"
    pair_star_recursive("aaa") => "a*a*a"
    pair_star_recursive("") => ""

    :param s: input string
    :return: string with stars between identical chars.
    """
    if 0 <= len(s) <= 1:
        return s
    elif s[0] == s[1]:
        return s[0] + "*" + pair_star_recursive(s[1:])
    else:
        return s[0] + pair_star_recursive(s[1:])


def stonks(coins: float, rate: float, years: int) -> int:
    """
    Each year your crypto-investment grows.

    Write a recursive function that calculates the net worth of coins after some years.
    Rate is in percents.
    Round the answer down to the nearest integer.

    stonks(1000, 10, 10) -> 2593
    stonks(100000, 12, 3) -> 140492

    :param coins: starting amount (0-10000)
    :param rate: rate percentage (0-100)
    :param years: number of years (0-50)
    :return: coins after years
    """
    if coins == 0:
        return 0
    elif rate == 0 or years == 0:
        return coins
    else:
        coins = coins + coins * (rate / 100)
    return int(stonks(coins, rate, years - 1))


def quic_mafs(a: int, b: int) -> list:
    """
    Write a recursive function that applies the following operations.

    i) If a = 0 or b = 0, return [a,b]. Otherwise, go to step (ii);
    ii) If a >= 2*b, set a = a - 2*b, and repeat step (i). Otherwise, go to step (iii);
    iii) If b >= 2*a, set b = b - 2*a, and repeat step (i). Otherwise, return [a,b].

    quic_mafs(6, 19) -> [6, 7]
    quic_mafs(2, 1) -> [0, 1]
    quic_mafs(22, 5) -> [0, 1]
    quic_mafs(8796203,7556) -> [1019,1442]

    :param a: int
    :param b: int
    :return: result
    """
    if a == 0 or b == 0:
        return [a, b]
    elif a >= 2 * b:
        a = a - 2 * b
        return quic_mafs(a, b)
    elif b >= 2 * a:
        b = b - 2 * a
        return quic_mafs(a, b)
    else:
        return [a, b]


def find_string_length(string: str) -> int:
    if len(string) == 0:
        return 0
    else:
        return find_string_length(string[1:]) + len(string[0])


def get_every_nth_letter(string: str, n: int) -> str:
    if len(string) == 0:
        return ""
    elif len(string) < n:
        return ""
    else:
        return string[n - 1] + get_every_nth_letter(string[n:], n)


def replace(input_string: str, char_to_replace: str, new_string: str) -> str:
    if len(char_to_replace) != 1:
        return "Length of char_to_replace must be one character!"

    if not input_string:
        return ""

    if input_string[0] == char_to_replace:
        return new_string + replace(input_string[1:], char_to_replace, new_string)
    else:
        return input_string[0] + replace(input_string[1:], char_to_replace, new_string)


def fibonacci(num: int, fib_list=None) -> list | None:
    if num <= 2:
        return [0, 1]

    if fib_list is None:
        fib_list = [0, 1]

    if len(fib_list) == num:
        return fib_list

    next_fib = fib_list[-1] + fib_list[-2]
    fib_list.append(next_fib)

    return fibonacci(num, fib_list)


def x_sum_recursion(nums: list, x: int) -> int:
    if not nums:
        return 0

    if x == 0 or abs(x) > len(nums):
        return 0

    if x > 0:
        return nums[x - 1] + x_sum_recursion(nums[x:], x)
    else:
        return nums[x] + x_sum_recursion(nums[:x], x)


def check_for_prime(num: int, i=2) -> bool:
    """
    Check if input number 'num' is a prime number using recursion.

    check_for_prime(0) => False
    check_for_prime(1) => False
    check_for_prime(997) => True

    Solution
    :param num: integer to be checked
    :param i: used to check if 'num' is a multiple of some integer.
    :return: boolean. True if 'num' is prime, False otherwise
    """
    if num <= 1:
        return False
    if num % i == 0:
        return False
    if num // 2 == i:
        return True
    if num % i != 0:
        return check_for_prime(num, i + 1)


def sum_squares(nested_list: list | int) -> int:
    """
    Write a function that sums squares of numbers in 'nested_list' using recursion.

    'nested_list' may contain additional lists.
    (Hint use the type() or isinstance() function)

    sum_squares([1, 2, 3]) -> 14
    sum_squares([[1, 2], 3]) -> sum_squares([1, 2]) + 9 -> 1 + 4 + 9 -> 14
    sum_squares([[[[[[[[[2]]]]]]]]]) -> 4

    :param nested_list: list of lists of lists of lists of lists ... and ints
    :return: sum of squares
    """
    if isinstance(nested_list, int):
        return nested_list ** 2
    else:
        return sum(sum_squares(x) for x in nested_list)


# Example usage:
print(sum_squares([1, 2, 3]))  # 14
print(sum_squares([[1, 2], 3]))  # 14
print(sum_squares([[[[[[[[[2]]]]]]]]]))  # 4


if __name__ == "__main__":
    print(loop_reverse("hello"))  # -> "olleh"
    print(loop_reverse(""))  # -> ""
    print(loop_reverse("123"))  # -> "321"

    print(recursive_reverse("hello"))  # -> "olleh"
    print(recursive_reverse(""))  # -> ""
    print(recursive_reverse("123"))  # -> "321"

    print(loop_sum(0))  # -> 0
    print(loop_sum(3))  # -> 6
    print(loop_sum(10))  # -> 55

    print(recursive_sum(0))  # -> 0
    print(recursive_sum(3))  # -> 6
    print(recursive_sum(10))  # -> 55

    print(countdown(5))  # -> [5, 4, 3, 2, 1, 0]
    print(countdown(8))  # -> [8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(countdown(-1))  # -> []

    print(add_commas(1245))  # -> '1,245'
    print(add_commas(123456789))  # -> '123,456,789'
    print(add_commas(1011))  # -> '1,011'

    print(sum_digits_recursive(123))  # -> 6
    print(sum_digits_recursive(0))  # -> 0
    print(sum_digits_recursive(1000000000000000))  # -> 1

    print(pair_star_recursive("abc"))  # -> "abc"
    print(pair_star_recursive("aaa"))  # -> a*a*a
    print(pair_star_recursive(""))  # -> ""

    print(stonks(1000, 10, 10))  # -> 2593
    print(stonks(100000, 12, 3))  # -> 140492

    print(quic_mafs(6, 19))  # -> [6, 7]
    print(quic_mafs(2, 1))  # -> [0, 1]
    print(quic_mafs(22, 5))  # -> [0, 1]
    print(quic_mafs(8796203, 7556))  # -> [1019,1442]
