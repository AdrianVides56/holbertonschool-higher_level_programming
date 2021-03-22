#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || Number(num) === 0) {
    return Number(1);
  }
  return factorial(Number(num - 1)) * Number(num);
}

console.log(factorial(process.argv[2]));
