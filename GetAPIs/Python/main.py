from fastapi import FastAPI
app = FastAPI()


@app.get("/") # declare a route, type (GET, POST)
def read_root():
    return {"Hello": "World"}