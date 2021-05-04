#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const taskDict = {};

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(body);
    for (let i = 0; i < tasks.length; i++) {
      const user = tasks[i].userId;
      if (tasks[i].completed) {
        if (user in taskDict) {
          taskDict[user] += 1;
        } else {
          taskDict[user] = 1;
        }
      }
    }
  }
  console.log(taskDict);
});
