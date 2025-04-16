const fs = require("fs")

fs.readFile("j.csv",'utf-8',(err,data) => {
    if(err){
        console.log(err)
    } else {
        const lines = data.split("\n")
        for (let i = 0; i< lines.length; i++) {
            const line = lines[i]
            const[name,price,available,category] = line.split(",")
            let string = name + "\n"
            fs.appendFile("out.txt", string, (err) => {
                if (err){
                    console.log(err)
                }
            })
            
        }
    }
})

fs.readFile('j.json', 'utf-8', (err,data)=>{
    if(err){
        console.log(err)
    } else {
        // for json files, they need to be parsed to be able to be read
        json = JSON.parse(data)
        console.log(json["result"][0]["message"]

        )
    }
})

