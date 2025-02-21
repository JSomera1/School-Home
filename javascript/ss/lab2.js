const [x1,y1,x2,y2] = require('process').argv.slice(2);
const fs = require('fs');
const { distance } = require('./mathHelpers')
const result = distance(Number(x1),Number(y1),Number(x2),Number(y2))
const message = `The distance between (${x1},${y1}) and (${x2},${y2}) is ${result}`

fs.writeFile('./points.txt', message, (err) => {
    if (err) {
        console.log(err)
    }
    console.log('content saved')
})
