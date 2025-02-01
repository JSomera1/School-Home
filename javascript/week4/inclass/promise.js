//Object -> Dictionary 
// values can change overtime

//object literal 
// const obj = {};

// //literals is creating value on the spot 
// const str = "";

//promise object
// const obj = new Promise((resolve,reject)=>{
//     resolve("we read the file!") //pending -> fulfuled 
// })

//Promise{}
//result contains file content 
//3 states, pending, fulfilled or rejected 

const fs = require('fs')




//modeling as a promise 

function readFileP(){
    const promObj = new Promise((resolve,reject) => {
        fs.readFile(filename,(err,data) =>{
            if (err) {
                reject(err)
            }
            else{
                resolve(data.toString())
            }
        })
    })
    return promObj
}

const promise = readFileP("file2.txt")

promise.then((result)=> console.log(result))

promise.catch((err) => console.log(err))

// setTimeout(()=>{
//     console.log(promise)
// },5000)
// //prototype -> obejct that you inherit from 
// console.log(promise["[[PromiseResult]]"])

/**
 stage 1 
 Inside of object{
 pending 
 Undefined 
 }

 Logic
 1. code starts to run by calling fs.readfile 
 2. sends back resolve if no reject 
 3. changes pending to fulfilled 

 has a watcher that constantly watches object 
 - when change happens is when we jump to .then
 */

module.exports = {readFileP}