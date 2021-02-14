number = str(input())
time = 0

for i in range(len(number)):
    if 'A' <= number[i] <= 'C':  # ABC는 2, 3초
        time += 3
    if 'D' <= number[i] <= 'F':  # DEF는 3, 4초
        time += 4
    if 'G' <= number[i] <= 'I':  # GHI는 4, 5초
        time += 5
    if 'J' <= number[i] <= 'L':  # JKL은 5, 6초
        time += 6
    if 'M' <= number[i] <= 'O':  # MNO는 6, 7초
        time += 7
    if 'P' <= number[i] <= 'S':  # PQRS는 7, 8초
        time += 8
    if 'T' <= number[i] <= 'V':  # TUV는 8초, 9초
        time += 9
    if 'W' <= number[i] <= 'Z':  # WXYZ는 9, 10초
        time += 10

print(time)

