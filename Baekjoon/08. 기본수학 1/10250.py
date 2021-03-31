T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    room_num = int(N / H) + 1
    room_floor = N % H
    if room_floor == 0:
        room_floor = H
        room_num -= 1
    print(room_floor * 100 + room_num)
