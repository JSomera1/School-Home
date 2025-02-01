//just a rough approach
const fs = require('fs')
const path = require('path')

function filterModule(dir,ext,callback){
    function filteredFiles(dir,ext){
        fs.readdir(dir, {recursive:true}, (err,files) => {
            if(err) return callback(err)
            
            callback(null,files.filter(f=> path.extname(f) === ext))
        })
    }
}

filterModule('.', '.txt', (err,filteredFiles) =>{
    if(err) return console.log(err)
    
    filteredFiles.forEach(f => console.log(f));
})
