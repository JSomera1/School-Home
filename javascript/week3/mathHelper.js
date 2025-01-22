module.exports = { distance, square, squareRoot}


function squareRoot(num1,num2){
    num = num1+num2
    return Math.sqrt(num)
}

function square(num1,num2){
    squared = (num2 - num1)**2
    return squared
}

function distance(num){
    num1 = square(num[0],num[2])
    num2 = square(num[3],num[1])
    return squareRoot(num1,num2)
}

