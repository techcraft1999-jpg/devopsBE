from fastapi import FastAPI

app = FastAPI()

@app.get("/sayHello")
def say():
    return {"msg" : "Hello! World by TechCraft"}