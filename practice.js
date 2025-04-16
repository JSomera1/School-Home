const fs = require("fs")

function Readfile(filename){
    return new Promise((resolve,reject) => [
        fs.readFile(filename, "utf-8", (err,data) => {
            if(err){
                reject(err)
            } else {
                resolve(data)
            }
        })
    ] )
}

const file = await Readfile("products.csv")
console.log(file)