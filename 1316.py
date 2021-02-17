N = int(input())
cnt = 0
for i in range(N):
    words = input()
    for x in range(len(words)): 
        if x == len(words)-1:
            pass
        else:
            if words[x] != words[x + 1]:
                if words[x] in words[x+1:]:
                    cnt += 1
                    break
print(N - cnt)
