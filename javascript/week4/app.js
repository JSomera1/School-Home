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
.then((data) => {
    const reads = data.split("\n")
    const categories = {}
    
    for (let i = 0; i< reads.length;i++){
        const line = reads[i]
        const[MealType,MealName,MealQuantity,Price] = line.split(",")
        const correctFormat = `$${parseFloat(Price.slice(1)*1.8).toFixed(2)}  ${MealName.trim()}, ${MealQuantity.trim()}`

        if(!categories[MealType.trim()]){
            categories[MealType.trim()] = []
        }
        categories[MealType.trim()].push(correctFormat)
    }

    completedOutput = ''

    for (const category in categories) {
        completedOutput = completedOutput + `* ${category.charAt(0).toUpperCase() + category.slice(1)} Items *\n`
        completedOutput = completedOutput + categories[category].join("\n") + "\n\n";
    }
    
    return completedOutput
})
.then((menu) => writeFileP('menu.txt', menu))
.then(console.log("Program complete"))
.catch((err) => console.log(err))