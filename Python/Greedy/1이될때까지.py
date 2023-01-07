import sys

N, K = map(int, sys.stdin.readline().split())
answer = 0
while N >= K:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    answer += 1
print(answer)