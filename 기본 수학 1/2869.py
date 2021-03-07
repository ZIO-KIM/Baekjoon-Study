# 구글링하여 참고했음

A, B, V = map(int, input().split())
day = (V - B) / (A - B)  # 아침에 한번에 올라가는 경우를 고려

if day == int(day):  # 4.0일 경우 4이다
    print(int(day))
else:   # 4.2일 경우 5이다 (4.2일은 없음)
    print(int(day) + 1)


'''
# 틀린코드 (시간초과)  

A, B, V = map(int, input().split())
length = A - B  # length 는 하루에 올라갈 수 있는 거리
day = 1  # day 는 걸리는 일수

while V - (length * day) > A:
    day += 1

day += 1 

print(day)  
'''

