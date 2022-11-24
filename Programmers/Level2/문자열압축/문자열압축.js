function solution(s) {
  let answer = s.length;

  for (let step = 1; step <= s.length / 2; step++) {
    let count = 1;
    let prev = s.slice(0, step);
    let compressed = '';

    for (let i = step; i < s.length; i += step) {
      if (prev === s.slice(i, i + step)) {
        count++;
      } else {
        compressed += count >= 2 ? String(count) + prev : prev;
        count = 1;
        prev = s.slice(i, i + step);
      }
    }
    compressed += count >= 2 ? String(count) + prev : prev;
    answer = Math.min(answer, compressed.length);
  }
  return answer;
}
