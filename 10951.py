import sys

while True:
    try:
        A, B = sys.stdin.readline().split()
        A = int(A)
        B = int(B)
        print(A + B)
    except:
        break
