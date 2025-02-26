const fs = require('fs')
//this is the way without using promises
fs.readFile('menu.csv', (error,data) => {
    if (error){
        console.log(error)
    }
    const lines = data.toString().split("\n")
    const categories = {}
    for (let i = 0; i<lines.length; i++){
        const [meal, food, amount, Price] = lines[i].split(',')
        const correctFormat = `$${parseFloat(Price.slice(1)*1.8).toFixed(2)}  ${food}, ${amount} `

        if(!(categories[meal.trim()])){
            categories[meal] = []
        }
        categories[meal].push(correctFormat)
    }
    
    let output = ''

    for (cat in categories){
        output = output + `* ${cat.charAt(0).toUpperCase() + cat.slice(1)} *\n`
        output = output + categories[cat].join("\n") + `\n\n`
    }

    console.log(output)
})

// fs.readFile('menu.json', (error,data) => {
//     if (error) {
//         console.log(error)
//     }
//     console.log(data.toString())
// })

