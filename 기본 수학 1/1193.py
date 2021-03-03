X = int(input())
i = 0
k = 0
count = 1

while i < X:  # +1, +2, +3, ...
    k += 1
    i += k

# k -> 찾으려는 분수가 몇번째 묶음에 있는지 알려준다
# 분모와 분자의 합은 k + 1
# k가 짝수면 분자 1부터 시작
# k가 홀수면 분모 1부터 시작

if k % 2 == 0:
    denominator = i - X + 1  # 분모 1부터 시작
    numerator = k + 1 - denominator  # 분자 + 분모는 k + 1
else:
    numerator = i - X + 1  # 분자 1부터 시작
    denominator = k + 1 - numerator  # 분자 + 분모는 k + 1

print(numerator, end="")
print('/', end="")
print(denominator, end="")


