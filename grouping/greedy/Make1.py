def solution():
    n, k = map(int, input().split())
    count = 0

    while n != 1:
        if n % k == 0:
            n = n // k
            count += 1
        else:
            rest = n % k
            n = n - rest
            count += rest

    return count


def other():
    n, k = map(int, input().split())
    result = 0

    while True:
        target = (n // k) * k
        result += (n - target)
        n = target
        if n < k:
            break
        result += 1
        n //= k

    result += (n - 1)
    print(result)


print(solution())
