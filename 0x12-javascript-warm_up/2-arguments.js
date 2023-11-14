#!/usr/bin/node
// Declare a constant variable that stores the number of arguments passed
const numArgs = process.argv.length - 2;

// Use a switch statement to check the value of numArgs and print the appropriate message
switch (numArgs) {
  case 0:
    console.log("No argument");
    break;
  case 1:
    console.log("Argument found");
    break;
  default:
    console.log("Arguments found");
}

