H, M = map(int, input().split())

alarm = (H * 60 + M) - 45


if alarm // 60 == -1:
    print(23, alarm % 60)
else:
    print(alarm // 60, alarm % 60)

