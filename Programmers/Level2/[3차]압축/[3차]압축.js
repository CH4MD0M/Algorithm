function solution(msg) {
  const answer = [];
  const dict = new Map(
    [...Array(26)].map((_, i) => {
      return [String.fromCharCode(i + 65), i + 1];
    })
  );

  let w = (c = 0);

  while (true) {
    c += 1;

    if (c === msg.length) {
      answer.push(dict.get(msg.slice(w, c)));
      break;
    }

    if (!dict.has(msg.slice(w, c + 1))) {
      dict.set(msg.slice(w, c + 1), dict.size + 1);
      answer.push(dict.get(msg.slice(w, c)));
      w = c;
    }
  }

  return answer;
}
