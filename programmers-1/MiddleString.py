def solution(s):
    s_list = list(s)
    result = []
    if len(s) % 2 != 0:
        return s_list[len(s) // 2]
    else:
        result.append(s_list[(len(s) // 2) - 1])
        result.append(s_list[(len(s) // 2)])
        return ''.join(result)


def other(s):
    return s[(len(s)-1) // 2:len(s) // 2 + 1]


print(solution('qwer'))
print(other('qwer'))
