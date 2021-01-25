# 입력이 끝날 때까지 반복 (EOF 활용)

while True:
    try:
        A,B = map(int, input().split())
        print(A+B)
    except EOFError:
        break

