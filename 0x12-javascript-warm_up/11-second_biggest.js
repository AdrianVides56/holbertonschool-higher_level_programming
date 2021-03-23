#!/usr/bin/node
// let biggest = secBig = thirBig = 0;
let idx = 0;
let aux = 0;
const myList = [];

for (idx = 2; idx < process.argv.length; idx++) {
  myList.push(Number(process.argv[idx])); // Create a new list with args
}
if (Number(myList.length) === 0 || Number(myList.length) === 1) {
  console.log(0);
} else {
  for (idx = 0; idx < myList.length; idx++) { // Order the list of args
    if (myList[idx] > myList[idx + 1]) {
      aux = myList[idx + 1];
      myList[idx + 1] = myList[idx];
      myList[idx] = aux;
      idx = -1;
    }
  }
  console.log(myList[idx - 2]);
}
