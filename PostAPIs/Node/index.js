const express = require("express");
const app = express();

const theData = require("./data.json");

app.use(express.json());

app.get("/", (req, res)=>{
    res.json({message: "Hello"})
});

// get all the users
app.get("/all-users", (req, res)=>{
    res.json(theData)
})

// get a particular user
app.get("/user/:id", (req, res)=>{
    let id = parseInt(req.params.id);
    for(let i=0; i<theData.length; i++)
    {
        if(theData[i].id === id)
        {
            res.json(theData[i])
        }
    }
    res.json({"message": "User does not exist"})
});

const getRandomIndicesArray = (countOfList, requiredCount) => {
    let requiredIndices = [];
    while(true)
    {
        let aRandomNumber = Math.floor(Math.random() * countOfList)+1;
        if(!requiredIndices.includes(aRandomNumber))
        {
            requiredIndices.push(aRandomNumber);
        }
        if(requiredIndices.length == requiredCount)
        {
            return requiredIndices;
        }
    }
}

// get random users - count in URL
app.get("/random-users/:count", (req, res)=>{
    let theCount = req.params.count;
    let theListCount = theData.length;
    let theRandomIndices = getRandomIndicesArray(theListCount, theCount);
    
    let requiredObjects = []
    for(let i=0; i<theRandomIndices.length; i++)
    {
        requiredObjects = [...requiredObjects, theData[theRandomIndices[i]]]
        //requiredObjects.push(theData[theRandomIndices[i]]);
    }
    res.json(requiredObjects)
});

// post - create a new user
app.post("/create-user", (req, res)=>{
    let theNewUser = req.body;
    theNewUser["id"] = theData.length+1;
    theData.push(theNewUser);
    res.json(theNewUser);
});

// put - update a user (getting its ID)
app.put("/user/:id", (req, res)=>{
    let id = parseInt(req.params.id);
    let theBody = req.body;
    for(let i=0; i<theData.length; i++)
    {
        if(theData[i].id === id)
        {
            let theUpdatedUser = theBody;
            theUpdatedUser["id"] = id;
            theData[i] = theUpdatedUser;
            res.json(theUpdatedUser);
        }
    }
    res.json({"message": "User does not exist"});
});

// delete - delete a user (getting its ID)
app.delete("/user/:id", (req, res)=>{
    let id = parseInt(req.params.id);
    theData.filter((ele, index)=>{
        if(ele.id === id)
        {
            theData.splice(index, 1);
            res.json({
                message: "User deleted successfully."
            });
        }
    });
    res.json({"message": "User does not exist"});
})

app.listen(3000, ()=>{
    console.log("Server Started");
});