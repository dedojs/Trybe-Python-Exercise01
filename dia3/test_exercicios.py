import pytest
from exercicios import list_nums, encrypt_phrase


def test_list_nums_should_return_list_of_numbers():
    assert list_nums(2) == [1, 2]


def test_list_nums_should_return_fizzBuzz():
    assert list_nums(15)[-1] == 'FizzBuzz'


def test_list_nums_should_return_Buzz():
    assert list_nums(5)[-1] == 'Buzz'


def test_list_nums_should_return_fizz():
    assert list_nums(3)[-1] == 'Fizz'


def test_encrypt_phrase_should_converted_in_2():
    assert encrypt_phrase('abc') == '222'


def test_encrypt_phrase_should_converted_in_3():
    assert encrypt_phrase('def') == '333'


def test_encrypt_phrase_should_converted_in_4():
    assert encrypt_phrase('ghi') == '444'


def test_encrypt_phrase_should_converted_in_5():
    assert encrypt_phrase('jkl') == '555'


def test_encrypt_phrase_should_converted_in_6():
    assert encrypt_phrase('mno') == '666'


def test_encrypt_phrase_should_converted_in_7():
    assert encrypt_phrase('pqrs') == '7777'


def test_encrypt_phrase_should_converted_in_8():
    assert encrypt_phrase('tuv') == '888'


def test_encrypt_phrase_should_converted_in_9():
    assert encrypt_phrase('wxyz') == '9999'


def test_encrypt_phrase_should_return_0_1():
    assert encrypt_phrase('0-1') == '0-1'


def test_encrypt_phrase_should_len_0():
    with pytest.raises(ValueError):
        encrypt_phrase('')


def test_encrypt_phrase_should_len_more_30_char():
    long_char = (
      "1111111111"
      "1111111111"
      "1111111111"
      '1'
    )
    with pytest.raises(ValueError):
        encrypt_phrase(long_char)


def test_encrypt_phrase_should_char_invalid():
    with pytest.raises(ValueError):
        encrypt_phrase('I-**@@##-My')