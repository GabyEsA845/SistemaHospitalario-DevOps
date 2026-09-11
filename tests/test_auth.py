from src.auth import login

def test_login_exitoso():
    assert login("admin", "1234") is True

def test_login_fallido():
    assert login("admin", "incorrecta") is False