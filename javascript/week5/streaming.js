// const process = require("process");
// const {Transform} = require("stream")
// const rs = process.stdin
// //gives back a transform stream
// const ts = new Transform({
//     transform:(chunk,encoding,callback) => {
//         const upperCaseVer = chunk.toString().toUpperCase()

//         callback(null,upperCaseVer)
//     }
// }
    
// )
// const ws = process.stdout

// // rs.on("data", (chunk) => ws.writefile(chunk))
// // sending chunks of data
// rs.pipe(ts).pipe(ws)

// const input = process.stdin

// const output = process.stdout

// input
// .pipe()
// .pipe(output)

const { createReadStream } = require('fs');
const csv = require("csvtojson");
const z = require('zlib')
const {Transform} = require("stream")

// -----Your filterByCountry function here:-----
function filterByCountry(country) {
    const ts = new Transform({
        transform:(chunk,encoding,callback) => {
            const back = JSON.parse(chunk)

            callback(null, back)
        }
    })

    console.log(ts)

} 

//----------------------------------------------

// --------Your sumProfit function here:--------

const sumProfit = () => {
    const sum = new Transform({
        transform:(chunk,encoding,callback) => {
            const total = JSON.parse(chunk)
        }
    })
}
//----------------------------------------------



createReadStream('data.csv.gz') 
  .pipe(z.createGunzip())
  .pipe(csv())
  .pipe(filterByCountry('italy'))                       

//   .pipe(sumProfit())                     
//   .pipe(process.stdout)  