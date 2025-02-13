const { createReadStream } = require('fs');
const csv = require("csvtojson");
const { createGunzip } = require('zlib')
const {Transform} = require("stream")

// -----Your filterByCountry function here:-----
function filterByCountry(country) {
  const filter = new Transform({
    transform:(chunk, en, callback) => {
      const ls = []
      const str = chunk.toString()
      const obj = JSON.parse(str)

      if (obj.country === country){
        ls.push(obj)
      }
      
      console.log(ls)
      callback(null, this.obj)
    }
  })

  return filter


} 

//----------------------------------------------

// --------Your sumProfit function here:--------

const sumProfit = () => {
  const sum = new Transform({
    transform:(chunk, en, callback) => {
      const nums = JSON.parse(chunk.toString())
      parseFloat(nums.profit.trim())
      total += profit
    }
  })
}
//----------------------------------------------

createReadStream('data.csv.gz')
  .pipe(createGunzip())
  .pipe(csv())                       
  .pipe(filterByCountry('Italy'))        
  .pipe(process.stdout)                     
  // .pipe(process.stdout)  
