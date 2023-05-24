#!/usr/bin/node
//This is a script that computes the number of tasks completed by user id.

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(`Error: ${error.message}`);
  } else {
    const tasks = JSON.parse(body);

    const completeTasks = {};

    tasks.forEach((task) => {
      if (task.complete) {
        if (completeTasks.hasOwnProperty(task.userId)) {
          completeTasks[task.userId]++;
        } else {
          completeTasks[task.userId] = 1;
        }
      }
    });

    console.log(completeTasks);
  }
});

