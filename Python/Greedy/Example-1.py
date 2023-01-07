import sys

N = int(sys.stdin.readline().rstrip())
coins = [500, 100, 50, 10]
answer = 0

for coin in coins:
    answer += N // coin
    N = N % coin

print(answer)