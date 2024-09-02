from pydantic import BaseModel
from typing import List


class DeviceCreate(BaseModel):
    device_id: str
    device_type: str
    operations: List[str]
