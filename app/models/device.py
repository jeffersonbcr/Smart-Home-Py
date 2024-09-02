from typing import List


class Device:
    def __init__(self, device_id: str, device_type: str, operations: List[str]):
        self.device_id = device_id
        self.device_type = device_type
        self.operations = operations
        self.status = {}
