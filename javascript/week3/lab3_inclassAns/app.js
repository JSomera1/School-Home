const mathhelpers = require('./mathHelpers')
const process = require('process')
const fs = require('fs')
const { EOL } = require('os')//os.EOL

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
    //pathfinding 
    const dirName = "dataPoints"
    const dirPath = path.join(__dirname, dirName, "points.txt")
    if(err) return console.log(err);
    console.log("Directory already exists")
    //error codes
    if(err.code === "EEXIST") return 'something'
    //nest functions if there is a dependency 
    fs.writeFile(dirPath, userInput, (err) => {
        if (err) return console.log(err)
        console.log('Content Saved')
        //pathfinding 
        // path.join(__dirname, "dataPoints", "points.txt")
        // console.log(__dirname + /) ::: from root to current directory (full path)
        const distanceMsg = `${EOL}distance message...`
        

        fs.appendFile(dirPath, distanceMsg, (err) => {
            if (err) return console.log
        })
    });

    

})

//create a file called dataPoints/points.txt

//write userInput into points.txt

//APPEND the distance message to points.txt 