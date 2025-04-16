const fs = require("node:fs/promises");
const { EOL } = require("node:os");

const readMenu = (file) => fs.readFile(file, "utf8");
const groupMenu = (csv) => {
  const groupings = {};
  csv.split(EOL).forEach((row) => {
    const [type, name, qty, price] = row.split(","); // { type: lunch, name: bento a }
    if (!(type in groupings)) {
      groupings[type] = [{ name, price, qty }];
    } else {
      groupings[type].push({ name, qty, price });
    }
  });
  return groupings;
};
const makePrettyMenu = (groupings) => {
  let prettyStr = "";
  for (const key in groupings) {
    const mealItems = groupings[key];
    prettyStr += `${key} items`;
    prettyStr += EOL;
    mealItems.forEach((meal) => {
      prettyStr += `${meal.price} ${meal.name} ${meal.qty}`;
      prettyStr += EOL;
    });
    prettyStr += EOL;
  }
  return prettyStr;
};
const writeMenu = (prettyMenu) => fs.writeFile("menu.txt", prettyMenu);
async function main() {
  try {
    const csv = await readMenu("menu.csv");
    const groupings = groupMenu(csv);
    const prettyMenu = makePrettyMenu(groupings);
    await writeMenu(prettyMenu);
    console.log("Program finished");
  } catch (error) {
    console.log(error);
  }
}
main();
