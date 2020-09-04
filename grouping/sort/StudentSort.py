n = int(input())
array = []
for i in range(n):
    inp = input()
    array.append((inp.split()[0], inp.split()[1]))

result = sorted(array, key=lambda student: student[1])
for value in result:
    print(value[0], end=' ')
