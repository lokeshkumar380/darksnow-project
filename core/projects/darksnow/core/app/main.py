from fastapi import FastAPI
from .router import designer

app = FastAPI()

app.include_router(designer.router)


