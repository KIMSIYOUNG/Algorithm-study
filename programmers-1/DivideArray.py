'''
파이썬에서 문자열, 튜플, 리스트가 비어있는 경우 False를 반환한다.
return문에서도 and | or 를 사용하면 boolean 유무를 판단하여 리턴한다.
둘을 합치면 return answer or -1 이 가능하다.
 - answer가 빈 리스트가 아니면 true이기에 그냥 리턴하고,
 빈 리스트라면 false를 리턴하여 or 뒤의 구문이 실행된다.
'''


def solution(arr, divisor):
    answer = sorted([v for v in arr if v % divisor == 0])

    return answer or -1


print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))
