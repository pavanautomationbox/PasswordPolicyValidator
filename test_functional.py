
import pytest
from bot import validate_password


# Test 1: Strong password should be accepted
def test_valid_password():
    result = validate_password("Strong@123")
    assert result == []


# Test 2: Password must have minimum 8 characters
def test_password_minimum_length():
    result = validate_password("Ab1!")
    assert any("at least 8 characters" in rule for rule in result)


# Test 3: Password must contain uppercase
def test_uppercase_required():
    result = validate_password("strong@123")
    assert any("uppercase" in rule for rule in result)


# Test 4: Password must contain lowercase
def test_lowercase_required():
    result = validate_password("STRONG@123")
    assert any("lowercase" in rule for rule in result)


# Test 5: Password must contain a number
def test_number_required():
    result = validate_password("Strong@abc")
    assert any("number" in rule for rule in result)


# Test 6: Password must contain special character
def test_special_character_required():
    result = validate_password("Strong123")
    assert any("special character" in rule for rule in result)


# Test 7: Weak password should be rejected
def test_weak_password_rejected():
    result = validate_password("password")
    assert any("weak password" in rule for rule in result)


# Test 8: Password matching is case-insensitive
def test_weak_password_case_insensitive():
    result = validate_password("PASSWORD")
    assert any("weak password" in rule for rule in result)


# Test 9: All failed rules should be returned
def test_multiple_failed_rules():
    result = validate_password("abc")

    assert len(result) >= 4

    assert any("at least 8 characters" in rule for rule in result)
    assert any("uppercase" in rule for rule in result)
    assert any("number" in rule for rule in result)
    assert any("special character" in rule for rule in result)


# Test 10: Empty password should be rejected
def test_empty_password():
    result = validate_password("")

    assert len(result) >= 5
