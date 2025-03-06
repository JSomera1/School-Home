///getting information from the website


const express = require('express')
const app = express()
const port = 3000

const messages = { success : "you exist in the database!", failure: "you do not exist in the database"}

app.get("/", (req,res) => {res.render("pages/index")})

app.get("/myForm", (req,res) => { res.render("pages/myForm")})

app.post("/myForm", (req,res) => {
    let formData = req.body
    console.log(formData)
    let username = formData.username
    if (databaseOfUsernames.includes(userName)) {
        res.render("pages/result", { result: messages.success})
    }
        res.render("pages/result". { result: messages.failure})
})

app.listen(port)