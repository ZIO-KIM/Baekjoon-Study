score = []
addAll = 0
countGoodStudent = 0

C = int(input())

for _ in range(0, C):  # 테스트 케이스의 개수 C
    score = list(map(int, input().split()))
    N = score[0]  # 첫번째 입력된 수는 한 케이스의 학생수
    for i in range(1, N + 1):
        addAll += score[i]
    mean = addAll / N
    for i in range(1, N + 1):
        if score[i] > mean:
            countGoodStudent += 1
    percentage = round((countGoodStudent / N) * 100, 3)
    print("%.3f%%" % percentage)
    countGoodStudent = 0
    addAll = 0




