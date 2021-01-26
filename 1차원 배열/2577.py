A = int(input())
B = int(input())
C = int(input())
num_list = [0 for _ in range(12)]
used_num = [0 for _ in range(10)]
i = 0

mul = A * B * C

while mul > 0:
    num_list[i] = mul % 10
    mul //= 10
    i += 1
index = i

for i in range(0, index):
    if num_list[i] == 0:
        used_num[0] += 1
    if num_list[i] == 1:
        used_num[1] += 1
    if num_list[i] == 2:
        used_num[2] += 1
    if num_list[i] == 3:
        used_num[3] += 1
    if num_list[i] == 4:
        used_num[4] += 1
    if num_list[i] == 5:
        used_num[5] += 1
    if num_list[i] == 6:
        used_num[6] += 1
    if num_list[i] == 7:
        used_num[7] += 1
    if num_list[i] == 8:
        used_num[8] += 1
    if num_list[i] == 9:
        used_num[9] += 1

for i in range(0, 10):
    print(used_num[i])







