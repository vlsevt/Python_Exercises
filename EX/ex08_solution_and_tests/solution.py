"""Solution."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    return (1 <= time <= 4 and coffee_needed is False) or (5 <= time <= 17 and coffee_needed is True) or (18 <= time <= 24)


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == 5 and c == 5:
        return 10
    elif a == b == c:
        return 5
    elif a != b and a != c:
        return 1
    elif a == b or a == c:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    left_after_using_big_baskets = ordered_amount - (ordered_amount // 5 * 5)

    if big_baskets != 0 and ((ordered_amount - big_baskets * 5) <= small_baskets):
        if big_baskets * 5 >= ordered_amount and small_baskets >= left_after_using_big_baskets:
            return left_after_using_big_baskets
        elif big_baskets * 5 < ordered_amount and small_baskets >= left_after_using_big_baskets:
            return ordered_amount - big_baskets * 5
        else:
            return -1
    elif small_baskets >= ordered_amount:
        return ordered_amount
    else:
        return -1


if __name__ == '__main__':
    print(fruit_order(5, 4, 22))
