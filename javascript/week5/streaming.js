const process = require("process");
const {Transform} = require("stream")
const rs = process.stdin
//gives back a transform stream
const ts = new Transform({
    transform: (chunk,encoding,callback) => {
        const upperCaseVer = chunk.toString().toUpperCase()

        callback(null,upperCaseVer)
    }
}
    
)
const ws = process.stdout

// rs.on("data", (chunk) => ws.writefile(chunk))
// sending chunks of data
rs.pipe(ts).pipe(ws)
