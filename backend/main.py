from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Criminal Management System API Running"}
