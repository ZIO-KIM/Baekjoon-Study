def IsometricSe_func(num):  # 한수 판별 함수
    count = 0
    if num < 100:  # 100 이하의 한자리 / 두 자리 수는 모두 한수임
        count = num
    else:
        count += 99
        for i in range(100, num + 1):
            if i // 100 >= i % 10:  # 백의 자리가 일의 자리보다 크다면
                t1 = i // 100 - ((i // 10) % 10)  # t1은 백의 자리 - 십의 자리
                t2 = ((i // 10) % 10) - i % 10  # t2는 십의 자리 - 일의 자리
                if t1 == t2:  # 공차가 같다면 갯수 +1
                    count += 1
            else:  # 일의 자리가 백의 자리보다 크다면
                t1 = i % 10 - ((i // 10) % 10)  # t1은 일의 자리 - 십의 자리
                t2 = ((i // 10) % 10) - i // 100  # t2는 십의 자리 - 백의 자리
                if t1 == t2:  # 공차가 같다면 갯수 +1
                    count += 1
    return count


N = int(input())
print(IsometricSe_func(N))





