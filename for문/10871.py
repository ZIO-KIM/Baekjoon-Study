N, X = map(int, input().split())
A_list = list(map(int, input().split()))

for i in range(0, N):
    if (A_list[i] < X):
        print("%d " % (A_list[i]), end="")
