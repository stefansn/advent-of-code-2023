f = open("1.txt", "r")

sum = 0
for line in f:
    first = None
    second = None

    for char in line:
        if char.isdigit():
            if first is None:
                first = int(char)
            else:
                second = int(char)
    if second is None:
        sum += first * 10 + first
    else:
        sum += first * 10 + second


print(sum)

f.close()