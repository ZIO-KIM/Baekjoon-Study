# 수정중  

N = int(input())
count = 0

for i in range(N):
    word = str(input())
    lst = [k for k in str(word)]  # 문자열을 리스트 형식으로 바꾸기
    j = 0
    while j < len(lst):
        while lst[j] == lst[j + 1]:
            j += 1
        lst.insert(j + 1, " ")

print(lst)

