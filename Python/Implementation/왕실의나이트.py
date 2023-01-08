import sys

pos = sys.stdin.readline()

columns = ['a','b','c','d','e','f','g','f']

columnIndex = columns.index(pos[0])
rowIndex = int(pos[1])-1

answer = 0
lst = [(-2, 1), (-2, -1), (2, 1), (2, -1),
       (1, 2), (1, -2), (-1, 2), (-1, -2)]

for i in range(8):
    tmpX = columnIndex + lst[i][0]
    tmpY = rowIndex + lst[i][1]
    if 0 <= tmpX <= 7 and 0 <= tmpY <= 7:
        answer += 1

print(answer)