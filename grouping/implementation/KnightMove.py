def solution():
    location = input()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    chars = ['a', 'b', 'c', 'd', 'e', 'g', 'h']
    x = numbers[chars.index(location[0])]
    y = int(location[1])
    answer = 0

    dxy = [
        (x - 2, y - 1), (x - 2, y + 1), (x - 1, y + 2), (x + 1, y + 2),
        (x + 2, y + 1), (x + 2, y - 1), (x - 1, y - 2), (x + 1, y - 2)
    ]

    for index in range(len(dxy)):
        if (0 < dxy[index][0] < 9) and (0 < dxy[index][1] < 9):
            answer += 1
    return answer


print(solution())
