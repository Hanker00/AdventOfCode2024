with open("day1.txt") as f:
    lines = f.readlines()
    total_cal_list = []
    current_total = 0
    left_list = []
    right_list = []
    for i in lines:
        both = i.split()
        left_list.append(both[0])
        right_list.append(both[1])
    total = 0
    right_dict = {}
    for right in right_list:
        if right in right_dict:
            right_dict[right] += 1
        else:
            right_dict[right] = 1
    for left in left_list:
        if left in right_dict:
            total += int(left) * right_dict[left]

    print(total)