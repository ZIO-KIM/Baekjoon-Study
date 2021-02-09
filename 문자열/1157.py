# import numpy as np
str1 = str(input())
lst = [0 for _ in range(26)]  # 알파벳의 개수를 담을 리스트

for i in range(len(str1)):
    if 'A' <= str1[i] <= 'Z':  # 대문자라면
        lst[ord(str1[i]) - 65] += 1
    else:  # 소문자라면
        lst[ord(str1[i]) - 97] += 1

copy_lst = lst.copy()  # 가장 많이 사용된 알파벳이 존재할때 사용할 리스트 copy
lst.sort()  # 같은 값 존재할때 사용할 리스트 정렬
sort_index = sorted(range(len(copy_lst)), key = lambda k: copy_lst[k])  # numpy 사용이 불가능해서 요렇게

'''
# numpy 사용이 가능하다면?

vals = np.array(copy_lst)
sort_index = np.argsort(vals) # 인덱스들을 들어있는 value들의 오름차순으로 정렬
'''

if lst[25] == lst[24]:
    print("?")

else:
    print(chr(sort_index[25] + 65))
