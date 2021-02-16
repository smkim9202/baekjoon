N = int(input())
alphabetcnt = 0

for i in range(N):
    words = input()
    for x in range(len(words)-1):
        if words[x] == words[x + 1]:
            words.replace(words[x], '*')
            for y in words:
                if y != '*':
                    if words.count(y) != 1:
                        alphabetcnt += 1
    if alphabetcnt > 0:
        cnt = N -1       

print(cnt)
