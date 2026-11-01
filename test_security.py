
import bot


# Test 1: Password should not appear in terminal output
def test_password_not_displayed(monkeypatch, capsys):

    secret_password = "MySecret@123"

    # Simulate password entry
    monkeypatch.setattr(
        bot.getpass,
        "getpass",
        lambda prompt: secret_password
    )

    # Run application
    bot.main()

    # Capture terminal output
    output = capsys.readouterr()

    # Password must not appear in output
    assert secret_password not in output.out
    assert secret_password not in output.err


# Test 2: Password should not be saved in files
def test_password_not_saved(monkeypatch, tmp_path):

    secret_password = "MySecret@123"

    # Use a temporary folder
    monkeypatch.chdir(tmp_path)

    # Simulate password entry
    monkeypatch.setattr(
        bot.getpass,
        "getpass",
        lambda prompt: secret_password
    )

    # Run application
    bot.main()

    # Check that no files were created
    files = list(tmp_path.iterdir())

    assert files == []


# Test 3: Password should not be written to logs
def test_password_not_logged(monkeypatch, caplog):

    secret_password = "MySecret@123"

    monkeypatch.setattr(
        bot.getpass,
        "getpass",
        lambda prompt: secret_password
    )

    # Run application
    bot.main()

    # Check captured application logs
    assert secret_password not in caplog.text


# Test 4: Application should use hidden password input
def test_hidden_password_input(monkeypatch):

    secret_password = "MySecret@123"

    # Track whether getpass is called
    called = []

    def fake_getpass(prompt):
        called.append(True)
        return secret_password

    monkeypatch.setattr(
        bot.getpass,
        "getpass",
        fake_getpass
    )

    bot.main()

    assert len(called) == 1


# Test 5: Weak passwords must be rejected
def test_weak_password_security():

    result = bot.validate_password("password")

    assert len(result) > 0
    assert any("weak password" in rule for rule in result)
