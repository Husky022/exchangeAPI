from fastapi import FastAPI
from utils.exchange import available_rates, get_currency

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to exchange API, /rates - получение конвертации, /available-rates - доступные валюты"}


@app.get("/available-rates")
async def all_rates():
    return {"result": available_rates()}


@app.get("/rates")
async def exchange(from_: str, to: str, value: int):
    return {"result": get_currency(from_, to, value)}
