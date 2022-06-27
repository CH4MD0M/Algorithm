# stack 관련 문제

-   레벨1. 같은 숫자는 싫어
-   레벨2. 짝지어 제거하기
-   레벨2. 괄호 회전하기
-   레벨2. 올바른 괄호

```python
def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
```

```python
def solution(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()

    return not stack
```

<br><br>

# dictionary

### dict.get()

첫 번째 인자로 찾고자 하는 키를 넣고, 두 번째 인자로 첫 번째 인자에서 넣은 키가 없을 때 넣고자 하는 값을 넣는다.

```python
def solution(clothes):
    answer = 1
    clothe_dict = {}

    for clothe, kind in clothes:
        clothe_dict[kind] = clothe_dict.get(kind, 0) + 1
```

-   프로그래머스 레벨2 위장

### dict() 열거

dictionary는 for in 문으로 순회할 때 `key` 값을 기준으로 순회하게 된다.

**`keys()`**, **`values()`**, **`items()`** 로 배열로 dict 내부를 열거할 수 있다.

```python
table = {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
};
```

```python
table.keys()
'''
dict_keys(['zero', 'one', 'two', 'three', 'four',
'five', 'six', 'seven', 'eight', 'nine'])
'''
```

```python
table.values()
'''
dict_values([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
'''
```

```python
table.items()
'''
dict_items([('zero', 0), ('one', 1), ('two', 2), ('three', 3), ('four', 4),
('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)])
'''
```

<br><br>

# defaultdict()

딕셔너리를 만드는 dict클래스의 서브클래스이다.

작동하는 방식은 거의 동일하고, **인자로 주어진 객체의 기본값을 딕셔너리의 초깃값으로 지정할 수 있다.**

```python
from collections import defaultdict

int_dict = defaultdict(int)
set_dict = defaultdict(set)
```

```python
int_dict # defaultdict(int, {})
set_dict # defaultdict(set, {})
```

<br><br>

# 아스키 코드(ASCII code) 관리

**`‘a’`** 의 아스키코드는 97이고, **`‘z’`** 의 아스키 코드는 122이다.

**`‘A’`** 의 아스키코드는 65이고, **`‘Z’`** 의 아스키 코드는 90이다.

알파벳은 **`26`** 자이다.

### chr()

아스키 코드 값을 문자로 변환해 주는 함수이다.

```python
chr(65)  # 'A'
chr(97)  # 'a'
chr(90)  # 'Z'
chr(122) # 'z'
```

### ord()

특정 문자를 아스키 코드 값으로 변환해 주는 한수이다.

```python
ord('A') # 65
ord('a') # 97
ord('Z') # 90
ord('z') # 122
```

<br><br>

# 대소문자 관리

### **upper()**, **lower()**

문자열을 대문자 또는 소문자로 변경한다.

```python
text1 = 'hello world'
text2 = 'HELLO WORLD'
print(text1.upper()) # 'HELLO WORLD'
print(text2.lower()) # 'hello world'
```

### **isupper()**, **islower()**

문자열의 전체가 소문자인지 대문자인지 Boolean형태(True,Flase)로 구분해준다.

```python
text = 'hello world'
print(text.isupper()) # False
print(text.islower()) # True
```

<br><br>

# 리스트에서 빈 문자열 제거

### 1. list comprehension

```python
arr = ['a', '', 'bb', '', 'cccc']
arr = [e for e in arr if e]
arr   # ['a','bb','cccc']
```

### 2. join(), split()

```python
arr = ['a', '', 'bb', '', 'cccc']
arr = ' '.join(arr).split()
arr   # ['a','bb','cccc']
```

### 3. filter()

```python
arr = ['a', '', 'bb', '', 'cccc']
arr = list(filter(None, arr)) # OR arr = list(filter(bool, arr))
arr   # ['a','bb','cccc']
```

<br><br>

# 문자열 체크하기(isalpha, isalnum, isdigit)

### isalpha

문자열이 영어 또는 한글로만 이루어져 있는지 판별하고 `True` 또는 `False`를 반환한다.

공백, 특수 문자, 숫자가 포함되어 있으면 `False`를 반환한다.

```python
s = 'OneTwoThReE'

s.isalpha()
```

### isalnum()

문자열이 영어, 한글, 숫자로만 이루어져 있는지 판별하고 `True` 또는 `False`를 반환한다.

공백, 특수 문자가 포함되어 있으면 `False`를 반환한다.

```python
s = 'One2ThReE'

s.isalnum() # True
```

### isnumeric(), isdigit(), isdecimal()

3개 함수 모두 문자열이 숫자로만 이루어져 있는지 판별하고 `True` 또는 `False`를 반환한다.

숫자 이외의 문자(공백 포함)가 포함되어 있으면 `False`를 반환한다.

```python
s = '123'

s.isnumeric() # True
s.isdigit() # True
s.isdecimal() # True
```

<br><br>

# 2차원 리스트 합치기

```python
matrix = [[1, 0, 0, 0], [2, 9, 0, 0], [3, 10, 8, 0], [4, 5, 6, 7]]

merged = [data for inner_list in lst for data in inner_list]

# 위 코드는 아래와 같다.
merged = []
for inner_list in lst:
	for data in inner_list:
		merged.append(data)

print(merged) # [1, 0, 0, 0, 2, 9, 0, 0, 3, 10, 8, 0, 4, 5, 6, 7]
```

<br><br>

# 진수 변환

### 10진수 → n진수 변환

```python
def convert(num, base):
    temp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    q, r = divmod(num, base)
    return convert(q, base) + temp[r] if q else temp[r]
```

```python
# n은 10진수이다.
# 뒤집어서 출력되기 때문에 문자열을 반대로 출력해야 한다.
def convert(n, q):
		rev_base = ''

		while n > 0:
				n, mod = divmod(n, q)
				rev_base += str(mod)

		return rev_base[::-1]
```

<br><br>

# 소수 판별하기

```python
def isPrime(n):
    if n in (0, 1):
        return False

    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))
```

```python
def isPrime(n):
    if n in (0, 1):
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

<br><br>

# 최대 공약수, 최소 공배수 구하기

```python
# 최대 공약수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최소 공배수
def lcm(a, b):
    return a * b // gcd(a, b)

# lambda 함수
gcd = lambda a, b : a if not b else gcd(b, a % b)
lcm = lambda a, b : a * b // gcd(a, b)
```

<br><br>

# 2차원 배열 초기화

```python
# rows, columns가 주어질 때
# 한 칸씩 더 추가해서 인덱스가 아닌 행렬값으로 접근할 수 있게 한다.
matrix = [[0 for _ in range(columns + 1)]for _ in range(rows + 1)]

# n이 주어질 때
matrix = [[0] * (n + 1) for _ in range(n + 1)]
```

<br><br>

# sort 메서드 compare

```python
# 프로그래머스 가장 큰 수
import functools

def compare(a, b):
    return (int(a + b) > int(b + a)) - (int(a + b) < int(b + a))

def solution(numbers):
    num_lst = [str(n) for n in numbers]
    num_lst.sort(key=functools.cmp_to_key(compare), reverse=True)
    return str(int(''.join(num_lst)))
```

<br><br>

# 순열, 조합 파이썬 구현

### 조합(Combinations)

```python
def combinations(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for comb in combinations(arr[i + 1:], n - 1):
                result.append([arr[i]] + comb)

    return result
```

### 순열(Permutations)

```python
def permutations(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for perm in permutations(ans, n-1):
                result.append([arr[i]] + perm)

    return result
```
