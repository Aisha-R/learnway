import pytest
from conftest import default_user

@pytest.mark.django_db  
def test_create_user(api_client) -> None:  

    target_url = "/api/users/"
    login_url = "/api/auth/"

    payload = default_user

    payload_with_confirm_password = {  
        **payload,
        "confirm_password": "testPassword"  
    }
  
    # create new user
    response_create = api_client.post(
        target_url,
        data = payload_with_confirm_password
    )
    assert response_create.status_code == 201

    # login with new user
    response_login = api_client.post(
        login_url,
        data = payload
    )
    assert response_login.data['access']
    assert response_login.data['refresh']
    assert response_login.status_code == 200

@pytest.mark.django_db  
def test_read_user(api_client, headers) -> None:
    target_url = "/api/users/2/"
    
    # read user
    response_read = api_client.get(
        target_url,
        headers = headers
    )
    assert response_read.data["email"] == default_user["email"]
    assert response_read.status_code == 200

@pytest.mark.django_db  
def test_update_user(api_client, headers) -> None:
    target_url = "/api/users/3/"
    login_url = "/api/auth/"

    payload = {
        "password": "newTestPassword",
        "confirm_password": "newTestPassword"
    }
    
    # update user password
    response_update = api_client.patch(
        target_url,
        data = payload,
        headers = headers
    )
    assert response_update.status_code == 200

    login_payload = {
        "email": "test@user.com",
        "password": payload["password"]
    }

    # login with new password
    response_login = api_client.post(
        login_url,
        data = login_payload
    )
    assert response_login.status_code == 200

@pytest.mark.django_db
def test_delete_user(api_client, headers) -> None:
    target_url = "/api/users/4/"
    
    # delete user
    response_delete = api_client.delete(
        target_url,
        headers = headers
    )
    assert response_delete.status_code == 204