function solution(s) {
    let zeroCount = 0;
    let binCount = 0;

    while (s.length > 1) {
        zeroCount += (s.match(/0/g) || []).length;
        s = s.replace(/0/g, "").length.toString(2);
        binCount += 1;
    }
    return [binCount, zeroCount];
}
