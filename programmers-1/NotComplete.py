import collections


def solution(participant, completion):
    participant.sort()
    completion.sort()

    for index in range(len(completion)):
        if participant[index] != completion[index]:
            return participant[index]
        else:
            return participant[len(participant) - 1]


def other(participant, completion):
    item = collections.Counter(participant) - collections.Counter(completion)

    return list(item.keys())[0]


print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']))
print(other(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']))

