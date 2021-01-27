leap_year = input()

leap_year = int(leap_year)


if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
