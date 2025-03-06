//why do we want express? contant third party and other related stuff from a server

const express = require('express')
const app = express()
const port = 3000

function callMe(req, res) {
    //res -> allows to send reponses to browser
    res.send(myHTML) //-> sending string of text back to the browser
    //.sendFile("thisfile.txt")
    
}
app.get("/", callMe)
//routing -> telling express what to send to the browser

app.listen(port)


//end of part 1 

let  myHTML = ``

let names = ["john", "jian", "joseph", "jorge"]

names.forEach(name => myHTML += `<h1>${name}</h1>`)

/* req.query version */
// const express = require('express')
// const app = express()

app.get("/hello", (req, res) =>{
    let firstName= req.query.firstName;
    let lastName = req.query.lastName
    res.send(`<p> Hi ${firstName} ${lastname}</p>`)
})

app.listen(port)


/* req.params ver */
// const express = require('express')
// const app = express()

// order matters in this one
// app.get('/hello/:firstName/:lastName', (req,res) => {
//     let firstName = req.params.firstName
//     let lastName = req.params.lastName
//     res.send(`<p> Hi ${firstName} ${lastName }</p>`)
// })

// app.listen(port)


//accessing into folder 
//accessing into files
app.use(express.static("public"))

app.set("view engine", "ejs")
// ejs allows us to put dynamic content in html

app.get("/", (req,res) => {
    let date = new Date()
    res.render("pages/index"), {
        dateVariable: date
    }
})
/**
 changes:
    when user goes to index, return page in pages directory
    if user goes to /about -> return about page
 */

app.get("/about", (req,res) => {
    res.render("pages/about")
})
app.listen(3000)