def hansu(N):
    count = 0
    if N < 100:
        return N
    else:
        for i in range(100, N+1):
            if i < 1000:
                o = i % 10
                t = (i // 10) % 10
                h = (i // 100) % 10
            
                if (h-t) == (t-o):
                    count += 1
        return (99 + count)


N = int(input())
print(hansu(N))
