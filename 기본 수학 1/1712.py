A, B, C = map(int, input().split())

if C - B == 0:  # avoid dividebyzero
    print(-1)
elif A / (C - B) <= 0:  # avoid when there is no break-even point (손익분기점이 없을 경우) 
    print(-1)
else:  # when break-even point exists
    N = int(A / (C - B))
    print(N + 1)

