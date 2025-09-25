from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/temp")
async def temp(celsius: float | None = None, kelvin: float | None = None):
    if (celsius is None and kelvin is None) or (celsius is not None and kelvin is not None):
        raise HTTPException(400, "Nur einen Parameter angeben")
    if celsius is not None:
        return {"celsius": celsius, "kelvin": celsius + 273.15}
    return {"kelvin": kelvin, "celsius": kelvin - 273.15}
