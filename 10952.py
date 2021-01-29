import sys

A, B = sys.stdin.readline().split()
A = int(A)
B = int(B)

while not (A == B == 0):
    print(A + B)
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
