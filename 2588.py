A = int(input())
B = int(input())

o = A * (B%10)
t = A * ((B%100)-(B%10))
m = A * (B-(B%100))
mul = o + t + m

print(o, t//10, m//100, mul, sep='\n')
