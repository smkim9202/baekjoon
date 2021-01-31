import sys

count = 0
Nlist = []
while count < 9:    
    N = int(sys.stdin.readline())
    Nlist.append(N)
    count = count + 1

print(max(Nlist))
print(Nlist.index(max(Nlist))+1)
