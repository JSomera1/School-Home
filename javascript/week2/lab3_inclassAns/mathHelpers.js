const squareRoot = (n) => Math.sqrt(n);

const square = (n) => n * n; //Math.pow(n, 2) if you want to

const distance = (x1,y1,x2,y2) => {
    return squareRoot(square(x2-x1) + square(y2-y1))
}


//default export 
/* module.exports = distance (single function)*/

module.exports = { distance } //only export function you are calling //can remove curly braces if exporting one fun