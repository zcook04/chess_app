from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api_v1.api import router as api_router

app = FastAPI()

allow_origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router, prefix="/api/v1")