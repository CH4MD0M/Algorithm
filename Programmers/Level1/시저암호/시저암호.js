function solution(s, n) {
    s = [...s];
    for (let i = 0; i < s.length; i++) {
        if (!/[a-zA-Z]/.test(s[i])) continue;
        if (s[i] === s[i].toUpperCase()) {
            s[i] = String.fromCharCode(
                ((s[i].charCodeAt() - 65 + n) % 26) + 65
            );
        } else if (s[i] === s[i].toLowerCase()) {
            s[i] = String.fromCharCode(
                ((s[i].charCodeAt() - 97 + n) % 26) + 97
            );
        }
    }
    return s.join("");
}
