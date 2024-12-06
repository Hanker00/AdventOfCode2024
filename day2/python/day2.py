def isNotSafeDiff(diff):
    return abs(diff) > 3 or abs(diff) < 1

def isSameSign(first, second):
    return (first * second) > 0

def checkLevelSafe(level):
    current_safe = True
    prev_diff = 0
    for i in range(len(level) - 1):
        first = level[i]
        second = level[i + 1]
        if(i == 0):
            prev_diff = first - second
            if(isNotSafeDiff(prev_diff)):
                current_safe = False
                break
        else:
            current_diff = first - second
            if(isNotSafeDiff(current_diff)):
                current_safe = False
                prev_diff = current_diff
                break
            elif(not isSameSign(prev_diff, current_diff)):
                prev_diff = current_diff
                current_safe = False
                break
    if(current_safe):
        return True
    else:
        False

with open("day2.txt") as f:
    lines = f.readlines()
    levels = []
    for i in lines:
        levels.append([int(x) for x in i.split()])
    total_safe = 0
    for level in levels:
        safe = False
        for i in range(len(level)):
            slice = level[:i] + level[i+1:]
            if checkLevelSafe(slice):
                safe = True
        if(safe):
            total_safe += 1
    print(total_safe)
"""
            if(current_safe == False):
                if(removed > 0):
                    break
                if(i == 1):
                    current_diff = level[i] - level[i + 1]
                    if(isNotSafeDiff(current_diff)):
                        current_safe = False
                        break
                else:
                    current_diff = level[i - 1] - level[i + 1]
                    if(isNotSafeDiff(current_diff)):
                        current_safe = False
                        break
                    elif(isSameSign(prev_diff, current_diff)):
                            current_safe = True
                            removed = 1
                            continue
                    else:
                        current_safe = True
                        removed = 1
                        prev_diff = current_diff
                        continue
"""   
