from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import temp, prime, number

app = FastAPI()
app.include_router(temp.router, prefix="/api")
app.include_router(prime.router, prefix="/api")
app.include_router(number.router, prefix="/api")

app.mount("/api/ui", StaticFiles(directory="app/static", html=True), name="ui")
