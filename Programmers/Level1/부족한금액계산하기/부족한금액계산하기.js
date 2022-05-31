function solution(price, money, count) {
    const total = Array(count)
        .fill()
        .map((_, i) => {
            return (i + 1) * price;
        })
        .reduce((acc, cur) => acc + cur);

    return total >= money ? total - money : 0;
}
