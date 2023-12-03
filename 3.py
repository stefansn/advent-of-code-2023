f = open("3.txt", "r")

sum = 0
EXCLUDED_SYMBOLS = [".", "\n"]
matrix = [[el for el in line] for line in f]

for row_index, row in enumerate(matrix):
    number = None
    number_indexes = []
    for col_index, element in enumerate(row):
        if element.isdigit():
            if number is None:
                number = 0
            number = number * 10 + int(element)
            number_indexes.append((row_index, col_index))
        else:
            if not number is None:
                stop_searching = False
                for position in number_indexes:
                    if stop_searching:
                        break

                    x = position[0]
                    y = position[1]

                    iterations = [
                        (x, y - 1),
                        (x - 1, y - 1),
                        (x - 1, y),
                        (x - 1, y + 1),
                        (x, y + 1),
                        (x + 1, y + 1),
                        (x + 1, y),
                        (x + 1, y - 1),
                    ]

                    for iteration in iterations:
                        try:
                            val = matrix[iteration[0]][iteration[1]]
                            if not val.isdigit() and not val in EXCLUDED_SYMBOLS:
                                sum += number
                                stop_searching = True
                                break
                        except:
                            pass
            number = None
            number_indexes = []

print(sum)
