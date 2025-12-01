const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const list1 = [];
const list2 = [];

console.log("Enter the numbers (press Enter on empty line to finish):");

rl.on("line", (line) => {
    if (line.trim() === "") {
    rl.close(); 
    return;
    }

  const [a, b] = line.trim().split(/\s+/).map(Number);
  if (!isNaN(a) && !isNaN(b)) {
    list1.push(a);
    list2.push(b);
  } else {
    console.log("Enter two numbers separated by a space");
}
});

rl.on("close", () => {
  list1.sort((a, b) => a - b);
  list2.sort((a, b) => a - b);

  const pairList = list1.map((item, index) => [item, list2[index]]);
  const pairDistance = pairList.map((pair) => Math.abs(pair[1] - pair[0]));
  const sumPairDistance = pairDistance.reduce((a, b) => a + b, 0);

  console.log("sumPairDistance:", sumPairDistance);
});
