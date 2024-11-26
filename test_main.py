from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_add_name():
    response = client.post("/add_name/", params={"name": "Матвій"})
    assert response.status_code == 200
    assert response.json() == {"message": "Ім'я 'Матвій' додано"}


def test_add_duplicate_name():
    client.post("/add_name/", params={"name": "Петро"})
    response = client.post("/add_name/", params={"name": "Петро"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Ім'я вже існує"}


def test_get_names():
    response = client.get("/get_name/")
    assert response.status_code == 200
    assert "Всі ім'я" in response.json()


def test_delete_name():
    client.post("/add_name/", params={"name": "Степан"})
    response = client.delete("/delete_name/2")
    assert response.status_code == 200
    assert response.json() == {"message": "Ім'я з індексом '2' видалено"}


def test_delete_non_existent_name():
    response = client.delete("/delete_name/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "таке ім'я не знайдено"}


def test_get_name_by_index():
    client.post("/add_name/", params={"name": "Марія"})
    response = client.get("/get_name_by_index/3")
    assert response.status_code == 200
    assert response.json() == {"name": "Марія"}


def test_get_non_existent_name_by_index():
    response = client.get("/get_name_by_index/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "Index not found"}
