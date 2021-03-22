#!/usr/bin/node
let idx = 0;
let row = '';
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (idx = 0; idx < process.argv[2]; idx++) {
    row += 'X';
  }

  for (idx = 0; idx < process.argv[2]; idx++) {
    console.log(row);
  }
}
