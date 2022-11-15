function divide(w) {
  let w1 = 0,
    w2 = 0;
  [];
  for (let i = 0; i < w.length; i++) {
    w[i] == '(' ? w1++ : w2++;
    if (w1 === w2) return [w.slice(0, w1 + w2), w.slice(w1 + w2)];
  }
}

function check(u) {
  const stack = [];
  for (let chr of u) {
    if (chr === '(') {
      stack.push(chr);
    } else {
      if (!stack.length) return false;
      stack.pop();
    }
    return true;
  }
}

function solution(p) {
  if (!p.length) return '';

  let [u, v] = divide(p);

  if (check(u)) return u + solution(v);
  else {
    const tmp = [...u.slice(1, -1)]
      .map(item => (item === '(' ? ')' : '('))
      .join('');
    return '(' + solution(v) + ')' + tmp;
  }
}
