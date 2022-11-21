from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/student/")
def students():
    return {"status": "success"}

@app.get("/")
def root():
    return {"message": "Hello World"}
