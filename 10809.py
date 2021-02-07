import sys

s = sys.stdin.readline()

ap = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
ap = ap.split()

result = []
for i in ap:
    sfind = s.find(i)
    result.append(sfind)

for j in result:
    print(j, end=' ')
