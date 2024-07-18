from fastapi import APIRouter
from workout_api.atleta.controler import router as atleta

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
