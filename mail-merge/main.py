# Read template letter
with open("./input/letters/starting_letter.txt") as f:
    template = f.readlines()

# Read names from files
with open("./input/names/invited_names.txt") as name_file:
    names = name_file.readlines()

# Create personalized letters
for name in names:
    cleaned_name = name.strip() # Remove whitespace/newline characters
    personalized_letter = "".join([line.replace("[name]", cleaned_name) for line in template])
    #save the letter with a proper filename
    with open(f"./output/ready_to_send/letter_for_{cleaned_name}.txt", mode="w") as output_file:
        output_file.write(personalized_letter)
