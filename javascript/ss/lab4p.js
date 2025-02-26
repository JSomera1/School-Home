const fs = require('fs/promises')

const read = (file) => {
    return fs.readFile(file, 'utf-8')
}
const group = (data) => {
    const group = {}
    
    data.split("\n").forEach((row) => {
        const [tp, fd, am, pr] = row.split(",")
        if(!(tp in group)){
            group[tp] = [{fd,am,pr}]
        }
        else{
            group[tp].push({fd,am,pr})
        }
    })
    
    let output = ''

    for(const key in group){
        output += `${key} item \n`
        group[key].forEach((data) => {
            const {fd,am,pr} = data
            //using curly braces when decompositioning dictionary
            output += `$${parseFloat(pr.slice(1)*1.8).toFixed(2)} ${fd}, ${am}`
            output += `\n`
        })
    }
    return output
}

const write = (file) => {
    return fs.writeFile('menu.txt', file)
}

read(`menu.csv`)
.then(data => {
    const gr = group(data) 
    return gr
})
.then(data => write(data))
.catch(err => console.log(err))