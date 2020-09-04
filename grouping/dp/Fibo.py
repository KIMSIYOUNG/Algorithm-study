def fibo(value):
    if value == 1 or value == 2:
        return 1
    return fibo(value - 1) + fibo(value - 2)


print(fibo(4))
