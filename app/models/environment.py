from typing import List
from app.models.device import Device


class Environment:
    def __init__(self, name: str):
        self.name = name
        self.devices: List[Device] = []

    def add_device(self, device: Device):
        self.devices.append(device)

    def remove_device(self, device_id: str):
        self.devices = [d for d in self.devices if d.device_id != device_id]

    def execute_command(self, command: str):
        for device in self.devices:
            device.status["last_command"] = command
