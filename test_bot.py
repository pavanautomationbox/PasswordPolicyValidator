
from bot import validate_password


# Test 1: Strong password should pass
def test_strong_password():
    result = validate_password("Strong@123")

    assert result == []


# Test 2: Password shorter than 8 characters
def test_short_password():
    result = validate_password("Ab1!")

    assert any("at least 8 characters" in rule for rule in result)


# Test 3: Password without uppercase letter
def test_missing_uppercase():
    result = validate_password("strong@123")

    assert any("uppercase" in rule for rule in result)


# Test 4: Password without lowercase letter
def test_missing_lowercase():
    result = validate_password("STRONG@123")

    assert any("lowercase" in rule for rule in result)


# Test 5: Password without a number
def test_missing_number():
    result = validate_password("Strong@abc")

    assert any("number" in rule for rule in result)


# Test 6: Password without a special character
def test_missing_special_character():
    result = validate_password("Strong123")

    assert any("special character" in rule for rule in result)


# Test 7: Known weak password should be rejected
def test_weak_password():
    result = validate_password("password")

    assert any("weak password" in rule for rule in result)


# Test 8: Multiple failed rules should be returned
def test_multiple_failed_rules():
    result = validate_password("abc")

    assert len(result) >= 3

    assert any("at least 8 characters" in rule for rule in result)
    assert any("uppercase" in rule for rule in result)
    assert any("number" in rule for rule in result)
    assert any("special character" in rule for rule in result)
