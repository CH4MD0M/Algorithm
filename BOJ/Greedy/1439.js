const fs = require('fs');
const data = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('')
  .map(v => +v);

let answer = 0;

for (let i = 0; i < data.length - 1; i++) {
  if (data[i] !== data[i + 1]) answer++;
}

console.log(Math.floor((answer + 1) / 2));
