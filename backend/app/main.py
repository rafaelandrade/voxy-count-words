from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import count_words_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(count_words_router.router)


@app.get("/")
def read_root():
    return {"message": "Hello World!"}
