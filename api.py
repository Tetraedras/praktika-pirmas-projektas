from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

history = []

class Question(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"message": "Serveris veikia!"}

@app.post("/ask")
def ask_ai(data: Question):
    answer = f"Mock atsakymas į: {data.question}"

    history.append({
        "question": data.question,
        "answer": answer
    })

    return {
        "question": data.question,
        "answer": answer
    }

@app.get("/history")
def get_history():
    return history

@app.delete("/history")
def clear_history():
    history.clear()
    return {"message": "History cleared"}