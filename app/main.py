from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import get_environment


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Check the current environment during the application startup
    current_env = get_environment()
    print(f"Starting application in {current_env} environment.")

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "Portfolio API"}
