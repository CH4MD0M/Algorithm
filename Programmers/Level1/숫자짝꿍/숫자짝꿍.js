function solution(X, Y) {
  const hashX = [...Array(10)].fill(0);
  const hashY = [...Array(10)].fill(0);

  [...X].forEach(item => hashX[item]++);
  [...Y].forEach(item => hashY[item]++);

  const answer = hashX.map((item, idx) => {
    if (item !== 0 && hashY[idx] !== 0) {
      return String(idx).repeat(Math.min(item, hashY[idx]));
    }
  });

  const result = answer.reverse().join('');

  return result ? (+result ? result : '0') : '-1';
}
