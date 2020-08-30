example = (1, 2, 3, 4)

print(example + example)
print(example * 3)
print(example.index(1))

try:
    example[0] = '3'
    del example[0]
except TypeError:
    print('type error')
