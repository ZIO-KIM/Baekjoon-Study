# Can multiply string when python used
N = int(input())

for i in range(1, N+1):
    print("*" * i)
    
''' # C type code (first thought)
N = int(input())

for i in range(1, N+1):
    for j in range(0, i):
        print("*", end='')
    print()
'''
