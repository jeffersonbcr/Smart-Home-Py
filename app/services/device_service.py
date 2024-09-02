from fastapi import HTTPException
from app.models.device import Device
from app.schemas.device import DeviceCreate

devices = {}


def create_device(device: DeviceCreate):
    if device.device_id in devices:
        raise HTTPException(status_code=400, detail="Device already registered")
    new_device = Device(**device.dict())
    devices[device.device_id] = new_device
    return {"message": "Device registered successfully"}


def get_device(device_id: str):
    return devices.get(device_id)
