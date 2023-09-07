import pytest

from rest_framework.test import APIClient  

@pytest.fixture(scope="function")  
def api_client() -> APIClient:  
    yield APIClient()

default_user = {
    "email": "test@user.com",  
    "password": "testPassword"
}

default_item = {
    "title": "vocab #2",
    "description": "dummy data, again",
    "stage": "0"
}

@pytest.fixture(scope="function")
def headers(api_client):
    create_user_url = "/api/users/"
    login_url = "/api/auth/"

    payload = default_user

    payload_with_confirm_password = {  
        **payload,
        "confirm_password": default_user["password"] 
    }
    
    # create user
    api_client.post(
        create_user_url,
        data = payload_with_confirm_password
    )

    # login with user
    response_login = api_client.post(
        login_url,
        data = payload
    )

    access_token = response_login.data['access']

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    return headers

@pytest.fixture(scope="function")
def headers_with_item(api_client, headers):
    target_url = "/api/items/"

    payload = default_item
    
    # create new item
    api_client.post(
        target_url,
        data = payload,
        headers = headers
    )

    return headers