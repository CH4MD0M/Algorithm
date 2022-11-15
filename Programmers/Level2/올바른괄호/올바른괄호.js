function solution(s) {
  let count = 0;

  for (let p of s) {
    p === '(' ? count++ : count--;
    if (count < 0) return false;
  }
  return 0 < count ? false : true;
}
