
import asyncio
from fastapi import FastAPI
import httpx


app = FastAPI()

async def fetch_address(address: str):
    url = "https://zipcloud.ibsnet.co.jp/api/search"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params={"zipcode": address})
        return response.json()


@app.get("/address/")
async def read_address():
    zip_codes = [
        "1000001",
        "1500001",
        "1600001",
        "1700001",
    ]
    return await asyncio.gather(*(fetch_address(zip_code) for zip_code in zip_codes))
