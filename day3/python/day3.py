import re

with open("day3.txt") as f:
    text = f.read()
    pattern = r"(don\'t|do)|mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, text)
    should_do_calculation = True
    result = 0
    for match in matches:
        command, num1, num2 = match
        if command:
            print(command)
            if command == "do":
                should_do_calculation = True
            else:
                should_do_calculation = False
        if(should_do_calculation and num1 and num2):
            result += int(num1) * int(num2)
print(result)