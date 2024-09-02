from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_device():
    response = client.post(
        "/v1/devices/",
        json={
            "device_id": "1234",
            "device_type": "curtain",
            "operations": ["open", "close"],
        },
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Device registered successfully"}


def test_send_command():
    response = client.post("/v1/devices/1234/command", json={"command": "open"})
    assert response.status_code == 200
    assert response.json() == {"message": "Command 'open' sent to device 1234"}
