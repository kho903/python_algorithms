num_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
value = 1
for i in range(3):
    value *= int(input())

while value != 0:
    num_list[int(value % 10)] += 1
    value = int(value / 10)

for i in range(len(num_list)):
    print(num_list[i])