import random
import time


def count_sort(arr):
    count_array = [0] * (max(arr) + 1)
    answer = []
    for value in arr:
        count_array[value] += 1

    for i in range(len(count_array)):
        for j in range(count_array[i]):
            answer.append(i)
    return answer


big_array = []
for i in range(1000000):
    big_array.append(random.randrange(0, 1000000))

start = time.time()
print(count_sort(big_array))
end = time.time()

py_start = time.time()
big_array.sort()
print(big_array)
py_end = time.time()

print('계수 정렬 시간 : ' + str(end - start))
print('내장 정렬 시간 : ' + str(py_end - py_start))
