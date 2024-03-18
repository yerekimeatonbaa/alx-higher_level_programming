#!/usr/bin/node
const list = require('./100-data');

// Compute new array using map
const newList = list.map((value, index) => value * index);

// Print initial list
console.log("Initial List:", list);

// Print new list
console.log("New List:", newList);
