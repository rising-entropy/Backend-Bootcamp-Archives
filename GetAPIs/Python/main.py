from fastapi import FastAPI
import json
app = FastAPI()

f = open('data.json')
theData = json.load(f)


@app.get("/") # declare a route, type (GET, POST)
def read_root():
    return {"message": "Hello"}

# get all the users
@app.get("/all-users")
def allUsers():
    return theData

# get a particular user
@app.get("/user/{id}")
def particularUser(id: int):
    for d in theData:
        if d['id'] == id:
            return d
    return {"message": "User does not exist"}


# get random users - count in URL
@app.get("/random-users/{count}")
def randomUsers(count: int):
    return {"message": "User does not exist"}