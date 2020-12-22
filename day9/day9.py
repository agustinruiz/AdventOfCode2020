from io import open

lines = list()
with open("puzzleInput.txt", "r") as fp:
    lines = [line for line in fp]


def is_sum_of(number, number_list):
    for i in range(len(number_list)):
        for j in range(i + 1, len(number_list)):
            if int(number) == (int(number_list[i]) + int(number_list[j])):
                return True
    return False


def find_first_wrong(preamble, number_list):
    for index, number in enumerate(number_list[preamble:]):
        if not is_sum_of(number, number_list[index:index+preamble]):
            return number


print(f"First number without the property: {find_first_wrong(25,lines)}")
