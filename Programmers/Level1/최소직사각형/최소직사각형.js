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
