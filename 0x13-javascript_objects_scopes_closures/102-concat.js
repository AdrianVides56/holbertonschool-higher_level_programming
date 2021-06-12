#!/usr/bin/node
const fs = require('fs');
const fileA = fs.readFileSync(process.argv[2], 'utf8');
const fileB = fs.readFileSync(process.argv[3], 'utf8');
try {
  fs.writeFileSync(process.argv[4], fileA + '\n' + fileB);
} catch (err) {
  console.error(err);
}
