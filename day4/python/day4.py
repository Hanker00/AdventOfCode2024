import numpy as np

def check_horizontally_and_vertically(lines):
    count = 0
    count += check_normal_and_reverse(lines)
    lines = np.array([list(line) for line in lines])
    print(lines)
    transposed = np.transpose(lines)
    count += check_normal_and_reverse([''.join(row) for row in transposed])
    
    return count

def check_normal_and_reverse(lines):
    count = 0
    target = "XMAS"
    target_backwards = "SAMX"
    for line in lines:
        count += line.count(target)
        count += line.count(target_backwards)
    return count


with open("day4.txt") as f:
    lines = f.read().splitlines()
    count = 0
    count += check_horizontally_and_vertically(lines)
    target = "XMAS"
    target_backwards = "SAMX"
    for i in range(len(lines) - 3):
        new_lines = lines[i:i+4]

        matrix = np.array([list(line) for line in new_lines])
        for k in range(-matrix.shape[0]+1, matrix.shape[1]):
            diagonal = np.diag(matrix, k)
            check = ''.join(diagonal)
            if(len(check) >= 4):
                count += check.count(target)
                count += check.count(target_backwards)
    flipped_lines = [line[::-1] for line in lines]
    for i in range(len(flipped_lines) - 3):
        new_lines = flipped_lines[i:i+4]
        clean_lines = [line.strip() for line in new_lines]

        matrix = np.array([list(line) for line in clean_lines])
        for k in range(-matrix.shape[0]+1, matrix.shape[1]):
            diagonal = np.diag(matrix, k)
            check = ''.join(diagonal)
            if(len(check) >= 4):
                count += check.count(target)
                count += check.count(target_backwards)
    print(count)


    