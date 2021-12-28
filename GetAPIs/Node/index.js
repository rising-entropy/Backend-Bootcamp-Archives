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

// get random users - count in URL
app.get("/random-users/:count", (req, res)=>{
    
});


app.listen(3000, ()=>{
    console.log("Server Started");
});