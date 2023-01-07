import sys

N = int(sys.stdin.readline().rstrip())
cmds = list(sys.stdin.readline().split())

x, y = 1, 1

for cmd in cmds:
    if cmd == 'L':
        if x > 1: x -= 1
    elif cmd == 'R':
        if x < N: x += 1
    elif cmd == 'U':
        if y > 1: y -= 1
    elif cmd == 'D':
        if y < N: y += 1

print(y, x)