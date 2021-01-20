import sys

a, b = input().split()
a = int(a)
b = int(b)

if a < 1 or b > 10000:
    sys.exit()
else:
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
