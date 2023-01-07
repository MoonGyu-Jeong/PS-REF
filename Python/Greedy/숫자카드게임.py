import sys

N, M = map(int, sys.stdin.readline().split())
lst = [0] * N
for i in range(N):
    lst[i] = min(list(map(int, sys.stdin.readline().split())))

print(max(lst))