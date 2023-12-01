def calibrate(str):
    l = 0
    r = len(str) - 1
    left_num = None
    right_num = None

    while left_num == None:
        if str[l].isnumeric():
            left_num = str[l]
        else:
            l += 1

    while right_num == None:
        if str[r].isnumeric():
            right_num = str[r]
        else:
            r -= 1

    return int(left_num + right_num)

def import_data(file):
    with open(file, 'r') as file:
        return file.read()


def first_problem():
    file = "puzzle_input_1.txt" if True else "example_1.txt"
    data = import_data(file)
    total = 0

    for line in data.splitlines():
        total += calibrate(line)

    return total;




print(first_problem())

