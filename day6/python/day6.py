def find_guy_pos_and_dir(matrix):
    dirs_dict = {
        "^": "UP",
        "v": "DOWN",
        "<": "LEFT",
        ">": "RIGHT"
    }
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            if(matrix[y][x] in dirs_dict):
                return y, x, dirs_dict[matrix[y][x]]

with open("day6.txt") as f:
    lines = f.read().splitlines()
    matrix = []
    for line in lines:
        matrix.append(line)
    start_y, start_x, start_dir = find_guy_pos_and_dir(matrix)
    found = False
    total_count_steps = 0
    x = start_x
    y = start_y
    visited_positions = set()
    visited_positions.add((y, x))
    while not found:
        match start_dir:
            case "UP":
                # Move up
                while y > 0 and matrix[y-1][x] != "#":
                    y -= 1
                    total_count_steps += 1
                    visited_positions.add((y, x))
                if matrix[y-1][x] == "#":
                    start_dir = "RIGHT"
                else:
                    found = True
                    visited_positions.add((y, x))
            case "DOWN":
                while y < len(matrix) - 2 and matrix[y+1][x] != "#":
                    y += 1
                    visited_positions.add((y, x))
                if matrix[y+1][x] == "#":
                    start_dir = "LEFT"
                else:
                    found = True
                    visited_positions.add((y, x))
            case "LEFT":
                while x > 0 and matrix[y][x-1] != "#":
                    x -= 1
                    visited_positions.add((y, x))
                if matrix[y][x-1] == "#":
                    start_dir = "UP"
                else:
                    found = True
                    visited_positions.add((y, x))
            case "RIGHT":
                while x < len(matrix[0]) - 2 and matrix[y][x+1] != "#":
                    x += 1
                    visited_positions.add((y, x))
                if matrix[y][x+1] == "#":
                    start_dir = "DOWN"
                else:
                    found = True
                    visited_positions.add((y, x))
    print(x, y)
    print(len(visited_positions))
    print(visited_positions)
    print(matrix)
