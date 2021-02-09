str1 = str(input())
lst = [-1 for _ in range(26)]  # 알파벳 개수를 세는 리스트

for i in range(len(str1)):
    if lst[ord(str1[i]) - 97] == -1:  # 처음 들어갈 경우에만
        lst[ord(str1[i]) - 97] = i  # lst의 0, 1, 2번째 위치에 알파벳이 처음 등장한 index 넣기

for i in range(26):
    print(lst[i], end=' ')

