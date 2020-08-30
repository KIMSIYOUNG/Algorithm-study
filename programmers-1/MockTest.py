def solution(answers):
    first = [1, 2, 3, 4, 5]
    first = first * (len(answers) // 5) + first[:(len(answers) % 5)]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    second = second * (len(answers) // 8) + second[:(len(answers) % 8)]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    third = third * (len(answers) // 10) + third[:(len(answers) % 10)]

    first_count = 0
    second_count = 0
    third_count = 0

    for index in range(len(answers)):
        if answers[index] == first[index]:
            first_count += 1
        if answers[index] == second[index]:
            second_count += 1
        if answers[index] == third[index]:
            third_count += 1

    result = {1: first_count, 2: second_count, 3: third_count}
    max_value = max(result.values())
    answer = []

    for index, value in result.items():
        if value == max_value:
            answer.append(index)

    return answer


def other(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for index, item in enumerate(answers):
        if item == pattern1[index % (len(pattern1))]:
            score[0] += 1
        if item == pattern2[index % (len(pattern2))]:
            score[1] += 1
        if item == pattern3[index % (len(pattern3))]:
            score[2] += 1

    for index, item in enumerate(score):
        if item == max(score):
            result.append(index + 1)

    return result


print(solution([1, 2, 3, 4, 5]))
print(other([1, 2, 3, 4, 5]))
