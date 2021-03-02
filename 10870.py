def pina(num):
    if num <= 1:
        return num
    else:
        return pina(num-1) + pina(num-2)

num = int(input())
print(pina(num))
