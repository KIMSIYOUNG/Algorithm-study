def solution():
    m, n = map(int, input().split())
    all_list = []
    for count in range(m):
        value = list(map(int, input().split()))
        all_list.append(min(value))
    return max(all_list)


def other():
    m, n = map(int, input().split())
    max_result = 0
    for count in range(m):
        value = list(map(int, input().split()))
        max_result = max(max_result, min(value))

    return max_result


print(solution())
print(other())
