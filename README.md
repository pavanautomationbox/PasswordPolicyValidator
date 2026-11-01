# Password Policy Validator

## 1. Project Description

The Password Policy Validator is a simple Python application that checks whether a password follows predefined security rules.

The application checks password length, uppercase letters, lowercase letters, numbers, special characters, and known weak passwords.

It displays whether the password is accepted or rejected and shows all failed validation rules.

The application does not save or log passwords.

---

## 2. Project Structure

```text
PasswordPolicyValidator/
│
├── bot.py
├── test_bot.py
├── test_functional.py
├── test_security.py
└── README.md
```

### File Description

- bot.py: Main Python application.
- test_bot.py: Contains unit test cases.
- test_functional.py: Contains functional test cases.
- test_security.py: Contains security test cases.
- README.md: Project documentation.

---

## 3. Technologies Used

- Python 3
- Pytest
- VS Code
- Python getpass module

No external Python libraries are required except pytest for testing.

---

## 4. Password Policy Rules

The application follows these password rules:

1. Password must contain at least 8 characters.
2. Password must contain at least one uppercase letter.
3. Password must contain at least one lowercase letter.
4. Password must contain at least one number.
5. Password must contain at least one special character.
6. Password must not match any password in the weak password list.

### Expected Output

PASS:
The password satisfies all security rules.

FAIL:
The password does not satisfy the rules.
All failed rules are displayed to the user.

---

# 5. Unit Testing

## What is Unit Testing?

Unit testing checks individual functions or small parts of a Python program to make sure they work correctly.

In this project, unit testing checks the password validation function separately.

## Tool Used

Pytest is used to execute automated unit tests.

## File Used

test_bot.py

## Unit Test Cases

| Test Case                 | Expected Result           |
| ------------------------- | ------------------------- |
| Strong password           | Password accepted         |
| Short password            | Password rejected         |
| Missing uppercase letter  | Validation failed         |
| Missing lowercase letter  | Validation failed         |
| Missing number            | Validation failed         |
| Missing special character | Validation failed         |
| Known weak password       | Password rejected         |
| Multiple failed rules     | All failed rules returned |

## Expected Result

All 8 unit tests should pass if the password validation function works correctly.

---

# 6. Functional Testing

## What is Functional Testing?

Functional testing checks whether the application performs its expected functions correctly.

In this project, functional testing verifies that the password validator follows all defined password policy rules.

## Tool Used

Pytest is used to perform automated functional testing.

## File Used

test_functional.py

## Functional Test Cases

| Test Case                                | Expected Result            |
| ---------------------------------------- | -------------------------- |
| Valid password                           | Password accepted          |
| Password below minimum length            | Password rejected          |
| Password without uppercase               | Validation failed          |
| Password without lowercase               | Validation failed          |
| Password without number                  | Validation failed          |
| Password without special character       | Validation failed          |
| Weak password                            | Password rejected          |
| Weak password with different letter case | Password rejected          |
| Password with multiple rule failures     | All failed rules displayed |
| Empty password                           | Password rejected          |

## Expected Result

All 10 functional tests should pass.

The application should correctly identify valid and invalid passwords.

---

# 7. Security Testing

## What is Security Testing?

Security testing checks whether an application handles sensitive information safely.

In this project, security testing focuses on protecting passwords entered by users.

## Tool Used

Pytest is used to perform automated security testing.

## Python Features Used in Security Testing

### 1. monkeypatch

- Temporarily replaces a function during testing.
- Used to simulate password input.
- Helps test application behaviour without manually entering passwords.

### 2. capsys

- Captures the output displayed in the terminal.
- Used to check that passwords are not displayed on the screen.

### 3. tmp_path

- Creates a temporary directory for testing.
- Used to check whether the application creates files containing saved passwords.

### 4. caplog

- Captures application log messages.
- Used to check that passwords are not written to logs.

### 5. getpass

- Python module used to hide password input.
- Prevents the password from appearing visibly while the user types it in a supported terminal.

## Security Test Cases

| Test Case                   | Expected Result                                   |
| --------------------------- | ------------------------------------------------- |
| Password visibility test    | Password should not appear in terminal output     |
| Password storage test       | Password should not be saved in files             |
| Password logging test       | Password should not appear in application logs    |
| Hidden input test           | Application should use getpass for password input |
| Weak password security test | Known weak password should be rejected            |

## Expected Result

All 5 security tests should pass.

The application should not display, log, or save the entered password.

Note: These tests provide basic security checks for an educational project. They do not guarantee complete protection against memory inspection or other advanced attacks.

---

# 8. How to Install Pytest

Open the terminal in VS Code and execute:

pip install pytest

Check the installation:

pytest --version

---

# 9. How to Run the Tests

### Run all tests

pytest -v

### Run unit tests only

pytest -v test_bot.py

### Run functional tests only

pytest -v test_functional.py

### Run security tests only

pytest -v test_security.py

---

# 10. Expected Testing Summary

| Testing Type       | Test Cases | Expected Result |
| ------------------ | ---------: | --------------- |
| Unit Testing       |          8 | 8 Passed        |
| Functional Testing |         10 | 10 Passed       |
| Security Testing   |          5 | 5 Passed        |
| Total              |         23 | 23 Passed       |

---

# 11. Project Conclusion

The Password Policy Validator successfully checks passwords against predefined security rules.

Unit testing verifies individual password validation functions.

Functional testing verifies that all password policy requirements work correctly.

Security testing checks that passwords are not displayed, saved, or logged by the application.

Pytest makes it easier to automate testing and identify errors.

This project demonstrates basic Python programming, password validation, automated testing, and introductory application security concepts.
