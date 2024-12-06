import numpy as np

def create_3x3(lines):
    matrices = []
    for i in range(len(lines) - 2):
        rows = lines[i:i+3]
        for j in range(len(lines[0]) - 2):
            matrix = []
            for row in rows:
                matrix.append(list(row[j:j+3]))
            matrices.append(matrix)
    return matrices

with open("day4.txt") as f:
    lines = f.read().splitlines()
    mini_matrices = create_3x3(lines)
    count = 0
    for matrix in mini_matrices:
        diagonal = ''.join(np.diag(matrix, 0))
        if 'MAS' in diagonal or 'SAM' in diagonal:
            flipped_matrix = [line[::-1] for line in matrix]
            diagonal = ''.join(np.diag(flipped_matrix, 0))
            if 'MAS' in diagonal or 'SAM' in diagonal:
                count += 1

    print(count)
    
