from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from main_service import app
import httpx

client = TestClient(app)


def test_get_user_by_id():
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Leanne Graham",
        "email": "Sincere@april.biz"
    }


def test_get_incorrect_user():
    response = client.get("user/11")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_invalid_input():
    response = client.get("user/a")
    assert response.status_code == 404
