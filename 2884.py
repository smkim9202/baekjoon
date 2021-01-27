H, M = input().split()

H = int(H)
M = int(M)

t = H * 60 + M - 45

if t % 60 == 0:
    if t//60 == -1:
        print(23, 0)
    else:
        print(t//60, 0)
else:
    if t//60 == -1:
        print(23, t%60)
    else:
        print(t//60, t%60)
