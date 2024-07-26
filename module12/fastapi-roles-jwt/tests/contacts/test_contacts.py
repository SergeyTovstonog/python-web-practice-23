import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.contacts.schemas import ContactCreate, ContactUpdate


@pytest.mark.asyncio
async def test_create_contact(client: TestClient, db_session: AsyncSession):
    response = client.post(
        "/contacts/",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone_number": "1234567890",
            "birthday": "2000-01-01",
            "additional_info": "Test info",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"


@pytest.mark.asyncio
async def test_read_contacts(client: TestClient, db_session: AsyncSession):
    response = client.get("/contacts/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_read_contact(client: TestClient, db_session: AsyncSession):
    response = client.post(
        "/contacts/",
        json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "phone_number": "0987654321",
            "birthday": "2001-01-01",
            "additional_info": "Another test info",
        },
    )
    contact_id = response.json()["id"]

    response = client.get(f"/contacts/{contact_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Jane"
    assert data["last_name"] == "Doe"


@pytest.mark.asyncio
async def test_update_contact(client: TestClient, db_session: AsyncSession):
    response = client.post(
        "/contacts/",
        json={
            "first_name": "Jake",
            "last_name": "Smith",
            "email": "jake.smith@example.com",
            "phone_number": "1122334455",
            "birthday": "2002-01-01",
            "additional_info": "Initial info",
        },
    )
    contact_id = response.json()["id"]

    response = client.put(
        f"/contacts/{contact_id}",
        json={
            "first_name": "Jake",
            "last_name": "Smith",
            "email": "jake.smith@example.com",
            "phone_number": "1122334455",
            "birthday": "2002-01-01",
            "additional_info": "Updated info",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["additional_info"] == "Updated info"


@pytest.mark.asyncio
async def test_delete_contact(client: TestClient, db_session: AsyncSession):
    response = client.post(
        "/contacts/",
        json={
            "first_name": "Tom",
            "last_name": "Brown",
            "email": "tom.brown@example.com",
            "phone_number": "2233445566",
            "birthday": "2003-01-01",
            "additional_info": "Delete me",
        },
    )
    contact_id = response.json()["id"]

    response = client.delete(f"/contacts/{contact_id}")
    assert response.status_code == 200

    response = client.get(f"/contacts/{contact_id}")
    assert response.status_code == 404
