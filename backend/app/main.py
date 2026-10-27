from fastapi import FastAPI

app = FastAPI(title="DayBook API")

@app.get("/")
def read_root():
  return {"message": "Welcome to DayBook"}