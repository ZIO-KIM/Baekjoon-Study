# 수정중

str1 = str(input())
count = 0

for i in range(len(str1) - 2):  # 2글자짜리
    if str1[i] == 'c' and str1[i+1] == '=':
        count += 1
        i += 2
    if str1[i] == 'c' and str1[i+1] == '-':
        count += 1
        i += 2
    if str1[i] == 'd' and str1[i+1] == '-':
        count += 1
        i += 2
    if str1[i] == 'l' and str1[i+1] == 'j':
        count += 1
        i += 2
    if str1[i] == 'n' and str1[i+1] == 'j':
        count += 1
        i += 2
    if str1[i] == 's' and str1[i+1] == '=':
        count += 1
        i += 2
    if str1[i] == 'z' and str1[i+1] == '=':
        count += 1
        i += 2
    if str1[i] == 'd' and str1[i + 1] == 'z' and str1[i + 2] == '=':
        count += 1
        i += 3
    else:
        count += 1



print(count)

