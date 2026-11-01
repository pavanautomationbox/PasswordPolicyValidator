
# Provides secure, hidden password input by masking characters as they are typed.
# getpass.getpass() is used below to collect the password without echoing it to the terminal.
import getpass

# -----------------------------------
# PASSWORD POLICY CONFIGURATION
# -----------------------------------

MIN_LENGTH = 8

REQUIRE_UPPERCASE = True
REQUIRE_LOWERCASE = True
REQUIRE_NUMBER = True
REQUIRE_SPECIAL = True

# Small list of weak demo passwords
WEAK_PASSWORDS = [
    "password",
    "12345678",
    "qwerty123",
    "admin123",
    "welcome123"
]


# -----------------------------------
# PASSWORD VALIDATION FUNCTION
# -----------------------------------

def validate_password(password):

    failed_rules = []

    # Rule 1: Minimum length
    if len(password) < MIN_LENGTH:
        failed_rules.append(
            f"Password must contain at least {MIN_LENGTH} characters."
        )

    # Rule 2: Uppercase letter
    if REQUIRE_UPPERCASE and not any(char.isupper() for char in password):
        failed_rules.append(
            "Password must contain at least one uppercase letter."
        )

    # Rule 3: Lowercase letter
    if REQUIRE_LOWERCASE and not any(char.islower() for char in password):
        failed_rules.append(
            "Password must contain at least one lowercase letter."
        )

    # Rule 4: Number
    if REQUIRE_NUMBER and not any(char.isdigit() for char in password):
        failed_rules.append(
            "Password must contain at least one number."
        )

    # Rule 5: Special character
    special_characters = "!@#$%^&*()-_+=<>?/"

    if REQUIRE_SPECIAL and not any(
        char in special_characters for char in password
    ):
        failed_rules.append(
            "Password must contain at least one special character."
        )

    # Rule 6: Check weak passwords
    if password.lower() in WEAK_PASSWORDS:
        failed_rules.append(
            "Password is present in the weak password list."
        )

    return failed_rules


# -----------------------------------
# MAIN PROGRAM
# -----------------------------------

def main():

    print("=" * 40)
    print("     PASSWORD POLICY VALIDATOR")
    print("=" * 40)

    # Get password without displaying it on screen
    password = getpass.getpass("Enter your password: ")

    # Validate password
    failed_rules = validate_password(password)

    print("\n========== VALIDATION RESULT ==========")

    if len(failed_rules) == 0:

        print("RESULT: PASSWORD ACCEPTED")
        print("Your password satisfies all security rules.")

    else:

        print("RESULT: PASSWORD REJECTED")
        print("\nFailed Rules:")

        for rule in failed_rules:
            print("- " + rule)

    print("\nPassword was not saved or logged.")
    print("=" * 40)


# Start the program
if __name__ == "__main__":
    main()
