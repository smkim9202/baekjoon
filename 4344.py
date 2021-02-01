import sys

C = int(sys.stdin.readline())

for i in range(C):
    mate = list(map(int, sys.stdin.readline().split()))
    people = mate[0]
    score = mate[1:]
    ave = sum(score) / people

    n = 0
    for j in score:
        if ave < j:
            n = n + 1
        else:
            pass
    
    result = n / people * 100
    print("%0.3f%%" % result)
