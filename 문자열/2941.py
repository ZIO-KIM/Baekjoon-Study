# 출처 - https://hongku.tistory.com/255
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str1 = input()

for t in lst: 
    str1 = str1.replace(t, '*')

print(len(str1))


# 이하 틀린코드    
# 더 공부하자 ..

str1 = str(input())
count = 0

for i in range(0, len(str1)):
    if str1[i:i+2] == 'c=':
        count += 1

str1 = str1.replace("c=", "")  # 해당 문자열 삭제

for i in range(0, len(str1) - 2):
    if str1[i:i+2] == 'c-':
        count += 1

str1 = str1.replace("c-", "")  # 해당 문자열 삭제

for i in range(0, len(str1) - 3):
    if str1[i:i+3] == 'dz=':
        count += 1

str1 = str1.replace("dz=", "")  # 해당 문자열 삭제

for i in range(0, len(str1) - 2):
    if str1[i:i+2] == 'd-':
        count += 1

str1 = str1.replace("d-", "")  # 해당 문자열 삭제

for i in range(0, len(str1) - 2):
    if str1[i:i+2] == 'lj':
        count += 1

str1 = str1.replace("lj", "")  # 해당 문자열 삭제

for i in range(0, len(str1) - 2):
    if str1[i:i+2] == 'nj':
        count += 1

str1 = str1.replace("nj", "")  # 해당 문자열 삭제

for i in range(0, len(str1) - 2):
    if str1[i:i+2] == 's=':
        count += 1

str1 = str1.replace("s=", "")  # 해당 문자열 삭제

for i in range(0, len(str1) - 2):
    if str1[i:i+2] == 'z=':
        count += 1

str1 = str1.replace("z=", "")  # 해당 문자열 삭제

print(len(str1))
count = count + len(str1)  # 남은 1개짜리 알파벳 개수 모두 더해주기

print(count)

