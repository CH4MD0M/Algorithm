function solution(k, m, score) {
  let answer = 0;
  const sorted = score.sort((a, b) => a - b).slice(score.length % m);
  for (let i = 0; i < sorted.length; i += m) answer += sorted[i] * m;

  return answer;
}
