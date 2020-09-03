def dfs(graph, v, visits):
    visits[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visits[i]:
            dfs(graph, i, visits)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visits = [False] * 9
dfs(graph, 1, visits)
