N = int(input())
count_groupWord = 0

for i in range(N):
    word = str(input())
    lst = [k for k in str(word)]  # 문자열을 리스트 형식으로 바꾸기
    tmp_lst = lst.copy()
    j = 0
    while j < len(lst) - 1:  # hㅁaㅁppㅁy 형식으로 새로운 문자가 나올 때마다 공백 삽입
        if lst[j] != lst[j+1]:
            lst.insert(j+1, " ")
            j += 2
        else:
            j += 1

    count_blank = lst.count(" ")  # 공백의 개수 세기
    count_lst = len(set(tmp_lst))  # 원 리스트에서 중복 제거 (등장하는 알파벳의 개수)

    if count_blank + 1 == count_lst:
        count_groupWord += 1  # 공백 개수 + 1 == 원 리스트에서 등장하는 알파벳 개수라면 그룹 단어

print(count_groupWord)


