#!/usr/bin/node
// Declare a constant variable that stores the first argument passed
const firstArg = process.argv[2];

// Use a ternary operator to check if firstArg is undefined and print the appropriate message
firstArg === undefined ? console.log("No argument") : console.log(firstArg);
