from fastapi import FastAPI
import json
import random
import jwt
app = FastAPI()
from pydantic import BaseModel
from datetime import datetime, timedelta

f = open('data.json')
theData = json.load(f)

SECRET = "Aman"
ALGORITHM = 'HS256'
EXPIRY = 600


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
class User(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str

@app.post("/create-user")
def newUser(user: User):
    user = dict(user)
    user["id"] = len(theData)+1
    theData.append(user)
    return user

# put - update a user (getting its ID)
@app.put("/user/{id}")
def updateUser(id: int, user: User):
    for i in range(len(theData)):
        if theData[i]["id"] == id:
            # make a new copy of that updated instance
            theUpdatedUser = dict(user)
            # pass the same ID
            theUpdatedUser["id"] = id
            #put it back in place of old instance
            theData[i] = theUpdatedUser
            return theUpdatedUser
    return {"message": "User does not exist"}
            

# delete - delete a user (getting its ID)
@app.delete("/user/{id}")
def deleteUser(id: int):
    for i in range(len(theData)):
        if theData[i]["id"] == id:
            del theData[i]
            return {
                "message": "User deleted successfully."
            }
    return {"message": "User does not exist"}

# Login API - Validate the User
# If authenticated - Return a Token

class Login(BaseModel):
    email: str
    password: str

@app.post("/login")
def loginUser(body: Login):
    thatEmail = body.email
    thatPassword = body.password
    for i in theData:
        if i["email"] == thatEmail:
            if i["password"] == thatPassword:
                payload = {
                    "exp": datetime.utcnow() + timedelta(seconds = EXPIRY),
                    "data": thatEmail
                }
                token = jwt.encode(payload,SECRET, ALGORITHM)
                return {
                    "message": "Login Successful",
                    "email": i["email"],
                    "token": token
                }
            return {"message": "Wrong Password"}
    return {"message": "Email does not exist"}

# Check Token API
# Return True if valid else False