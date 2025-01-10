from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from qalamos.transliteration.transliterator import transliterate_text
import os

app = FastAPI()

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

origins = [
    "http://localhost:3000",
    "http://localhost:5000",
    "https://api.qalamos.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/")
def root():
    return {"message": "Welcome to the Qalamos API"}


@app.post("/transliterate/")
def transliterate(request: dict):
    text = request.get("text", "")
    if not text.strip():
        return {"error": "Input text cannot be empty"}
    return transliterate_text(text)
