function rotate(arr) {
  let n = arr.length;
  let m = arr[0].length;
  const result = Array(n)
    .fill(0)
    .map(() => Array(m).fill(0));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      result[j][n - i - 1] = arr[i][j];
    }
  }
  return result;
}

function check(matrix) {
  const len = matrix.length / 3;
  for (let i = len; i < 2 * len; i++) {
    for (let j = len; j < 2 * len; j++) {
      if (matrix[i][j] !== 1) return false;
    }
  }
  return true;
}

function solution(key, lock) {
  const n = lock.length;
  const m = key.length;

  let matrix = Array(n * 3)
    .fill(0)
    .map(() => Array(n * 3).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      matrix[i + n][j + n] = lock[i][j];
    }
  }

  for (let i = 0; i < 4; i++) {
    key = rotate(key);
    for (let i = 0; i < n * 2; i++) {
      for (let j = 0; j < n * 2; j++) {
        for (let x = 0; x < m; x++) {
          for (let y = 0; y < m; y++) {
            matrix[i + x][j + y] += key[x][y];
          }
        }

        if (check(matrix)) return true;

        for (let x = 0; x < m; x++) {
          for (let y = 0; y < m; y++) {
            matrix[i + x][j + y] -= key[x][y];
          }
        }
      }
    }
  }
  return false;
}
