/**
file USI has a major limitation: can only find file in your home network 
http is the smarter version but does not hold limitation -> can find any file on the internet
computers become servers -> stops people from accessing your files

what we are doing:
infinite node loop waiting for website to get a request and sends back response
    - called web server
 */

const fs = require('fs/promises');
const http = require('http'); 
const net = require('net'); // <- TCP/IP
const express = require('express');

const app = express(); //using this to create a server with express
// this is the previous code for a server wihtout using express
// http.createServer(async (req,res) => {
//     const data = await fs.readFile("wk7.html", "utf8")    
//     res.end(data)

//     // receiving data from web browser
// })
app.set("view engine", "ejs")

app.use(express.urlencoded( {extrended: false} ))


app.get("/", (req,res) => {
    res.send("<a href='/login'>contact</a>")
})


app.post("/login", (req,res) => {
    const { username, password } = req.body;
    // log in the user... (after midterm)
    res.redirect("/dashboard")
    // whenever you call -> sends response to browser. response has a special code 
    // whenever a browser sees 302 -> make another request to server 
})

app.get("/dashboard",async (req,res) => {
    const username = "john123" 
    res.render("dashboard", { username })
    
})
app.get("/login", (req,res) => {
    res.send(`
        <form action="/login" method="post">
            <input name="username" placeholder="username">
            <input name="password" placeholder="password">
            <button>submit</button>
        </form>`)
})

// http://ip
//provide a port number
app.listen(5500, () => {
    console.log("server is running")
})
