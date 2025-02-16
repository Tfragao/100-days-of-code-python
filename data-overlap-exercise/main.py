# Read numbers from files and store as list of integers

def read_numbers_from_file(filename):
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file]

file1_numbers = read_numbers_from_file("file1.txt")
file2_numbers = read_numbers_from_file("file2.txt")

# Find common numbers using list comprehension
result = [num for num in file1_numbers if num in file2_numbers]
print(result)