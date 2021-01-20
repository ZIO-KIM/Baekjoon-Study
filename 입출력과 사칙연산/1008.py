import sys

a, b = input().split()
a = int(a)
b = int(b)

if a <= 0 or b >= 10:
    sys.exit()
else:
    print(a / b)
