const { createReadStream } = require('fs');
const csv = require("csvtojson");
const { createGunzip } = require('zlib')
const {Transform} = require("stream");
const { callbackify } = require('util');

// -----Your filterByCountry function here:-----
function filterByCountry(country) {
  const filter = new Transform({
    transform(chunk, en, callback){
      const obj = JSON.parse(chunk.toString())

      if (obj.country === country){
        this.push(chunk.toString())
      }
      callback()
    }
  })
  return filter


} 

//----------------------------------------------

// --------Your sumProfit function here:--------

function sumProfit() {
  let total = 0
  const sum = new Transform({
    transform(chunk, en, callback){
      const nums = parseFloat(JSON.parse(chunk.toString()).profit.trim())

      //add all the results together somehow 
      total += nums
      callback()
      

    },
    
    flush(callback) {
      console.log(`profit from Italy: ${total.toLocaleString(undefined, {
        minimumFractionDigits: 2, 
        maximumFractionDigits: 2})}`);
      callback();
    }
  })
  


  return sum
}
//----------------------------------------------

createReadStream('data.csv.gz')
  .pipe(createGunzip())
  .pipe(csv())                       
  .pipe(filterByCountry('Italy'))        
  .pipe(sumProfit())                     
  .pipe(process.stdout)  
