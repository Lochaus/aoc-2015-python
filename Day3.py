def new_coordinates(instruction, x, y):
    if instruction == "^":
        y += 1
    elif instruction == "v":
        y -= 1
    elif instruction == ">":
        x += 1
    elif instruction == "<":
        x -= 1
    return x, y

def Part1(input_lines):
    x, y = 0, 0
    positions_visited = [[0, 0]]
    for each_character in input_lines[0]:
        x, y = new_coordinates(each_character, x, y)
        if [x, y] not in positions_visited:
            positions_visited.append([x, y])
    return len(positions_visited)

def Part2(input_lines):
    santa_x, santa_y, robot_x, robot_y = 0, 0, 0, 0
    positions_visited = [[0, 0]]
    turn_counter = 0
    for each_character in input_lines[0]:
        if turn_counter%2:
            santa_x, santa_y = new_coordinates(each_character, santa_x, santa_y)
            if [santa_x, santa_y] not in positions_visited:
                positions_visited.append([santa_x, santa_y])
        else:
            robot_x, robot_y = new_coordinates(each_character, robot_x, robot_y)
            if [robot_x, robot_y] not in positions_visited:
                positions_visited.append([robot_x, robot_y])
        turn_counter += 1
    return len(positions_visited)


# Open input data as input file
input_file = open("./Day3.txt", "r")

# Add each line of the input to an array
input_lines = []
for each_line in input_file:
    input_lines.append(each_line)

input_file.close()

# Call functions to get solutions
print(Part1(input_lines))
print(Part2(input_lines))