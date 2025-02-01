/*
Create a functoin called solveRect/

-->takes 2 parameters:length and width
-> it should call a seperate function you've defined
    in another file called rect.

    rect is a function that contains 3 params: length, width, callback
    ->If length/width is <=0, provide an error to the callback


*/

const { callbackify } = require('util');
const {rect} = require('./rectModule')
function solveRect(l,w){
    rect(l,w, (err,result) => {
        //check for errors 
        if(err){
            return console.log(err);
            
        }
        console.log(`the dimensions are: ${result.perimeter}, ${result.area}`)
        //print result.area, result.perimeter
    })
}
solveRect(1,4); // -> print area, perimeter