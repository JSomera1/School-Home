const fs = require("node:fs");

function readFileP(filename) {
    const promObj = new Promise((resolve, reject) => {
        fs.readFile(filename, (err, data) => {
            if (err) {
                reject(err); // Pending -> Rejected and Update the Promise Result
            }
            else {
                resolve(data.toString()); // Pending -> Fulfilled
            }
        });
    });
    
    return promObj;
};

function turnIntoNiceMenu(data) {
    const lines = data.split("\n")
    const categories = {};

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        const [mealType, mealName, mealQuantity, price] = line.split(",");
        const correctFormat = `$${parseFloat(price.slice(1)).toFixed(2)} ${mealName.trim()} ${mealQuantity.trim()}`

        if (!categories[mealType.trim()]){
            categories[mealType.trim()] = [];
        }
        categories[mealType.trim()].push(correctFormat)
    }

    completedOutput = "";

    for (const category in categories) {
        completedOutput = completedOutput + `* ${category.charAt(0).toUpperCase() + category.slice(1)} Items *\n`
        completedOutput = completedOutput + categories[category].join("\n") + "\n\n";
        console.log(categories)
    }
    return completedOutput
}

function writeFileP(filename, data) {
    const promObj = new Promise((resolve, reject) => {
        fs.writeFile(filename, data, (err) => {
            if (err){
                reject(err);
            }
            else {
                resolve();
            }
        })
    })
    return promObj;
}

readFileP("menu.csv")
    .then((csvContents) => turnIntoNiceMenu(csvContents))
    .then((niceMenuStr) => writeFileP("nicemenu.txt", niceMenuStr))
    .then(() => console.log("Program Complete"))
    .catch((err) => console.log(err));