import sys

N, X = sys.stdin.readline().split()
N = int(N)
X = int(X)


A = list(map(int, sys.stdin.readline().split()))

result = ""
for i in A:
    if X < i or X == i:
        pass
    else:
        result = result + '%d '%i
print(result)
