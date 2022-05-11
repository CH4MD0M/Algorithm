function solution(cacheSize, cities) {
    const cache = ["Jeju"];
    let time = 0;

    for (let city of cities) {
        city = city.toLowerCase();
        if (cacheSize) {
            if (!cache.filter((v) => v === city).length) {
                if (cache.length === cacheSize) {
                    cache.shift();
                }
                cache.push(city);
                time += 5;
            } else {
                cache.splice(cache.indexOf(city), 1);
                cache.push(city);
                time += 1;
            }
        } else {
            time += 5;
        }
    }
    return time;
}
