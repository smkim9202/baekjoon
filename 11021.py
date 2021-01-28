import sys
T = sys.stdin.readline()
T = int(T)

result = []
for i in range(1,T+1):
    i = sys.stdin.readline()
    
    A, B = i.split()
    A = int(A)
    B = int(B)
    add = A + B
    result.append(add)

x = 0
for j in result:
    x = x + 1
    print("Case #%d: %d"%(x, j))
