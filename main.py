from fastapi import FastAPI
from app.routes.event_routes import router as event_router

app = FastAPI(
    title="Personalized Networking Assistant"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Personalized Networking Assistant"
    }

app.include_router(event_router)