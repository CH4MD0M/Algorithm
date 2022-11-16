// while문 사용
function solution(babbling) {
  let answer = 0;
  const double = ['ayaaya', 'yeye', 'woowoo', 'mama'];

  while (babbling.length) {
    let b = babbling.shift();
    if (double.some(v => b.includes(v))) continue;
    b = b.replace(/aya|ye|woo|ma/g, '');
    if (!b.length) answer++;
  }
  return answer;
}

// for문 사용
function solution(babbling) {
  let answer = 0;
  const double = ['ayaaya', 'yeye', 'woowoo', 'mama'];

  babbling.forEach(b => {
    for (let i = 0; i < 4; i++) {
      if (b.includes(double[i])) return;
    }
    b = b.replace(/aya|ye|woo|ma/g, '');
    if (!b.length) answer++;
  });
  return answer;
}
