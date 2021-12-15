#!/usr/bin/node
// script that imports an array and computes a new array
const { list } = require('./100-data');

const newList = [];
for (let i = 0; i < list.length; i++) {
  newList.push(i * list[i]);
}
console.log(list);
console.log(newList);
