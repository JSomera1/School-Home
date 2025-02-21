//Distance lab (2)
const process = require('process');
const fs = require('fs');

//destructuing
const [,,x1,y1,x2,y2] = process.argv

const processInput = (userinput) => {
    //create a filder called data points
    fs.mkdir("datapoints", (err) => {
        if (err) {
            console.log(err)
        }

        fs.writeFile("datapoints/points.txt", userinput, (err) => {
            if (err) {
                console.log(err)
            }
            //print content saved
            console.log("content satves")

            //append distance message to file
            const distance = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        })
    })
}

processInput(`${x1} ${y1} ${x2} ${y2}`)