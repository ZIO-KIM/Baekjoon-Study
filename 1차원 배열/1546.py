score = []
sum = 0

N = int(input())

score = list(map(int, input().split()))

score.sort()
max_score = score[N - 1]

for i in range(0, N):
    score[i] = score[i] / max_score * 100
    sum += score[i]

mean = sum / N
print(mean)


