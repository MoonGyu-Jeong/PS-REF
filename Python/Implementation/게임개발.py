import sys

N, M = map(int, sys.stdin.readline().split())
A, B, d = map(int, sys.stdin.readline().split())
lst = [0] * N
for i in range(N):
    lst[i] = list(map(int, sys.stdin.readline().split()))

nextDir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = [0, 1, 2, 3]
count = 0
answer = 1
while True:
    lst[A][B] = 'X'
    d = dir[d-1]
    tmpX = nextDir[d][1]
    tmpY = nextDir[d][0]
    if 0 <= B+tmpX < M and 0 <= A+tmpY < N:
        pass
    else:
        continue
    if lst[A+tmpY][B+tmpX] == 0:
        B += tmpX
        A += tmpY
        answer += 1
        count = 0
        continue
    count += 1
    if count == 4:
        if lst[A+nextDir[(d+2)%4][0]][B+nextDir[(d+2)%4][1]] == 1:
            break
        B += nextDir[(d+2)%4][0]
        A += nextDir[(d+2)%4][1]
print(answer)