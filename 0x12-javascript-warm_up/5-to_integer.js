#!/usr/bin/node
const myArg = process.argv[2];
if (!isNaN(myArg)) {
  console.log(myArg);
} else {
  console.log('Not a Number');
}
