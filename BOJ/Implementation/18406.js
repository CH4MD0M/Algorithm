const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

let count = 0;
for (let i = 0; i < input.length; i++) {
  if (i < input.length / 2) {
    count += input[i] * 1;
  } else {
    count -= input[i] * 1;
  }
}

console.log(!count ? 'LUCKY' : 'READY');
