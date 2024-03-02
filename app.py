# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/api/connect")
async def establish_connection():
    return {"status": "Connection established"}
