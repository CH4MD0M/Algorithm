function solution(food) {
  let letter = '';
  for (let i = 1; i < food.length; i++) {
    letter += String(i).repeat(Math.floor(food[i] / 2));
  }
  return letter + '0' + letter.split('').reverse().join('');
}
