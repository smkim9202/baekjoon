import sys

C = int(sys.stdin.readline())

for i in range(C):
    quiz = list(map(str, sys.stdin.readline()))

    score = 0
    add = 0
    for j in quiz:
        if j == 'O':
            score += 1
        else:
            score = 0
        add = add + score
    print(add)
