# Specify the path to your text file
file_path = 'Day3/input.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()

lines = list(file_contents.strip().split())

print(lines)
