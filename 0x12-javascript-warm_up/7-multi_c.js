#!/usr/bin/node
// const printTimes = process.argv[2];
let idx = 0;
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (idx = 0; idx < process.argv[2]; idx++) {
    console.log('C is fun');
  }
}
