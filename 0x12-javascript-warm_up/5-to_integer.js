#!/usr/bin/node
const myArg = process.argv[2];
if (isNaN(myArg) === false) {
  console.log('My number: ' + myArg);
} else {
  console.log('Not a Number');
}
