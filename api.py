from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Serveris veikia!"}

@app.get("/hello")
def say_hello(name: str = "drauge"):
    return {"message": f"Sveikas, {name}!"}

@app.get("/sum")
def calculate_sum(a: int, b: int):
    return {"result": a + b}