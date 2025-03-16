const express = require('express')
const session = require("express-session")

const app = express()

app.set("view engine", "ejs")
app.use(express.urlencoded())
//for web
// app.use(express.json())
//for phone

app.use(session({secret:'keyboard cat', cookie: {maxAge: 80000 }}))

// app.get("/", (req,res) => {
//     res.send(`
//         <form>
//             <input name="username" placeholder="username"/>
//             <button>login</button>
//         </form>
//         `)
// })



app.post("/login", (req,res) => {
    res.render("login")
    })
app.listen(8008, () => {
    console.log("server is running")
})