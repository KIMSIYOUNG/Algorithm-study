def mine():
    n = input()
    answer = int(n[0])

    for i in range(len(n)):
        if (i + 1) == len(n):
            break
        if int(n[i]) + int(n[i + 1]) >= int(n[i]) * int(n[i + 1]):
            answer += int(n[i + 1])
        else:
            answer *= int(n[i + 1])
    return answer


print(mine())
