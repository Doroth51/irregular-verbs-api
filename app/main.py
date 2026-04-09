from fastapi import FastAPI
from app.routers import verbs

app = FastAPI(
    title="Irregular Verbs API",
    version="1.0",
)

app.include_router(verbs.router)


@app.get("/")
def root():
    return {"message": "API is running"}
