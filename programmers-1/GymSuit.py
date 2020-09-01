def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()

    for index in range(1, n + 1):
        if index not in lost:
            answer += 1
        elif index in lost and index in reserve:
            lost.remove(index)
            reserve.remove(index)
            answer += 1

    for value in lost:
        if (value + 1 in reserve) and (value - 1 in reserve):
            del reserve[min(reserve.index(value + 1), reserve.index(value - 1))]
            answer += 1

        elif (value + 1 in reserve) or (value - 1 in reserve):
            if reserve.count(value + 1) == 1:
                answer += 1
                reserve.remove(value + 1)
            else:
                answer += 1
                reserve.remove(value - 1)

    return answer


def other(n, lost, reserve):
    answer = 0
    for index in range(1, n + 1):
        if index not in lost:
            answer += 1
        elif index in lost and index in reserve:
            answer += 1
            lost.remove(index)
            reserve.remove(index)
    for value in lost:
        if value - 1 in reserve:
            answer += 1
            reserve.remove(value - 1)
        elif value + 1 in reserve:
            answer += 1
            reserve.remove(value + 1)
    return answer

print(solution(5, [2, 4], [1, 2, 5]))
print(other(5, [2, 4], [1, 2, 5]))
