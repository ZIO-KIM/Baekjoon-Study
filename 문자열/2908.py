A, B = map(str, input().split())
rev_A = A[::-1]  # 문자열을 하나씩 반대로 잘라서 다시 입력시킨 후 출력
rev_B = B[::-1]

if rev_A > rev_B:
    print(rev_A)
else:
    print(rev_B)
