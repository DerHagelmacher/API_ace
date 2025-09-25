from fastapi import FastAPI
from . import temp, prime, number

app = FastAPI()

app.include_router(temp.router, prefix="/api")
app.include_router(prime.router, prefix="/api")
app.include_router(number.router, prefix="/api")

