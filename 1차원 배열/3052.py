nums = []
remainder = []
tmp = 0
diff_r = 0

for i in range(0, 10):
    nums.append(int(input()))
    remainder.append(nums[i] % 42)

for i in range(0, 10):
    for j in range(i+1, 10):
        if remainder[i] == remainder[j]:
            tmp += 1
    if tmp == 0:
        diff_r += 1
    tmp = 0

print(diff_r)
