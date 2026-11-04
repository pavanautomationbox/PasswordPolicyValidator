
import pytest
from bot import validate_password


# ==========================================
# 1. FIXTURE AND TEARDOWN
# ==========================================

@pytest.fixture
def password_samples():

    print("\nSetting up password test data")

    samples = {
        "valid": [
            "Strong@123",
            "Welcome#2026",
            "MySecure$Pass9"
        ],

        "invalid": [
            "abc",
            "password",
            "Strong123",
            "strong@123",
            "STRONG@123",
            "Strong@abc",
            ""
        ]
    }

    yield samples

    # TEARDOWN: Clean up test data after testing
    samples.clear()

    print("\nCleaning up test data")


# ==========================================
# 2. PARAMETRIZATION
# ==========================================

@pytest.mark.parametrize(
    "password, expected",
    [
        ("Strong@123", True),
        ("Welcome#2026", True),
        ("abc", False),
        ("password", False),
        ("Strong123", False),
        ("", False)
    ]
)
def test_password_parametrization(password, expected):

    result = validate_password(password)

    actual = (result == [])

    assert actual == expected


# ==========================================
# 3. POSITIVE ASSERTIONS
# ==========================================

# Test 1: Valid password should be accepted
def test_positive_assertion(password_samples):

    for password in password_samples["valid"]:

        result = validate_password(password)

        assert result == []


# Test 2: True Positive (TP)
# Expected valid and actually accepted
@pytest.mark.parametrize(
    "password",
    [
        "Strong@123",
        "Welcome#2026",
        "MySecure$Pass9"
    ]
)
def test_true_positive(password):

    result = validate_password(password)

    assert result == []


# ==========================================
# 4. NEGATIVE ASSERTIONS
# ==========================================

# Test 3: Invalid password should be rejected
def test_negative_assertion(password_samples):

    for password in password_samples["invalid"]:

        result = validate_password(password)

        assert result != []


# Test 4: True Negative (TN)
# Expected invalid and actually rejected
@pytest.mark.parametrize(
    "password",
    [
        "abc",
        "password",
        "Strong123",
        "strong@123",
        "STRONG@123"
    ]
)
def test_true_negative(password):

    result = validate_password(password)

    assert result != []


# ==========================================
# 5. FALSE POSITIVE TESTING
# ==========================================

# Test 5: Prevent False Positive (FP)
# Invalid password must NOT be accepted

@pytest.mark.parametrize(
    "password",
    [
        "password",
        "abc",
        "Strong123",
        "strong@123"
    ]
)
def test_false_positive_prevention(password):

    result = validate_password(password)

    # Negative assertion:
    # Invalid password must be rejected

    assert result != []


# ==========================================
# 6. FALSE NEGATIVE TESTING
# ==========================================

# Test 6: Prevent False Negative (FN)
# Valid password must NOT be rejected

@pytest.mark.parametrize(
    "password",
    [
        "Strong@123",
        "Welcome#2026",
        "MySecure$Pass9"
    ]
)
def test_false_negative_prevention(password):

    result = validate_password(password)

    # Positive assertion:
    # Valid password must be accepted

    assert result == []


# ==========================================
# 7. EXISTING PASSWORD POLICY TESTS
# ==========================================

# Test 7: Minimum password length
def test_password_minimum_length():

    result = validate_password("Ab1!")

    assert any("at least 8 characters" in rule for rule in result)


# Test 8: Uppercase required
def test_uppercase_required():

    result = validate_password("strong@123")

    assert any("uppercase" in rule for rule in result)


# Test 9: Lowercase required
def test_lowercase_required():

    result = validate_password("STRONG@123")

    assert any("lowercase" in rule for rule in result)


# Test 10: Number required
def test_number_required():

    result = validate_password("Strong@abc")

    assert any("number" in rule for rule in result)


# Test 11: Special character required
def test_special_character_required():

    result = validate_password("Strong123")

    assert any("special character" in rule for rule in result)


# Test 12: Weak password rejected
def test_weak_password_rejected():

    result = validate_password("password")

    assert any("weak password" in rule for rule in result)


# Test 13: Weak password case-insensitive
def test_weak_password_case_insensitive():

    result = validate_password("PASSWORD")

    assert any("weak password" in rule for rule in result)


# Test 14: Multiple failed rules
def test_multiple_failed_rules():

    result = validate_password("abc")

    assert len(result) >= 4

    assert any("at least 8 characters" in rule for rule in result)
    assert any("uppercase" in rule for rule in result)
    assert any("number" in rule for rule in result)
    assert any("special character" in rule for rule in result)


# Test 15: Empty password
def test_empty_password():

    result = validate_password("")

    assert len(result) >= 5
