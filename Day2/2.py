
# Specify the path to your text file
file_path = 'Day2/input.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()

lines = file_contents.strip().split('\n')

"""
lines = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]
"""

red_tot = 0
blue_tot = 0
green_tot = 0
sum = 0
power_sum = 0

for line in lines:
    #Game 1: 1 red, 5 blue, 1 green; 16 blue, 3 red; 6 blue, 5 red; 4 red, 7 blue, 1 green. 
    #Split by colon to get [[Game 1] , [1 red, 5 blue, 1 green; 16 blue, 3 red; 6 blue, 5 red; 4 red, 7 blue, 1 green]]
    #split Game 1 to get Game ID = 1

    red_temp = 0
    blue_temp = 0
    green_temp = 0

    initial_split = line.split(":")
    game_split = initial_split[0].split()
    game_id = game_split[1]

    #split [1 red, 5 blue, 1 green; 16 blue, 3 red; 6 blue, 5 red; 4 red, 7 blue, 1 green] by ; 
    #to get [[1 red, 5 blue, 1 green],[16 blue, 3 red], [6 blue, 5 red],[4 red, 7 blue],[1 green]]

    games = initial_split[1].split(";")

    valid = True

    #split each item by comma eg [[1 red], [5 blue], [1 green]]
    for game in games:

        balls = game.split(",")

        for ball in balls:

            quant_col = ball.split()
            quantity = quant_col[0]

            if quant_col[1] == "red":
                red_tot += int(quantity)
                if int(quantity) > red_temp:
                    red_temp = int(quantity)
            elif quant_col[1] == "blue":
                blue_tot += int(quantity)
                if int(quantity) > blue_temp:
                    blue_temp = int(quantity)
            elif quant_col[1] == "green":
                if int(quantity) > green_temp:
                    green_temp = int(quantity)
                green_tot += int(quantity)

        if red_tot > 12 or blue_tot > 14 or green_tot > 13:
            valid = False
    
        red_tot = 0
        blue_tot = 0
        green_tot = 0

    power = red_temp * blue_temp * green_temp

    power_sum += power

    if valid:
        sum += int(game_id)
    


print(sum)
print(power_sum)
    