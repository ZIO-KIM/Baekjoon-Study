# 시간초과 문제로 수정중

A, B, V = map(int, input().split())
length = A - B  # length 는 하루에 올라갈 수 있는 거리
day = 1  # day 는 걸리는 일수

print(V // length)
'''
while V - (length * day) > A:
    day += 1

day += 1 
print(day)
'''

