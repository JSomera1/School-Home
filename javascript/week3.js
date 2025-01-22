const process = require('process').argv.slice(2)
console.log(process)

function processInput(num){
    console.log(distance(num))
}

function squareRoot(num1,num2){
    num = num1+num2
    return Math.sqrt(num)
}

function square(num){
    num1 = (num[2] - num[0])**2
    num2 = (num[3] - num[1])**2
    return squareRoot(num1,num2)
}

function distance(num){
    return square(num)
}

processInput(process)