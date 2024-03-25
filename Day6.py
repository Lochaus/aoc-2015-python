import numpy as np

def toggle_lights(instruction, grid_range, grid):
    grid_range = grid_range.split("through")
    start_x = (grid_range[0].split(","))[0]
    start_y = (grid_range[0].split(","))[1]
    end_x = (grid_range[1].split(","))[0]
    end_y = (grid_range[1].split(","))[1]
    for y in range(int(start_y), int(end_y)+1):
        for x in range(int(start_x), int(end_x)+1):
            if instruction == "on":
                grid[y][x] = 1
            elif instruction == "off":
                grid[y][x] = 0
            else:
                grid[y][x] = abs(grid[y][x] - 1)
    return grid

def change_light_brightness(instruction, grid_range, grid):
    grid_range = grid_range.split("through")
    start_x = (grid_range[0].split(","))[0]
    start_y = (grid_range[0].split(","))[1]
    end_x = (grid_range[1].split(","))[0]
    end_y = (grid_range[1].split(","))[1]
    for y in range(int(start_y), int(end_y)+1):
        for x in range(int(start_x), int(end_x)+1):
            if instruction == "on":
                grid[y][x] += 1
            elif instruction == "off":
                grid[y][x] -=1
                if grid[y][x] < 0:
                    grid[y][x] = 0
            else:
                grid[y][x] += 2
    return grid

def Part1(input_lines):
    grid = np.zeros((1000, 1000))
    lights_on_counter = 0
    for line in input_lines:
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        if line[0:6] == "toggle":
            grid = toggle_lights("toggle", line[6:], grid) 
        elif line[0:7] == "turnoff":
            grid = toggle_lights("off", line[7:], grid) 
        elif line[0:6] == "turnon":
            grid = toggle_lights("on", line[6:], grid)
    for y in range(1000):
        for x in range(1000):
            if grid[y][x] == 1:
                lights_on_counter += 1
    return lights_on_counter



def Part2(input_lines):
    grid = np.zeros((1000, 1000))
    total_brightness = 0
    for line in input_lines:
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        if line[0:6] == "toggle":
            grid = change_light_brightness("toggle", line[6:], grid) 
        elif line[0:7] == "turnoff":
            grid = change_light_brightness("off", line[7:], grid) 
        elif line[0:6] == "turnon":
            grid = change_light_brightness("on", line[6:], grid)
    for y in range(1000):
        for x in range(1000):
            total_brightness += grid[y][x]
    return int(total_brightness)


# Open input data as input file
input_file = open("./Day6.txt", "r")

# Add each line of the input to an array
input_lines = []
for each_line in input_file:
    input_lines.append(each_line)

input_file.close()

# Call functions to get solutions
print(Part1(input_lines))
print(Part2(input_lines))