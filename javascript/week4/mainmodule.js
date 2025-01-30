//function 
const fs = require('fs') //can 
const path = require('path')


function mod(dirpath, extension, callback){
    fs.readdir(dirpath, (err,list) =>{
        if(err){
            return callback(err)
        }
        const result = list.filter((file) =>{
            return path.extname(file) === extension;
        })
        callback(null, result)

    })
    
}

module.exports = {mod}

