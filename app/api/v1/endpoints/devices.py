from fastapi import APIRouter, HTTPException
from app.models.device import Device
from app.schemas.device import DeviceCreate
from app.services.device_service import create_device, get_device
from pydantic import BaseModel

router = APIRouter()


class Command(BaseModel):
    command: str


@router.post("/")
async def register_device(device: DeviceCreate):
    return create_device(device)


@router.get("/{device_id}")
async def get_device_status(device_id: str):
    device = get_device(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device.status


@router.post("/{device_id}/command")
async def send_command(device_id: str, command: Command):
    device = get_device(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    # Simula a execução do comando no dispositivo
    device.status["last_command"] = command.command
    return {"message": f"Command '{command.command}' sent to device {device_id}"}
