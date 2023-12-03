f = open("3.txt", "r")

sum = 0
SYMBOL = "*"
matrix = [[el for el in line] for line in f]
symbol_positions = {}

for row_index, row in enumerate(matrix):
    for col_index, element in enumerate(row):
        if element == SYMBOL:
            symbol_positions[f"{row_index}_{col_index}"] = []

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
                            key = f"{iteration[0]}_{iteration[1]}"
                            if symbol_positions[key] or symbol_positions[key] == []:
                                symbol_positions[key].append((f"{x}_{y}", number))
                                stop_searching = True
                                break
                        except:
                            pass
            number = None
            number_indexes = []

for key in symbol_positions.keys():
    product = 1
    if len(symbol_positions[key]) == 2:
        for val in symbol_positions[key]:
            product *= val[1]
        sum += product

print(sum)
