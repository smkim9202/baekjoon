def d(ctor):
    ctor_num = ctor
    for x in range(len(str(ctor))):
        ctor_num = ctor_num + ctor % 10
        ctor = ctor // 10
    return ctor_num

numbers = []
for i in range(1, 10001):
    numbers = numbers + [d(i)]

for j in range(1, 10001):
    if numbers.count(j) == 0:
        print(j)
