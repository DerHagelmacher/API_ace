from fastapi import FastAPI
from . import temp

app = FastAPI()

app.include_router(temp.router, prefix="/api")
