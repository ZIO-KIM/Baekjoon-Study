# 수정중  

N = int(input())
count = 0

for i in range(N):
    word = str(input())
    lst = [k for k in str(word)]  # 문자열을 리스트 형식으로 바꾸기
    for j in range(len(word) - 1):
        if word[j] != word[j+1] and word[j] != " ":
            lst.insert(j + 1, " ")

print(lst)
