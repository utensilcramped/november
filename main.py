function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Prompt the user to enter the minimum and maximum values
const min = parseInt(prompt("Enter the minimum value:"));
const max = parseInt(prompt("Enter the maximum value:"));

// Generate a random number
const randomNum = getRandomNumber(min, max);

// Display the random number
console.log(`Random number between ${min} and ${max}: ${randomNum}`);



