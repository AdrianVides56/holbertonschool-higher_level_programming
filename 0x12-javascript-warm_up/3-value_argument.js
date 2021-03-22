#!/usr/bin/node
const fisrtArg = process.argv[2];
if (fisrtArg !== undefined) {
  console.log(fisrtArg);
} else {
  console.log('No argument');
}
