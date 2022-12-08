import os

import uvicorn
from fastapi import FastAPI

from app.database import tables
from app.routers import items
from app.routers import projects

# import datetime


app = FastAPI()
app.include_router(projects.router)
app.include_router(items.router)

tables.create_tables()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"msg": "Hello World"}


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    log_level = os.getenv("LOG_LEVEL", "info")
    uvicorn.run(app, host=host, port=port, log_level=log_level)
