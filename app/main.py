from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.models.errors import ModelNotFoundException, UnauthenticatedErrorException, UserAlreadyExistsException, \
    ResourceAlreadyExistsException
from app.routers.auth import router as auth_router
from app.routers.transactions import router as transactions_router
from app.routers.categories import router as categories_router

app = FastAPI()

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_v1_router.include_router(transactions_router, prefix="/transactions", tags=["transactions"])
api_v1_router.include_router(categories_router, prefix="/categories", tags=["categories"])

app.include_router(api_v1_router)


class HealthCheckResponse(BaseModel):
    message: str


@app.get("/", response_model=HealthCheckResponse, tags=["health"])
def health_check():
    return {"message": "Healthy"}


@app.exception_handler(UnauthenticatedErrorException)
async def unauthenticated_error_handler(request, exc):
    return JSONResponse(status_code=401, content={"message": exc.message})


@app.exception_handler(ModelNotFoundException)
async def model_not_found_error_handler(request, exc):
    return JSONResponse(status_code=exc.code, content={"message": exc.message})


@app.exception_handler(ResourceAlreadyExistsException)
async def resource_already_exists_error_handler(request, exc):
    return JSONResponse(status_code=exc.code, content={"message": exc.message})


@app.exception_handler(UserAlreadyExistsException)
async def user_already_exists_error_handler(request, exc):
    return JSONResponse(status_code=exc.code, content={"message": exc.message})


@app.exception_handler(Exception)
async def generic_error_handler(request, exc):
    return JSONResponse(status_code=500, content={"message": "Internal server error"})
