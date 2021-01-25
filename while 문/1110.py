N = int(input())
cycle = 0
new_num = (N % 10) * 10 + (((N // 10)+(N % 10)) % 10)

while new_num != N:
    new_num = (new_num % 10) * 10 + (((new_num // 10)+(new_num % 10)) % 10)
    cycle += 1

print(cycle + 1)

