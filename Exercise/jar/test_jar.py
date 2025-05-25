from jar import Jar
import pytest

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12

    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdraw():
    jar = Jar(15)
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7
    jar.withdraw(7)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(10)

def test_invalid_input():
    jar = Jar()
    try:
        jar.deposit(-1)
    except ValueError as e:
        assert str(e) == "Number of cookies to deposit must be a non-negative integer"

    try:
        jar.withdraw(5)
    except ValueError as e:
        assert str(e) == "Not enough cookies in the jar"

    try:
        jar = Jar(-5)
    except ValueError as e:
        assert str(e) == "Capacity must be a non-negative integer"