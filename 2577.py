import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

n = A * B * C
n = str(n)
n = list(n)


i = 0
while i < 10:
    
    print(n.count(str(i)))
    i += 1
