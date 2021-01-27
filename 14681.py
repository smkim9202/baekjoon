A = input()
B = input()

A = int(A)
B = int(B)


if 0 < A:
    if 0 < B:
        print(1)
    else:
        print(4)
else:
    if 0 < B:
        print(2) 
    else:
        print(3)
