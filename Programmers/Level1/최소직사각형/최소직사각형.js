function solution(sizes) {
    const width = [];
    const height = [];
    sizes.map((e) => {
        e.sort((a, b) => a - b);
        width.push(e[1]);
        height.push(e[0]);
    });
    console.log(Math.max(...width) * Math.max(...height));
}

// 다른 풀이
function solution(sizes) {
    return (
        Math.max(...sizes.map((e) => Math.max(...e))) *
        Math.max(...sizes.map((e) => Math.min(...e)))
    );
}
