const fs = require("fs")
const path = require("path")
const process = require("process").argv


const dirpath = process[1];
const extension = "." + process[2];
fs.readdir(dirpath, (err, list) => {
    if (err) {
       return console.log(err);
    }

    const result = list.filter( (file) => {
        return path.extname(file) === extension;
    });
    for (let i = 0; i < result.length; i++) {
        console.log(result[i]);
    }
});