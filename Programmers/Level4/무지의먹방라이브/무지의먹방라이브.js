function solution(food_times, k) {
  let sum = 0;
  let previous = 0;
  let remainFood = food_times.length;
  const foods = food_times
    .map((v, i) => {
      sum += v;
      return [v, i + 1];
    })
    .sort((a, b) => b[0] - a[0]);

  if (sum <= k) return -1;

  while ((foods[foods.length - 1][0] - previous) * remainFood <= k) {
    let now = foods.pop()[0];
    k -= (now - previous) * remainFood;
    remainFood--;
    previous = now;
  }

  foods.sort((a, b) => a[1] - b[1]);
  return foods[k % remainFood][1];
}
