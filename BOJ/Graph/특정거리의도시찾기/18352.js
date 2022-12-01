const fs = require('fs');
const input = fs.readFileSync('./input.txt').toString().split('\n');
const [N, _, K, X] = input[0].split(' ').map(v => +v);

const graph = Array(N + 1)
  .fill()
  .map(() => Array());

for (let node of input.slice(1)) {
  let [a, b] = node.split(' ').map(v => +v);
  graph[a].push(b);
}

const distance = Array(N + 1).fill(-1);
distance[X] = 0;

const queue = new Queue();
queue.push(X);

while (queue.size()) {
  const v = queue.popleft();

  for (const node of graph[v]) {
    if (distance[node] === -1) {
      distance[node] = distance[v] + 1;
      queue.push(node);
    }
  }
}

let flag = false;
for (let i = 0; i < distance.length; i++) {
  if (distance[i] === K) {
    console.log(i);
    flag = true;
  }
}
if (!flag) console.log(-1);
