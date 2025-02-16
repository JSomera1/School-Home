const userInput = require('process').argv.slice(2)
const fs = require('fs')
const math = require('./mathHelper')




function processInput(main){
    const solution = math.distance(main).toString()
    const text = `The distance between your two points: (${main[0]},${main[1]}), (${main[2]},${main[3]}) is ${solution}`
    fs.mkdir('./dataPoints', () => {
        fs.appendFile('./dataPoints/points.txt', `\n${text}`, (err) =>{ if(err){throw err}})
        console.log('content saved')
    })
    // fs.appendFile('./dataPoints/points.txt', `\n${text}`, (err) =>{ if(err){throw err}})
    
}


processInput(userInput)
