import pytest
from auth import AuthService

@pytest.fixture
def auth_service():
    # Setup: criar uma instância do serviço de autenticação
    service = AuthService()
    return service

def test_login_success(auth_service):
    assert auth_service.login("user1", "password1") == True

def test_login_failure(auth_service):
    assert auth_service.login("user1", "wrongpassword") == False

def test_login_nonexistent_user(auth_service):
    assert auth_service.login("nonexistentuser", "password1") == False
