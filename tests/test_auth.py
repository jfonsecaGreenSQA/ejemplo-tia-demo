"""Tests para módulo auth.py - SIMPLIFICADOS para demo"""
import pytest
from src.auth import AuthManager

# Solo 5 tests representativos para demo rápida
def test_register_user():
    auth = AuthManager()
    result = auth.register_user('testuser', 'password123', 'test@example.com')
    assert result == True

def test_register_duplicate_user():
    auth = AuthManager()
    auth.register_user('testuser', 'password123', 'test@example.com')
    with pytest.raises(ValueError):
        auth.register_user('testuser', 'pass456', 'other@example.com')

def test_login_success():
    auth = AuthManager()
    auth.register_user('testuser', 'password123', 'test@example.com')
    session_id = auth.login('testuser', 'password123')
    assert session_id.startswith('SESSION-')

def test_login_wrong_password():
    auth = AuthManager()
    auth.register_user('testuser', 'password123', 'test@example.com')
    with pytest.raises(ValueError):
        auth.login('testuser', 'wrongpass')

def test_logout():
    auth = AuthManager()
    auth.register_user('testuser', 'password123', 'test@example.com')
    session_id = auth.login('testuser', 'password123')
    result = auth.logout(session_id)
    assert result == True
