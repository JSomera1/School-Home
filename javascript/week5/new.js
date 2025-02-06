/*
Syncronous - sometimes we cant avoid it 
console.log()
IO operations 
fs.readFileSync (which you dont really wanna use)

## node gives us Async functions as callbacks and promises 

##Promises 
1. .then syntax
2. await syntax
    - alternative way of writing .then
*/

const fs = require("node:fs/promises")


fs.writeFileSync("someFile.txt", "hello")
//Sync blocks the rest of the program from running 


// fs.writeFile("someFIle.txt", "hello")
// //anytime you see the .then, put await 
// .then(() => {
//     console.log("Done writing!")
//     fs.readFile("someFile.txt", "utf8")
// })
// .then(() => console.log(data))
// //is called if there is an error
// .catch(err=> console.log(err))

//await version
async function main(){
    //try catch blocks if any acceptions 
    try{
        await fs.writeFile("someFIle.txt", "hello")
        //following few lines are grouped with the await 
        console.log("Done writing!")
        fs.readFile("someFile.txt", "utf8")
        console.log(data)
    }
    
    catch{

    }

    //function groups lines, allowing outside to still run while inside waits for eachother
}

main()



//handling large files ex: 200gb 
/*
using something called streaming to process large files into pieces 
    - splitting into smaller parts 

fs.readfile is okay for html and css

stream is a way to get data from one location to another (when broken down)
    - only get benefits with large files

Backpressure 


Other types
    - duplex steram
        both writeable and readable
    - transform stream
        s

Example 
1. write data
2. transform the data
    - takes pieces and then compressed chunks get put into a zip file
3. read the transformed data

.pipe replaces if statements 
    - used like a .then 
    - passes data from one stream to the next stream without worrying about backpressure 

    .pipeline 
        - pushing all streams 
        - can catch errors
*/


