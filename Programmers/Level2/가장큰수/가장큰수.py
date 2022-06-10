import functools

def compare(a, b):
    return (int(a + b) > int(b + a)) - (int(a + b) < int(b + a))
    
def solution(numbers):
    num_lst=[str(n) for n in numbers]
    num_lst.sort(key = functools.cmp_to_key(compare), reverse = True)
    return str(int(''.join(num_lst)))