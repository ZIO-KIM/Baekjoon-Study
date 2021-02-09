T = int(input())

for _ in range(T):
    R, str1 = input().split()
    R = int(R)
    for i in range(len(str1)):
        for _ in range(R):
            print(str1[i], end="")
    print()
