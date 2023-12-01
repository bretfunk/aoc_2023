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

def letters():
    return {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            }

def create_index(str):
    indexes = []
    # add all letter and number indexes to minimize edge cases
    for key in letters():
        for index in find_all_indexes(str, key):
            indexes.append((key, index))

    for i in range(len(str)):
        if str[i].isnumeric():
            indexes.append((str[i], i))

    # sort by index
    indexes.sort(key=lambda tup: tup[1])

    # only first and last index
    return [indexes[0], indexes[-1]]

def index_to_number(index):
    new_num = ""
    for key, _index in index:
        if key in letters():
            new_num += letters()[key]
        else:
            new_num += key

    return int(new_num)

def find_all_indexes(input_string, word):
    start = 0
    indexes = []
    while start < len(input_string):
        index = input_string.find(word, start)
        if index == -1:
            break
        indexes.append(index)
  # move to next possible start position
        start = index + 1
    return indexes

def second_problem():
    file = "puzzle_input_1.txt" if True else "example_2.txt"
    data = import_data(file)
    total = 0

    for line in data.splitlines():
        print("line: " + line)
        index = create_index(line)
        print("create_index: ", index)
        result = index_to_number(index)
        print("no letters: ", result)
        total += result

    return total;

print(second_problem())

