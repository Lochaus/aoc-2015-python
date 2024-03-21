def Part1(input_lines):
    wrapping_paper = 0
    for each_line in input_lines:
        dimesnions = each_line.split("x")
        length, width, height = int(dimesnions[0]), int(dimesnions[1]), int(dimesnions[2])
        sides_dimensions = [length*width, width*height, length*height]
        smallest_side = min(sides_dimensions)
        wrapping_paper += 2*length*width + 2*width*height + 2*height*length + smallest_side
    return wrapping_paper

def Part2(input_lines):
    wrapping_paper = 0
    for each_line in input_lines:
        dimesnions = each_line.split("x")
        sides = [int(dimesnions[0]), int(dimesnions[1]), int(dimesnions[2])]
        bow_size = sides[0]*sides[1]*sides[2]
        sides.remove(max(sides))
        wrapping_paper += 2*sides[0] + 2*sides[1] + bow_size
    return wrapping_paper

# Open input data as input file
input_file = open("./Day2.txt", "r")

# Add each line of the input to an array
input_lines = []
for each_line in input_file:
    input_lines.append(each_line)

input_file.close()

# Call functions to get solutions
print(Part1(input_lines))
print(Part2(input_lines))