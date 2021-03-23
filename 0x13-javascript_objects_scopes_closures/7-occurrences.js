#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let idx; let count = 0;
  for (idx = 0; idx < list.length; idx++) {
    if (list[idx] === searchElement) {
      count++;
    }
  }
  return count;
};
