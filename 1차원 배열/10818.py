N = int(input())
a_list = list(map(int, input().split()))

a_list.sort()

print(a_list[0], end=" ")
print(a_list[N-1])
