from fastapi import FastAPI
from fastapi.testclient import TestClient

from router import api_v1_router


app = FastAPI()
app.include_router(api_v1_router, prefix="/api/v1")

# 传入app实例话TestClient
client = TestClient(app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)