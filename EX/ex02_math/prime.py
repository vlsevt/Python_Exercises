"""Prime number check."""


def is_prime_number(number: int) -> bool:
    """Check if the number is a prime number."""
    if number == 2:
        return True
    elif number > 2:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False
