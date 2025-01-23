function rect(length,width,callback) {
// check length/width is <= 0 -> send an error into callback
    if(length <= 0 || width <= 0){
        return callback(new Error("invalid dimensions"))
    }
    callback(null, {perimeter: 2 * (length + width), area: length * width })

// send the perimeter and area into the callback 
}

module.exports = {rect}