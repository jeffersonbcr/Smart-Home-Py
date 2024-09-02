from fastapi import HTTPException
from app.models.environment import Environment
from app.schemas.environment import EnvironmentCreate
from app.services.device_service import devices

environments = {}


def create_environment(environment: EnvironmentCreate):
    if environment.name in environments:
        raise HTTPException(status_code=400, detail="Environment already exists")
    new_environment = Environment(**environment.dict())
    environments[environment.name] = new_environment
    return {"message": "Environment created successfully"}


def add_device_to_environment(name: str, device_id: str):
    if name not in environments:
        raise HTTPException(status_code=404, detail="Environment not found")
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    environments[name].add_device(devices[device_id])
    return {"message": "Device added to environment"}


def remove_device_from_environment(name: str, device_id: str):
    if name not in environments:
        raise HTTPException(status_code=404, detail="Environment not found")
    environments[name].remove_device(device_id)
    return {"message": "Device removed from environment"}


def execute_command_on_environment(name: str, command: str):
    if name not in environments:
        raise HTTPException(status_code=404, detail="Environment not found")
    environments[name].execute_command(command)
    return {
        "message": f"Command '{command}' executed on all devices in environment '{name}'"
    }
