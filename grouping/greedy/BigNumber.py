def solution(arr_size, count, continuous, arr):
    arr.sort()
    arr.reverse()
    answer = 0

    while count != 0:
        for c in range(continuous):
            answer += arr[0]
            count -= 1
        answer += arr[1]
        count -= 1

    return answer


n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / k + 1) * k
count += m % (k + 1)

result += first * count
result += second * (m - count)

print(result)

print(solution(5, 8, 3, [5, 5, 3]))
