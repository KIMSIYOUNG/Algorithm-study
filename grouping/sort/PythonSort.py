array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
print(result)
print(array)
array.sort()
print(array)

tuple_array = [('사과', 1), ('오렌지', 3), ('수박', 2)]


def setting(data):
    return data[1]


result2 = sorted(tuple_array, key=setting)
print(tuple_array)
tuple_array.sort(key=setting)
print(tuple_array)
print(result2)
