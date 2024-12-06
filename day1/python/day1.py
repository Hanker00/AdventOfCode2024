with open("day1.txt") as file:
    lines = file.readlines()
left_list = []
right_list = []
total = 0
for i in lines:
    both = i.split()
    left_list.append(both[0])
    right_list.append(both[1])
    left_list.sort()
    right_list.sort()
for left, right in zip(left_list, right_list):
    total += abs(int(left)-int(right))
print(total)