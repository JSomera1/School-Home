const square = (x) => x * x;

const squareroot = (x) => Math.sqrt(x);

const distance = (x1,y1,x2,y2) => {
    return squareroot(square(x2 - x1) + square(y2 - y1))
}

module.exports = {
    distance
}