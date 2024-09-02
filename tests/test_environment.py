from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_environment():
    response = client.post("/v1/environments/", json={"name": "living_room"})
    assert response.status_code == 200
    assert response.json() == {"message": "Environment created successfully"}


def test_add_device_to_environment():
    response = client.post(
        "/v1/environments/living_room/devices/", json={"device_id": "1234"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Device added to environment"}


def test_send_command_to_environment():
    response = client.post(
        "/v1/environments/living_room/command", json={"command": "open"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Command 'open' executed on all devices in environment 'living_room'"
    }
