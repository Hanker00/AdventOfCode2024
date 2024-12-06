with open("day5.txt") as f:
    lines = f.read().split('\n\n')
    rules = lines[0]
    updates = lines[1]
    rules = rules.split("\n")
    updates = updates.split("\n")
    updates = [[int(num) for num in sublist.split(',')] for sublist in updates]

rules_dict = {}
for rule in rules:
    rule = rule.split("|")
    before = int(rule[0])
    after  = int(rule[1])
    if(before in rules_dict):
        rules_dict[before].append(after)
    if(before not in rules_dict):
        rules_dict[before] = [after]

isCorrect = True
count = 0
for update in updates:
    isCorrect = True
    for i in range(len(update)):
        j = i + 1
        if(isCorrect == False):
                break
        for j in range(i+ 1, len(update)):
            if update[j] in rules_dict:
                if update[i] in rules_dict[update[j]]:
                    isCorrect = False
                    break
             
    if(isCorrect):
        count += int(update[len(update) // 2])
print("part1: " + str(count))

# PART TWO
isCorrect = True
count2 = 0
for update in updates:
    isCorrect = True
    i = 0
    while i < len(update):
        j = i + 1
        should_update = True
        while j < len(update):
            if update[j] in rules_dict and update[i] in rules_dict[update[j]]:
                element_to_insert = update[j]
                update.insert(i, update[j])
                update.pop(j + 1)
                isCorrect = False
                j += 1
                should_update = False
            j += 1
        if(should_update):
            i += 1
    if(isCorrect == False):         
        count2 += int(update[len(update) // 2])

print("part2: " + str(count2))