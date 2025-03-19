import json
import pytest
from unittest.mock import patch


def test_login(client):
    # Patch the `services` dict so that `services["auth"]["login_user"]` returns our mock response
    with patch("api.routes.accounts.services", {"auth": {"login_user": lambda data: ("Login successful", 200)}}):
        payload = {"username": "testuser", "password": "testpass"}
        response = client.post("/api/accounts/login/", json=payload)
        assert response.status_code == 200
        assert b"Login successful" in response.data


def test_create_account(client):
    with patch("api.routes.accounts.services", {"auth": {"create_user": lambda data: ("Account created", 201)}}):
        payload = {"username": "newuser", "password": "somepass"}
        response = client.post("/api/accounts/create/", json=payload)
        assert response.status_code == 201
        assert b"Account created" in response.data


def test_edit_password(client):
    with patch("api.routes.accounts.services", {"auth": {"edit_user_password": lambda data: ("Password updated", 200)}}):
        payload = {"old_password": "oldpass", "new_password": "newpass"}
        response = client.post("/api/accounts/change_password/", json=payload)
        assert response.status_code == 200
        assert b"Password updated" in response.data


def test_edit_more_info(client):
    with patch("api.routes.accounts.services", {"auth": {"update_user_info": lambda data: ("User info updated", 200)}}):
        payload = {"bio": "Updated Bio"}
        response = client.post("/api/accounts/edit_more_info/", json=payload)
        assert response.status_code == 200
        assert b"User info updated" in response.data


def test_auth(client):
    # Mock the function that checks if a user is logged in
    with patch("api.routes.accounts.services", {"auth": {"authenticate_user": lambda: ("Authenticated", 200)}}):
        response = client.get("/api/accounts/auth/")
        assert response.status_code == 200
        assert b"Authenticated" in response.data


def test_logout(client):
    # The logout route doesn't call any service—it just clears a cookie.
    response = client.post("/api/accounts/logout/")
    assert response.status_code == 200
    assert b"Logout successful" in response.data


def test_get_user_difficulty(client):
    with patch("api.routes.accounts.services", {"auth": {"get_difficulty": lambda: ("Current difficulty: Intermediate", 200)}}):
        response = client.get("/api/accounts/difficulty/")
        assert response.status_code == 200
        assert b"Current difficulty: Intermediate" in response.data


def test_get_user_profile(client):
    # Provide mocks for both GET and POST calls
    with patch("api.routes.accounts.services", {"auth": {
        "get_profile": lambda: ("Profile data", 200),
        "update_profile": lambda data: ("Profile updated", 200)
    }}):
        # Test GET
        response_get = client.get("/api/accounts/profile/")
        assert response_get.status_code == 200
        assert b"Profile data" in response_get.data

        # Test POST
        response_post = client.post("/api/accounts/profile/", json={"bio": "new bio"})
        assert response_post.status_code == 200
        assert b"Profile updated" in response_post.data
