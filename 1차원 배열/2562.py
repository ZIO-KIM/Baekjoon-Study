a_list = []

for i in range(0, 9):
    a_list.append(int(input()))

max_num = a_list[0]
index = 0

for i in range(1, 9):
    if a_list[i] > max_num:
        max_num = a_list[i]
        index = i

print(max_num)
print(index + 1)
