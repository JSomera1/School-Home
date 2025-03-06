const fs = require('fs/promises')
const { EOL } = require('os')

const read = () => fs.readFile('supply.txt', 'utf8')
const viewAllSupply = (brew) => {
    const count = {}
    read()
    .then((data) => {
        data.split(EOL).forEach((row) =>{
            if(!(row in count)){
                count[row] = 1 
            }
            else{
                count[row] += 1
            }
        })
        if(brew.toLowerCase() == "b" || brew.toLowerCase() == "blonde"){
            console.log(count['blonde'])
        }
        else if (brew.toLowerCase() == "mr" || brew.toLowerCase() == "medium-roast" || brew.toLowerCase() == "medium roast"){
            console.log(count['medium-roast'])
        }
        else if (brew.toLowerCase() == "dr" || brew.toLowerCase() == "dark-roast" || brew.toLowerCase() == "dark roast"){
            console.log(count['dark-roast'])
        }
        else{
            console.log('that is not an available brew')
        }
    })
    return count 
}

const addSupply = (type) => {
    if(type.toLowerCase() == "b" || type.toLowerCase() == "blonde"){
        fs.appendFile('supply.txt', `blonde${EOL}`, (err) =>{
            if(err) {
                console.log(err)
            }
        })
    }
    else if (type.toLowerCase() == "mr" || type.toLowerCase() == "medium-roast" || type.toLowerCase() == "medium roast"){
        fs.appendFile('supply.txt', `medium-roast${EOL}`, (err) =>{
            if(err) {
                console.log(err)
            }
        })
    }
    else if (type.toLowerCase() == "dr" || type.toLowerCase() == "dark-roast" || type.toLowerCase() == "dark roast"){
        fs.appendFile('supply.txt', `dark-roast${EOL}`, (err) =>{
            if(err) {
                console.log(err)
            }
        })
    }
    else{
        console.log('that is not an available brew')
    }
    return 
}

const deleteSupply  = (brew, amount) => {
    const count = {}
    read()
    .then((data) => {
        data.split(EOL).forEach((row) =>{
            if(!(row in count)){
                count[row] = 1 
            }
            else{
                count[row] += 1
            }
        })
        if(brew.toLowerCase() == "b" || brew.toLowerCase() == "blonde"){
            if(amount == "*"){
                count[brew] -= count[brew]
            }
            else{
                if(amount >= count[brew]){
                    count[brew] -= count[brew]
                }
                else{
                    count[brew] -= amount 
                }
            }
        }
        else if (brew.toLowerCase() == "mr" || brew.toLowerCase() == "medium-roast" || brew.toLowerCase() == "medium roast"){
            if(amount == "*"){
                count[brew] -= count[brew]
            }
            else{
                if(amount >= count[brew]){
                    count[brew] -= count[brew]
                }
                else{
                    count[brew] -= amount 
                }
            }
        }
        else if (brew.toLowerCase() == "dr" || brew.toLowerCase() == "dark-roast" || brew.toLowerCase() == "dark roast"){
            if(amount == "*"){
                count[brew] -= count[brew]
            }
            else{
                if(amount >= count[brew]){
                    count[brew] -= count[brew]
                }
                else{
                    count[brew] -= amount 
                }
            }
        }
        else{
            if(amount == "*"){
                count[brew] -= count[brew]
            }
            else{
                if(amount >= count[brew]){
                    count[brew] -= count[brew]
                }
                else{
                    count[brew] -= amount 
                }
            }
        }
    })
    let recount = ""
    
    for (let key in count){
        count[key].forEach((row) => {
            recount += key + EOL
        })
    }
    fs.writeFile('supply.txt', recount)
    return recount
}


viewAllSupply("DR")
.then(() => deleteSupply("DR", 2))
.then(viewAllSupply("DR"))

