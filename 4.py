import re

f = open("4.txt", "r")

sum = 0
for line in f:
    just_numbers = line[8:].split("|")
    first_group = re.findall(r"\d+", just_numbers[0])
    second_group = re.findall(r"\d+", just_numbers[1])
    common = [first for first in first_group if first in second_group]

    if len(common) > 0:
        score = pow(2, len(common) - 1)
        sum += score

print(sum)
