import sys

case = int(sys.stdin.readline())

for i in range(case):
    times, s = sys.stdin.readline().split()
    times = int(times)
    slen = len(s)
        
    for j in range(slen):
        alphanumeric = s[j] * times
        print(alphanumeric, end = '')
    print('\n', end = '')
