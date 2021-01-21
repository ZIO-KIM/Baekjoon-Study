hour, min = input().split()

hour = int(hour)
min = int(min)

if min >= 45:
    print(hour, min-45)
else:
    if hour == 0:
        print(23, min+15)
    elif hour == 1:
        print(0, min+15)
    else:
        print(hour-1, min+15)
