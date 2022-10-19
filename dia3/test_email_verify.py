import email
import pytest
from exercicios import email_verify, verify_list_emails

def test_email_verify_email_name_user_first_string():
   with pytest.raises(ValueError):
      email_verify('1joao@gmail.com')


def test_email_verify_name_user_is_alpha_or_digit():
    with pytest.raises(ValueError):
      email_verify('joao#@gmail.com')


def test_email_verify_name_website_is_alpha_or_digit():
    with pytest.raises(ValueError):
      email_verify('joao@gm#ail.com')


def test_email_verify_name_domain_len():
    with pytest.raises(ValueError):
      email_verify('joao@gmail.comm')


def test_email_verify_name_correct():
    assert email_verify('joao@gmail.com') == True


def test_email_verify_name_correct_with_number():
    assert email_verify('joao11@gmail.com') == True


def test_email_verify_name_correct_with_dashes():
    assert email_verify('joao1-1@gmail.com') == True


def test_email_verify_name_website_correct_with_number():
    assert email_verify('joao1-1@gmail1.com') == True


def test_email_verify_name_website_correct_with_number():
    assert email_verify('joao1-1@gmail1.com') == True