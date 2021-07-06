T = int(input())
i = 0

for i in range(T):
    i += 1
    H, W, N = map(int, input().split())

    if N < H:
        floor = N
        room_num = 1
        print(str(floor) + '0' + str(room_num))

    else:
        if N % H == 0:
            floor = H
            room_num = N // H
        else:
            floor = N % H
            room_num = N // H + 1

        if len(str(room_num)) == 1:
            print(str(floor) + '0' + str(room_num))
        else:
            print(str(floor) + str(room_num))
