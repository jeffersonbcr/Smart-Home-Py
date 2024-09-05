from fastapi import FastAPI
from app.api.v1.endpoints import devices, environments
import uvicorn

app = FastAPI()

app.include_router(devices.router, prefix="/v1/devices", tags=["devices"])
app.include_router(
    environments.router, prefix="/v1/environments", tags=["environments"]
)

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)
