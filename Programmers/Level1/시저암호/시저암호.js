function solution(s, n) {
    s = [...s];

    for (let i = 0; i < s.length; i++) {
        if (/^[A-Z]*$/.test(s[i])) {
            s[i] = String.fromCharCode(
                ((s[i].charCodeAt(0) - 65 + n) % 26) + 65
            );
        } else if (/^[a-z]*$/.test(s[i])) {
            s[i] = String.fromCharCode(
                ((s[i].charCodeAt(0) - 97 + n) % 26) + 97
            );
        }
    }

    return s.join("");
}
