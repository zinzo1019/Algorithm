N = int(input())

result = 0
coins = [500, 100, 50, 10]

for coin in coins:
    result += N // coin
    N %= coin

print(result)