function solution(number, limit, power) {
  const weapons = [];
  for (let i = 1; i <= number; i++) {
    let count = 1;
    for (let j = 1; j <= i / 2; j++) {
      if (i % j === 0) count++;
    }
    weapons.push(count);
  }

  const answer = weapons.map(value => (limit < value ? power : value));
  return answer.reduce((acc, cur) => acc + cur, 0);
}

// 효율성 고려해서 약수 구하기
function solution(number, limit, power) {
  const weapons = [];
  for (let k = 1; k <= number; k++) {
    let count = 0;
    for (let i = 1; i * i <= k; i++) {
      if (k % i === 0) {
        count++;
        if (k / i != i) {
          count++;
        }
      }
    }
    weapons.push(count);
  }
  const answer = weapons.map(value => (limit < value ? power : value));
  return answer.reduce((acc, cur) => acc + cur, 0);
}
