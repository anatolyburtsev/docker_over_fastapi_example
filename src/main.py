from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/health")
def health_check():
    return {}


class PredictItemRequest(BaseModel):
    name: str
    id: int

@app.post("/predict/")
def predict(item: PredictItemRequest):
    return {"prediction": item.id * 10}
