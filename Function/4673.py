# 1차 제출 때 시간초과가 떠서, 다음과 같이 수정함
# find_self_num 내의 index를 0부터 오름차순이 아닌 num-1부터 내림차순으로 수정
# 생성자가 하나라도 있다면, break 하도록 하는 코드 추가하여 불필요한 반복 없앰
# Pypy3로 제출시 시간초과 문제가 해결될 때도 있다. (참고) 

def find_self_num(num):
    count = 0  # 생성자 갯수 세기
    constructor = 0  # 생성자 여부 판별

    for i in range(num - 1, 0, -1):  # num보다 작은 숫자 중에 생성자가 있는지 전부 봐야함
        tmp = i
        while i > 0:
            constructor += i % 10
            i //= 10
        if constructor+tmp == num:  # 생성자가 있다면
            count += 1  # 생성자 갯수 +1
            break

        constructor = 0

    return count


for i in range(1,10000):
    k = find_self_num(i)
    if k == 0:  # 생성자가 없다면
        print(i)

