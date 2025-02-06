
const fs = require("node:fs/promises")

const readMenu = (csvFile) => {
    return fs.readFile(csvFile, "utf-8")
}
const groupMenuItems = (menuData) => {

    const groupedItems = {}
    menuData.split(EOL).forEach((row) => {
        const [type,name,quantity,price] = row.split(",")
        if (!(type in groupedItems)){
            groupedItems[type] = [{name,quantity,price}]
        } else {
            groupedItems[type].push({name,quantity,price})
        }
    })
    return groupedItems
}
const makePrettyMenu = (groupedData) => {
    let menuStr = ''
    for(const key in groupedData) {
        menuStr += `${key} items`
        menuStr += EOL 
        groupedData.forEach(row => {
            const {name, quantity, price} = row 
            menuStr += `${price} ${name} ${quantity}`
            menuStr += EOL
        })
    }
    return menuStr
}
const writeMenu = (prettyMenuStr) => {
    return fs.writeFile("menu.txt", prettyMenuStr)
}

// only make promises when absolutely necessary 

//make this sort of like a blueprint 
readMenu("menu.csv")
.then(data => {
    const  grouedData = groupMenuItems(data)
    const prettyMenuStr = makePrettyMenu(groupedData)
    return WriteMenu(prettyMenuStr)
})
.then(() => console.log("Program is finished"))
.catch(err => console.log(err))