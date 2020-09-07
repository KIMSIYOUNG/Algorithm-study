def mine():
    n = int(input())
    fear = list(map(int, input().split()))
    fear_set = set(fear)
    answer = 0

    for value in fear_set:
        if fear.count(value) >= value:
            answer += 1

    print(answer)
