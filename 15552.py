import sys
T = sys.stdin.readline()
T = int(T)


for i in range(1,T+1):
    i = sys.stdin.readline()
    
    A, B = i.split()
    A = int(A)
    B = int(B)
    print(A + B)
