str1 = str(input())
count = 0

if str1 != " ":  # 공백 하나만 들어오는 경우는 제외해줌 (count = 0) 
    for i in range(len(str1)):  # 첫번째로 알파벳이 나오는 인덱스를
        if ("A" <= str1[i] <= "Z") or ("a" <= str1[i] <= "z"):
            start_idx = i  # 시작 인덱스로 정해줌
            break

    for i in range(len(str1) - 1, -1, -1):  # 뒤에서부터 첫번째로 알파벳이 나오는 인덱스를
        if ('A' <= str1[i] <= 'Z') or ('a' <= str1[i] <= 'z'):
            end_idx = i  # 끝 인덱스로 정해줌
            break

    if start_idx == end_idx:  # 두개가 같다면 한글자만 들어왔다는 뜻 ex. a
        count = 1

    else:  # 다를 경우 한개 이상의 글자가 들어옴
        for i in range(start_idx, end_idx, 1):
            if str1[i] == " ":
                count += 1  # 시작 인덱스 - 끝 인덱스 돌면서 공백 갯수 세기
        count += 1  # 공백만 셌으므로 단어는 1개 더 많음

print(count)  
