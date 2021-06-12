#!/usr/bin/node
const fs = require('fs');
let a = 0;
function read (num) {
  fs.readFile(process.argv[num], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      if (a === 0) {
        fs.appendFile(process.argv[4], data + '\n', err => {
          if (err) {
            console.error(err);
          }
        });
        a = 1;
      } else {
        fs.appendFile(process.argv[4], data, err => {
          if (err) {
            console.error(err);
          }
        });
      }
    }
  });
}

read(2);
read(3);
