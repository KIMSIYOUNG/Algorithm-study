def coin_count(value):
    coins = [500, 100, 50, 10]
    count = 0

    for coin in coins:
        count += value // coin
        value = value % coin

    return count


print(coin_count(1260))
