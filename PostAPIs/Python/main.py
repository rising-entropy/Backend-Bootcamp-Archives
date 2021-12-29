from fastapi import FastAPI
import json
import random
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

def getRandomIndicesArray(countOfList, requiredCount):
    requiredIndices = []
    while True:
        r1 = random.randint(1, countOfList)
        if r1 not in requiredIndices:
            requiredIndices.append(r1)
        if len(requiredIndices) == requiredCount:
            return requiredIndices

# get random users - count in URL
@app.get("/random-users/{count}")
def randomUsers(count: int):
    theRandomIndices = getRandomIndicesArray(len(theData), count)
    requiredObjects = []
    for i in theRandomIndices:
        requiredObjects.append(theData[i])
    return requiredObjects

# post - create a new user

# put - update a user (getting its ID)

# delete - delete a user (getting its ID)