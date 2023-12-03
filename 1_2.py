import re


f = open("1.txt", "r")

valid_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

digits = list(valid_digits.keys())


def form_number(occurrences, number):
    if number.isdigit():
        number = int(number)
    else:
        number = occurrences[number]
    return number


sum = 0

for line in f:
    occurrences = {}

    for digit in digits:
        for m in re.finditer(digit, line):
            occurrences[m.start()] = digit

    for i, char in enumerate(line):
        if char.isdigit():
            occurrences[i] = char

    sorted_indexes = list(occurrences.keys())
    sorted_indexes.sort()

    first_number = form_number(valid_digits, occurrences[sorted_indexes[0]])
    second_number = form_number(
        valid_digits, occurrences[sorted_indexes[len(sorted_indexes) - 1]]
    )

    if len(sorted_indexes) == 1:
        sum += first_number * 10 + first_number
    else:
        sum += first_number * 10 + second_number

print(sum)

f.close()
