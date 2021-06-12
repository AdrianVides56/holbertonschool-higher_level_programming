#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

for (const [key, value] of Object.entries(dict)) {
  /* console.log(key, value); */
  if (!newDict[value]) {
    newDict[value] = [key];
  } else {
    newDict[value].push(key);
  }
}

console.log(newDict);
