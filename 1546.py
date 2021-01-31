import sys

N = int(sys.stdin.readline())
mark = list(map(int, sys.stdin.readline().split()))

M = max(mark)
i = 0
new = []
while not(N == i):
    x = mark[i]
    x = x/M*100
    new.append(x)
    i += 1

print(sum(new)/N)
