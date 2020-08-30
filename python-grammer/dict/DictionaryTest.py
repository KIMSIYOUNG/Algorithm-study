try:
    a = {[1, 2]: 'hi'}
except TypeError:
    print('List can\' be key')

a = {(1, 2): 'hi'}
print(a)
