# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/src")
async def establish_connection():
    return {"status": "Connection established"}
