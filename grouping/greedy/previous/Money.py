from itertools import combinations


def mine():
    n = int(input())
    money_delimiter = sorted(list(map(int, input().split())))
    expected = []

    if money_delimiter.count(1) == 0:
        return 1
    for a in range(len(money_delimiter) - 1):
        diff = money_delimiter[a + 1] - money_delimiter[a]
        if diff != 1:
            for b in range(money_delimiter[a] + 1, money_delimiter[a + 1], 1):
                expected.append(b)

    cases = get_number_cases(money_delimiter)

    for index, value in enumerate(expected):
        if value not in cases:
            print(value)

    print(sorted(expected)[0])


def get_number_cases(arr):
    combinations(arr, )


mine()
