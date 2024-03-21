import hashlib

def Part1(input_lines):
    data_input = input_lines[0]
    number_addition = 1
    while True:
        if hashlib.md5((data_input+str(number_addition)).encode()).hexdigest()[0:5] == "00000":
            return number_addition
        number_addition += 1

def Part2(input_lines):
    data_input = input_lines[0]
    number_addition = 1038736
    while True:
        if hashlib.md5((data_input+str(number_addition)).encode()).hexdigest()[0:6] == "000000":
            return number_addition
        number_addition += 1


# Open input data as input file
input_file = open("./Day4.txt", "r")

# Add each line of the input to an array
input_lines = []
for each_line in input_file:
    input_lines.append(each_line)

input_file.close()

# Call functions to get solutions
print(Part1(input_lines))
print(Part2(input_lines))