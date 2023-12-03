# Specify the path to your text file
file_path = 'Day1/input.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()

lines = file_contents.strip().split('\n')

sum = 0
comb1 = 0
comb2 = 0
found1 = False
found2 = False

"""
lines = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]
"""

for line in lines:
    
    line = (
        line.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )

    splitlines = list(line)  
    x = 0
    y = len(splitlines) - 1

    while x < y or y > x:
        xchar = splitlines[x]
        ychar = splitlines[y]
        if splitlines[x].isdigit() and found1 == False:
            comb1 = splitlines[x]
            found1 = True
        else:
            if  not found1:

                x += 1
        
        if splitlines[y].isdigit() and found2 == False:
            comb2 = splitlines[y]
            found2 = True
        else:
            if not found2:
                y -= 1

        if found1 and found2:
            break
    
    if len(splitlines)%2 != 0 and not found1 and not found2:
            xchar = splitlines[x]
            if splitlines[x].isdigit():
                comb1 = splitlines[x]
                found1 = True

    if not found1:
        comb1 = ''

    if not found2:
        comb2 = ''

    if not found1 and not found2:
        number = 0
    elif not found1 and found2:
        number = int(str(comb2) + str(comb2))
    elif found1 and not found2:
        number = int(str(comb1) + str(comb1))
    else:
        number = int(str(comb1) + str(comb2))
    
    comb1 = 0 
    comb2= 0
    found1 = False
    found2 = False

    sum += number

print(sum)