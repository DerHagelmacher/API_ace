from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/number")
async def number(n: int):
    if n < 0 or n > 50:
        raise HTTPException(400, "n muss zwischen 0 und 50 liegen")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return {"number": a}
