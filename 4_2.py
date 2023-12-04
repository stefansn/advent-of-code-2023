import re

f = open("4.txt", "r")

card_ocurrences = {}
for line in f:
    card_id = int(re.findall(r"\d+", line[: line.index(":")])[0])

    if not card_id in card_ocurrences:
        card_ocurrences[card_id] = 1
    else:
        card_ocurrences[card_id] += 1

    just_numbers = line[8:].split("|")
    first_group = re.findall(r"\d+", just_numbers[0])
    second_group = re.findall(r"\d+", just_numbers[1])
    common = [first for first in first_group if first in second_group]

    for i in range(len(common)):
        next_card_id = card_id + i + 1
        if not next_card_id in card_ocurrences:
            card_ocurrences[next_card_id] = card_ocurrences[card_id]
        else:
            card_ocurrences[next_card_id] += card_ocurrences[card_id]

print(sum(card_ocurrences.values()))
