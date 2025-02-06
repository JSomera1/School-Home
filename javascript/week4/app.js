const fs = require('fs');

function readFileN(filename){
    return new Promise((resolve,reject) => {
        fs.readFile(filename, 'utf-8',(err,data) =>{
            if(err){
                reject(err)
            } else {
                resolve(data.toString())
            }
        })
    })
}

function nicemenu(data){
    const reads = data.split("\n")
    const categories = {}
    const completedOutput = ''
    for (let i = 0; i< reads.length;i++){
        const line = reads[i]
        const[MealType,MealName,MealQuantity,Price] = line.split(",")
        const correctFormat = `$${parseFloat(Price.slice(1)).toFixed(2)}  ${MealName.trim()}, ${MealQuantity.trim()}`

    
        if(!categories[MealType.trim()]){
            categories[MealType.trim()] = []
        }
        categories[MealType.trim()].push(correctFormat)
    }

    for (let j = 0;j<categories.length;j++) {
        // completedOutput = completedOutput + `* ${categories[j].charAt(0).toUpperCase() + categories[j].slice(1)} Items *\n`
        // completedOutput = completedOutput + categories[j].join("\n") + "\n\n";
        console.log(categories[j])
    }

    return completedOutput
}

function writeFileP(filename, data) {
    return new Promise((resolve, reject) => {
        fs.writeFile(filename, data, (err) => {
            if (err){
                reject(err);
            }
            else {
                resolve(data);
            }
        })
    })
}


readFileN('menu.csv')
.then((data) => nicemenu(data))
.then((menu) => writeFileP('menu.txt', menu))
.then(console.log("Program complete"))
.catch((err) => console.log(err))