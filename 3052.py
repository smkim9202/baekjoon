import sys

i = 0
remainder = []
while i < 10:
    x = int(sys.stdin.readline())
    i += 1
    remainder.append(x % 42)

remainder = set(remainder)
print(len(remainder))
