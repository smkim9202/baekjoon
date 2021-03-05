def star(N):
    three = N // 3
    a = "***"
    b = "* *"
    c = "***"
    d = (a*three)+"\n"+(b*three)+"\n"+(c*three)+"\n"
    if three == 1:
        return d
    else:
        return d * three
        
print(star(9))
