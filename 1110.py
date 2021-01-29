import sys
    
N = sys.stdin.readline()
N = int(N)

count = 0
new = 0
out = N

while True:
    if N < 10:
        add = 0 + N
        b = add
    else:
        a = N // 10
        b = N % 10
        add = a + b

    y = add % 10
    new = b*10 + y

    count = count + 1
    
    if out == new:
        break
    N = new

print(count)
