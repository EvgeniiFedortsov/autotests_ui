import pytest

def test_first_try():  # Этот тест мы добавили в предыдущем шаге
    print("Hello World!")

def test_equal():
    assert 1 == 1

def test_not_equal():
    assert 1 != 2

def test_in_list():
    assert 3 in [1, 2, 3, 4]

def test_boolean():
    is_authenticated = True
    assert is_authenticated

def test_lists():
    assert [1, 2, 3] == [1, 2, 4]

def test_sum():
    assert 1 + 1 == 3, "Сумма 1 и 1 должна быть 2!"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_assert_positive_case():  # Новый тест, которые проверяет положительный кейс
    assert (2 + 2) == 4  # Ожидается, что тест пройдет


def test_assert_negative_case():  # Новый тест, которые проверяет негативный кейс
    assert (2 + 2) == 5  # Тут должна быть ошибка