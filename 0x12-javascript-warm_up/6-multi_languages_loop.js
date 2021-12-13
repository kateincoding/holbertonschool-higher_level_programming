#!/usr/bin/node
//  script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
do {
  console.log(languages[i]);
  i++;
} while (i <= 2);
