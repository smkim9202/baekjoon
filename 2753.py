leapyear = int(input())

if leapyear % 4 == 0:
    if leapyear % 100 != 0:
        print(1)
    else:
        if leapyear % 400 == 0:
            print(1)
        else:
            print(0)
else:
    print(0)
