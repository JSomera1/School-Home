const fs = require('node:fs')
const { EOL } = require('os')

//create three functions or MORE


function viewAllSupply (stock) { 
    let count = {}
    fs.readFile('supply.txt', "utf8", (err, data) =>{
        if(err){
            console.log(err)
        }
        else{
            const lines = data.split(EOL)
            lines.forEach((row) => {
                if(!(row in count)){
                    count[row] = 1 
                }
                else{
                    count[row] += 1
                }
            })
            if(stock.toLowerCase() == "b" || stock.toLowerCase() == "blonde"){
                console.log(count['blonde'])
            }
            else if (stock.toLowerCase() == "mr" || stock.toLowerCase() == "medium-roast" || stock.toLowerCase() == "medium roast"){
                console.log(count['medium-roast'])
            }
            else if (stock.toLowerCase() == "dr" || stock.toLowerCase() == "dark-roast" || stock.toLowerCase() == "dark roast"){
                console.log(count['dark-roast'])
            }
            else{
                console.log('that is not an available brew')
            }
        }
    })
    return count
    
}
function addSupply (type) {
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

function deleteSupply (brew, amount) {
    let count = {}
    fs.readFile('supply.txt', "utf8", (err, data) =>{
        if(err){
            console.log(err)
        }
        else{
            const lines = data.split(EOL)
            lines.forEach((row) => {
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
        let recount = ""
        for (let key in count){
            for ( i in count[key]){
                recount += key
            }
        }
        fs.writeFile('supply.txt', recount, (err) => {
            if(err){
                console.log(err)
            }
        })
        return recount
    }
    
})


    

}

viewAllSupply('DARK-ROAST')
addSupply("DR")
deleteSupply("DR", 2)


