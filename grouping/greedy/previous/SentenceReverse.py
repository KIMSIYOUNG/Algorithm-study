n = list(input())
zero = n.count('0')
one = n.count("1")
answer = 0

if zero >= one:
    for i in range(len(n)):
        if n[i] == '0':
            continue
        else:
            answer += 1
            n[i] = '0'
            for j in range(i + 1, len(n)):
                if n[j] == '1':
                    n[j] = '0'
else:
    for i in range(len(n)):
        if n[i] == '1':
            continue
        else:
            answer += 1
            n[i] = '1'
            for j in range(i + 1, len(n)):
                if n[j] == '0':
                    n[j] = '1'

print(answer)
