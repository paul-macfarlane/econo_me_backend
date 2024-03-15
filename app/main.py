from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

from app.routers.transactions import router as transactions_router

app = FastAPI()

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(transactions_router, prefix="/transactions", tags=["transactions"])

app.include_router(api_v1_router)


class HealthCheckResponse(BaseModel):
    message: str


@app.get("/", response_model=HealthCheckResponse, tags=["health"])
def health_check():
    return {"message": "Healthy"}
