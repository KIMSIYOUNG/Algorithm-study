'''
각 단어를 공백을 기준으로 분리한다.
인덱스에 따라 upper lower 케이스를 적용한다.
1. 분리된 전체를 돌면서 한다 -> n**2
'''


def other(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split(' ')])


def solution(s):
    res = []
    for x in s.split(' '):
        word = ''
        for i in range(len(x)):
            c = x[i].upper() if i % 2 == 0 else x[i].lower()
            word = word + c
        res.append(word)
    return ' '.join(res)


print(solution("try         hello world"))
