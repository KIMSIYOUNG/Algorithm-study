'''
1번 풀이 : 0.00001초가 최대
2번 풀이 : 0.333초가 최대
3번 풀이 : 1초가 최대
'''


def solution(a, b):
    x, y = min(a, b), max(a, b)

    count = y - x + 1
    return int((x + y) * count / 2)


def other(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


def with_for(a, b):
    result = 0
    for value in range(min(a, b), max(a, b) + 1):
        result += value
    return result


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))

print(other(3, 5))
print(other(3, 3))
print(other(5, 3))

print(with_for(3, 5))
print(with_for(3, 3))
print(with_for(5, 3))
