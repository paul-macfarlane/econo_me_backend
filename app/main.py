from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.models.errors import ModelNotFoundError
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


@app.exception_handler(ModelNotFoundError)
async def model_not_found_error_handler(request, exc):
    return JSONResponse(status_code=exc.code, content={"message": exc.message})
