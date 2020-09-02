def solution():
    n = int(input())
    x, y = 1, 1
    plans = input().split()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    types = ['L', 'R', 'U', 'D']

    for plan in plans:
        index = types.index(plan)
        nx = x + dx[index]
        ny = y + dy[index]
        if nx <= 0 or nx > n or ny <= 0 or ny > n:
            continue
        x = nx
        y = ny
    return str(x) + ' ' + str(y)


print(solution())
