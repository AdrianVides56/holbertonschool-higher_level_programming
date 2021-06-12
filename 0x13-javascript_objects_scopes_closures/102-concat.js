#!/usr/bin/node
const fs = require('fs');
function read (num) {
  fs.readFile(process.argv[num], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      fs.appendFile(process.argv[4], data + '\n', err => {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}

read(2);
read(3);
