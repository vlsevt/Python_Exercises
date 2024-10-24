"""Test."""

import solution


def test_students_study__evening_not_coffee_needed():
    """Test if coffee is needed in evening."""
    assert solution.students_study(24, True) is True
    assert solution.students_study(24, False) is True
    assert solution.students_study(18, True) is True
    assert solution.students_study(18, False) is True


def test_students_study__night_sleep():
    """Test if coffee is needed at night."""
    assert solution.students_study(1, True) is False
    assert solution.students_study(1, False) is True
    assert solution.students_study(4, True) is False
    assert solution.students_study(4, False) is True


def test_students_study__day_coffee_needed():
    """Test if coffee is needed in daytime."""
    assert solution.students_study(5, True) is True
    assert solution.students_study(5, False) is False
    assert solution.students_study(17, True) is True
    assert solution.students_study(17, False) is False


def test_lottery():
    """Test lottery."""
    assert solution.lottery(5, 5, 5) == 10
    assert solution.lottery(2, 2, 2) == 5
    assert solution.lottery(-4, -4, -4) == 5
    assert solution.lottery(0, 0, 0) == 5
    assert solution.lottery(3, 3, 7) == 0
    assert solution.lottery(7, 2, 7) == 0
    assert solution.lottery(8, 1, 1) == 1
    assert solution.lottery(8, 5, 1) == 1


def test_fruit_order():
    """Test fruit order."""
    assert solution.fruit_order(0, 0, 0) == 0
    assert solution.fruit_order(0, 4, 0) == 0
    assert solution.fruit_order(0, 4, 2) == -1
    assert solution.fruit_order(10, 0, 0) == 0
    assert solution.fruit_order(5, 5, 0) == 0
    assert solution.fruit_order(2, 2, 2) == 2
    assert solution.fruit_order(0, 2, 15) == -1
    assert solution.fruit_order(0, 2, 22) == -1
    assert solution.fruit_order(0, 5, 10) == 0
    assert solution.fruit_order(5, 0, 5) == 5
    assert solution.fruit_order(9, 0, 5) == 5
    assert solution.fruit_order(10, 3, 200) == -1
    assert solution.fruit_order(4, 2, 14) == 4
    assert solution.fruit_order(4, 2, 12) == 2
    assert solution.fruit_order(4, 2, 8) == 3
    assert solution.fruit_order(90, 30, 241) == -1
    assert solution.fruit_order(95, 1, 100) == 95
    assert solution.fruit_order(7, 0, 16) == -1
    assert solution.fruit_order(7, 4, 20) == 0
    assert solution.fruit_order(0, 4, 20) == 0
    assert solution.fruit_order(2, 5, 4) == -1
    assert solution.fruit_order(7, 5, 4) == 4
    assert solution.fruit_order(2356, 889, 5611) == 1166
    assert solution.fruit_order(0, 22232225, 4233232323) == -1
    assert solution.fruit_order(1, 215641826538290947, 2) == -1
    assert solution.fruit_order(6520657301, 21564182653, 25639206574839075849307658493065784930) == -1
    assert solution.fruit_order(2, 120000001, 600000004) == -1
    assert solution.fruit_order(4, 120000001, 600000004) == 4
