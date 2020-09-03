import random
import time

array = [5, 7, 9, 0, 3, 1, 3, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    answer = quick_sort(left_side) + [pivot] + quick_sort(right_side)
    return answer


big_array = []
for i in range(200000):
    big_array.append(random.randrange(0, 200000))

start = time.time()
print(quick_sort(big_array))
big_array.reverse()
end = time.time()
print(end - start)
