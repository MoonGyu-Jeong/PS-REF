import sys

N, M, K = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0

maxFirst = max(numbers)
numbers.remove(max(numbers))
maxSecond = max(numbers)

answer += (M // (K+1)) * (K * maxFirst + maxSecond)
answer += (M % (K+1)) * maxFirst

print(answer)