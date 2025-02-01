const fs = require('fs')
// /promises at the end turns functions inside to promise function
const {readFileP} = require('./promise')
// //files read content and get transferred into another file 
// fs.readFile("file1.txt",(err, fileTwo) =>{
//     if (err) console.log(err)
//     //Two fundemental problems with async callback
//     // -> readability Issue (Nested Callbacks)
//     // -> No centralized Error handling 
//     // fs.readFile(filetwo, (err, filethree) => {
//     //     if (err) console.log(err)
//     //     fs.readFile(filethree,(err, filefour) => {
//     //         if (err) console.log(err)
//     //         fs.readFile(filefour, "utf8", (err,result) =>{
//     //             if (err) console.log(err)
//     //             console.log(result)
//     //         })
//     //     })
//     // })
// })


readFileP("file1.txt")
.then((fileTwo) => readFileP(fileThree))
.then((fileThree) => readFileP(fileFour))
.then((fileFour) => readFileP(result))
.then(result => console.log(result))
.catch(console.log(err))

//catch can run at any .then line 
//automatically wraps result into a promise
//promisify(fs.readfile) does .then for you
// promisify all functions 