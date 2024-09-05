from fastapi import APIRouter, HTTPException
from app.api.v1.endpoints.devices import Command
from app.models.environment import Environment
from app.schemas.environment import EnvironmentCreate
from app.services.environment_service import (
    create_environment,
    add_device_to_environment,
    remove_device_from_environment,
    execute_command_on_environment,
)

from pydantic import BaseModel

router = APIRouter()


class DeviceID(BaseModel):
    device_id: str


@router.post("/")
async def create_new_environment(environment: EnvironmentCreate):
    return create_environment(environment)


@router.post("/{name}/devices/")
async def add_device(name: str, device: DeviceID):
    return add_device_to_environment(name, device.device_id)


@router.post("/{name}/devices/remove")
async def remove_device(name: str, device_id: str):
    return remove_device_from_environment(name, device_id)


@router.post("/{name}/command")
async def send_command_to_environment(name: str, command: Command):
    return execute_command_on_environment(name, command.command)
