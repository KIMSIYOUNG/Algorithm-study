def solution(array, commands):
    answer = []
    for index in range(len(commands)):
        condition = commands[index]
        each = array[condition[0] - 1:condition[1]]
        each.sort()
        answer.append(each[condition[2] - 1])

    return answer


def other(array, commands):
    answer = []
    for command in commands:
        index, last_index, point = command
        answer.append(sorted(array[index - 1:last_index])[point - 1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
print(other([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
