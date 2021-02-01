import sys

C = int(sys.stdin.readline())

i = 0
while C != i:
    i += 1
    mate = list(map(int, sys.stdin.readline().split()))
    people = mate[0]
    tall = mate[1:]
    arv = sum(tall) / people

    j = 0
    n = 0
    while people != j:
        if arv < tall[j]:
            n = n + 1
        else:
            pass
        j = j + 1
    
    result = n / people * 100
    print("%0.3f%%" % result)
