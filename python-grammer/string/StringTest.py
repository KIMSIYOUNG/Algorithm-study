def escape():
    print('it\'s beautiful day')


def long_string():
    print('''
    Life is too short
    You need python
    Python is powerful language        
    ''')


def wtf_string_multiply():
    print("string example" * 3)


def slice_example():
    a = "20010331Rainy"
    year = a[:4]
    day = a[4:8]
    weather = a[8:]
    return year, day, weather
