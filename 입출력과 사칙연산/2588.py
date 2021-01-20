a = int(input())
b = int(input())

tmp = b

while b > 0:
    k = a * (b % 10)
    print(k)
    b //= 10

print(a * tmp)
