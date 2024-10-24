"""Math operators."""


def add(x: int, y: int) -> int:
    """Add x to y."""
    return x + y


def sub(x: int, y: int) -> int:
    """Subtract y from x."""
    return x - y


def multiply(x: int, y: int) -> int:
    """Multiply x by y."""
    return x * y


def div(x: int, y: int) -> float:
    """Divide x by y."""
    return x / y


def modulus(x: int, y: int) -> int:
    """Divide x by y and return remainder. Use an arithmetic operator."""
    return x % y


def floor_div(x: int, y: int) -> int:
    """Divide x by y and floor the value. Use an arithmetic operator."""
    return x // y


def exponent(x: int, y: int) -> int:
    """Calculate x raised to the power of y."""
    return x ** y


def first_greater_or_equal(x: int, y: int) -> bool:
    """If x is greater or equal than y then return True. If not then return False."""
    if x >= y:
        return True
    else:
        return False


def second_less_or_equal(x: int, y: int) -> bool:
    """If y is less or equal than x then return True. If not then return False."""
    if y <= x:
        return True
    else:
        return False


def x_is_y(x: int, y: int) -> bool:
    """If x value is the same as y value then return True. If not then return False."""
    if x == y:
        return True
    else:
        return False


def x_is_not_y(x: int, y: int) -> bool:
    """If x value is not the same as y value then return True. If not then return False."""
    if x != y:
        return True
    else:
        return False


def if_else(a: int, b: int, c: int, d: int) -> float:
    """
    Create a program that has 4 numeric parameters.

    Multiply parameters 1-2 (multiply a by b) by each other and divide parameters 3-4 (divide c by d) by each other.
    Next check and return the greater value. If both values are the same then return 0 (number zero).
    """
    if (a * b) == (c / d):
        return 0
    elif (a * b) > (c / d):
        return a * b
    else:
        return c / d


def surface(a: int, b: int):
    """Add the missing parameters to calculate the surface of a rectangle. Calculate and return the value of the surface."""
    return a * b


def volume(a: int, b: int, c: int):
    """Add the missing parameters to calculate the volume of a cubiod. Calculate and return the value of the volume."""
    return a * b * c


def clock(days: int, hours: int, minutes: int, seconds: int):
    """Define a function, the parameters of which are 4 whole numbers, named days, hours, minutes, seconds. The function needs to convert all the times passed as arguments to minutes and return the total amount of minutes."""
    return days * 24 * 60 + hours * 60 + minutes + seconds / 60


def calculate(a: int, b: int, c: int):
    """Signify the operation and return the result of it.

    0 - addition
    1 - subtraction
    2 - multiplication
    3 - division
    The second and third parameter stand for the operands of the operation.
    The function has to choose the correct operation based on the received arguments and return the result of it.
    """
    if a == 0:
        return b + c
    elif a == 1:
        return b - c
    elif a == 2:
        return b * c
    elif a == 3:
        return b / c


if __name__ == '__main__':
    print(add(1, -2))  # -1
    print(sub(5, 5))  # 0
    print(multiply(5, 5))  # 25
    print(div(15, 5))  # 3
    print(modulus(9, 3))  # 0
    print(floor_div(3, 2))  # 1
    print(exponent(5, 5))  # 3125
    print(first_greater_or_equal(1, 2))  # False
    print(second_less_or_equal(5, 5))  # True
    print(x_is_y(1, 2))  # False
    print(x_is_not_y(1, 2))  # True
    print(if_else(1, 3, 5, 99))  # 3
    print(if_else(2, 1, 10, 5))  # 0
    print(surface(1, 2))  # 2
    print(volume(5, 5, 5))  # 125
    print(clock(0, 0, 1, 15))  # 1.25
    print(clock(0, 1, 5, 0))  # 65
    print(calculate(3, 70, 2))
