import re

f = open("2.txt", "r")

RED = 12
GREEN = 13
BLUE = 14


game_pattern = re.compile(r"^Game (\d+)")
balls_pattern = re.compile(r"^Game (\d+): (.+)$")

blue_pattern = re.compile(r"(\d+) blue")
red_pattern = re.compile(r"(\d+) red")
green_pattern = re.compile(r"(\d+) green")

game_id_sum = 0
for line in f:
    game_match = game_pattern.match(line)
    game_id = game_match.group(1)

    balls_match = balls_pattern.match(line)
    balls_text = balls_match.group(2)

    subsets = balls_text.split(";")

    GAME_OK = True
    for subset in subsets:
        blue_match = blue_pattern.search(subset)
        red_match = red_pattern.search(subset)
        green_match = green_pattern.search(subset)

        if blue_match and int(blue_match.group(1)) > BLUE:
            GAME_OK = False

        if red_match and int(red_match.group(1)) > RED:
            GAME_OK = False

        if green_match and int(green_match.group(1)) > GREEN:
            GAME_OK = False

    if GAME_OK:
        game_id_sum += int(game_id)

print(game_id_sum)
f.close()
