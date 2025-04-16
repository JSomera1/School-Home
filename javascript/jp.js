const fs = require("fs")

await function readFile(filename){
	return new Promise (() => 
	fs.readFile(filename,"utf8", (err,data) =>{
		if(err){
			console.log(err)
			}
		else{
			console.log(data)
		}
	}
	
	))
}

try{

const data = await readFile("players.csv")
}
catch{
	console.log(err)
}