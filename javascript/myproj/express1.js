//why do we want express? contant third party and other related stuff from a server

const express = require('express')
const app = express()
const port = 3000

function callMe(req, res) {
    //res -> allows to send reponses to browser
    res.send() //-> sending string of text back to the browser
    //.sendFile("thisfile.txt")
    
}
app.get("/", callMe)
//routing -> telling express what to send to the browser

app.listen(port)