from fastapi import APIRouter, HTTPException
import math

router = APIRouter()

@router.get("/prime")
async def prime(limit: int):
    if limit < 2 or limit > 10_000:
        raise HTTPException(400, "Limit muss grösser als 2 und kleiner als 10000 sein")

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return {"primes": primes}
