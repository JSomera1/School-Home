const proc = require('process').argv.slice(2)
const mod = require('./mainmodule')

const dirpath = proc[0]
const extension = "."+proc[1]



const name = (dirpath, extension) =>{
    mod.mod(dirpath, extension, (err, result) => {
        if(err){
            return console.log(err)
        }
        for(let i=0;i<result.length;i++){
            console.log(result[i])
        }
    }) 
}

name(dirpath,extension)