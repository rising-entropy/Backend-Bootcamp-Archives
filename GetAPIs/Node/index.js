const express = require("express");
const app = express();

const theData = require("./data.json");

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


app.listen(3000, ()=>{
    console.log("Server Started");
});