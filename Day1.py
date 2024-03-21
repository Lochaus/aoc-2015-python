def Part1(input_lines):
    floor_counter = 0
    for each_character in input_lines[0]:
        if each_character == "(":
            floor_counter += 1
        elif each_character == ")":
            floor_counter -= 1
        else:
            return ("Invalid Input")
    return floor_counter

def Part2(input_lines):
    instruction_counter = 0
    floor_counter = 0
    for each_character in input_lines[0]:
        instruction_counter += 1
        if each_character == "(":
            floor_counter += 1
        elif each_character == ")":
            floor_counter -= 1
        else:
            return ("Invalid Input")
        if floor_counter == -1:
            return instruction_counter
    return ("Invalid Input")

# Open input data as input file
input_file = open("./Day1.txt", "r")

# Add each line of the input to an array
input_lines = []
for each_line in input_file:
    input_lines.append(each_line)

input_file.close()

# Call functions to get solutions
print(Part1(input_lines))
print(Part2(input_lines))