import re

f = open("2.txt", "r")

balls_pattern = re.compile(r"^Game (\d+): (.+)$")

blue_pattern = re.compile(r"(\d+) blue")
red_pattern = re.compile(r"(\d+) red")
green_pattern = re.compile(r"(\d+) green")

sum = 0
for line in f:
    balls_match = balls_pattern.match(line)
    balls_text = balls_match.group(2)

    subsets = balls_text.split(";")

    blue_max = 1
    red_max = 1
    green_max = 1

    GAME_OK = True
    for subset in subsets:
        blue_match = blue_pattern.search(subset)
        red_match = red_pattern.search(subset)
        green_match = green_pattern.search(subset)

        if blue_match:
            val = int(blue_match.group(1))

            if val > blue_max:
                blue_max = val

        if red_match:
            val = int(red_match.group(1))

            if val > red_max:
                red_max = val

        if green_match:
            val = int(green_match.group(1))

            if val > green_max:
                green_max = val

    sum += blue_max * red_max * green_max

print(sum)
f.close()
