from fastapi import FastAPI

api = FastAPI()


@api.get("/")
def read_root():
    return {"message": "Root endpoint"}
