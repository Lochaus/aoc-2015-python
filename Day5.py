def check_triple_vowel(word):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_counter = 0
    for letter in word:
        if letter in vowels:
            vowel_counter += 1
    if vowel_counter > 2:
        return True
    return False

def check_double_letter(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False

def check_banned_strings(word):
    banned_strings = ["ab", "cd", "pq", "xy"]
    for banned_string in banned_strings:
        if banned_string in word:
            return False
    return True


def Part1(input_lines):
    nice_string_counter = 0
    for line in input_lines:
        line = line.replace("\n", "")
        if check_triple_vowel(line) and check_double_letter(line) and check_banned_strings(line):
            print(nice_string_counter, line)
            nice_string_counter += 1
    return nice_string_counter


def Part2(input_lines):
    return 0


# Open input data as input file
input_file = open("./Day5.txt", "r")

# Add each line of the input to an array
input_lines = []
for each_line in input_file:
    input_lines.append(each_line)

input_file.close()

# Call functions to get solutions
print(Part1(input_lines))
print(Part2(input_lines))