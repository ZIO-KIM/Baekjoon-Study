'''
cut은 0, 1, 2, 3, ... 번째 문자열
만약 result[cut] == 'X' 라면 점수는 무조건 0일 것 (연속이 끊어짐)
result[cut] == 'O' 라면 cut 번째 문자열부터 1씩 줄여가며
연속된 O이 몇개나 있는지 검사
'''

score = 0
cut = 0

N = int(input())

for i in range(0, N):
    result = input()  # 각 테스트 케이스의 문자열 입력
    while cut < len(result):
        if result[cut] == 'O':
            tmp = cut
            while result[tmp] == 'O' and tmp >= 0:
                score += 1
                tmp -= 1
        cut += 1
    print(score)
    score = 0
    cut = 0

