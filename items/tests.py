import pytest
from conftest import default_item
import logging

@pytest.mark.django_db  
def test_create_item(api_client, headers) -> None:  
    
    target_url = "/api/items/"
    test_url = "/api/items/1/"

    payload = {
        "title": "vocab #1",
        "description": "dummy data"
    }
  
    # create new item
    response_create = api_client.post(
        target_url,
        data = payload,
        headers = headers
    )
    
    assert response_create.status_code == 201

    # read new item
    response_read = api_client.get(
        test_url,
        headers = headers
    )
    assert response_read.data['title'] == payload["title"]
    assert response_read.data['description'] == payload["description"]
    assert response_read.status_code == 200


@pytest.mark.django_db  
def test_read_item(api_client, headers_with_item) -> None:
    target_url = "/api/items/2/"
    
    # read user
    response_read = api_client.get(
        target_url,
        headers = headers_with_item
    )
    assert response_read.data["title"] == default_item["title"]
    assert response_read.data["description"] == default_item["description"]
    assert response_read.status_code == 200

@pytest.mark.django_db  
def test_update_item(api_client, headers_with_item) -> None:
    url = "/api/items/3/"

    payload = {
        "title": "vocab #3",
        "description": "dummy data, once again"
    }
    
    # update item
    response_update = api_client.patch(
        url,
        data = payload,
        headers = headers_with_item
    )
    assert response_update.status_code == 200

    # read updated item
    response_read = api_client.get(
        url,
        headers = headers_with_item
    )
    assert response_read.data["title"] == payload["title"]
    assert response_read.data["description"] == payload["description"]
    assert response_read.status_code == 200

@pytest.mark.django_db
def test_delete_item(api_client, headers_with_item) -> None:
    target_url = "/api/items/4/"
    
    # delete item
    response_delete = api_client.delete(
        target_url,
        headers = headers_with_item
    )
    assert response_delete.status_code == 204
