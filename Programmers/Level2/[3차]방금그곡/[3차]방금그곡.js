function solution(m, musicinfos) {
  const answer = [];
  m = m.replace(/(\D)#/g, (_, c) => c.toLowerCase());

  for (let musicinfo of musicinfos) {
    let [start, end, title, code] = musicinfo.split(",");

    let [start_hour, start_minute] = start.split(":");
    let [end_hour, end_minute] = end.split(":");
    const duration = (end_hour - start_hour) * 60 + +end_minute - start_minute;

    code = code.replace(/(\D)#/g, (_, c) => c.toLowerCase());
    code = code.repeat(Math.floor(duration / code.length) + 1);
    code = code.slice(0, duration);

    if (code.includes(m))
      answer.push([duration, start_hour * 60 + +start_minute, title]);
  }

  if (answer.length) {
    return answer.sort((a, b) => {
      if (a[0] > b[0]) return -1;
      if (a[0] < b[0]) return 1;
      if (a[1] > b[1]) return 1;
      if (a[1] < b[1]) return -1;
    })[0][2];
  }
  return "(None)";
}
