const mathhelpers = require('./mathHelpers')
const process = require('process')
const fs = require('fs')

//position matters for array destructure. Empty commas are used for skipping positions
//process.argv(slice) as alternative 
const [,,x1,y1,x2,y2] = process.argv
//objects for some reason
const person = {
    firstName:"james",
    lastName:"Doe"
}


// //destructuring in order to call variable instead of object.item
// const {firstName, lastName} = person;
// //names have to match 

// A function called processInput receives userInput
const processInput = (userInput) => {

}

processInput(`${x1},${y1},${x2},${y2}`)

//creat a folder called data points 
fs.mkdir("dataPoints", (err) => {
    if(err) return console.log(err);
    console.log("Directory already exists")
    //error codes
    if(err.code === "EEXIST") return 'something'
    //nest functions if there is a dependency 
    fs.writeFile("dataPoints/points.txt", userInput, (err) => {
        if (err) return console.log(err)
        console.log('Content Saved')

        const distanceMsg = `distance message...`

        fs.appendFile("dataPoints/points.txt", distanceMsg, (err) => {
            if (err) return console.log(err)
        })
    });

    

})

//create a file called dataPoints/points.txt

//write userInput into points.txt

//APPEND the distance message to points.txt 