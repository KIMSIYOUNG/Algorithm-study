array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count_array = [0] * (max(array) + 1)
for value in array:
    count_array[value] += 1

for i in range(len(count_array)):
    for j in range(count_array[i]):
        print(i, end=' ')

for i in range(len(count_array)):
    print(i, end=' ')
    if i > 1:
        continue
