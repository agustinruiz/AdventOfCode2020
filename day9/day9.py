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
            return (index, int(number))


def find_contiguous_set(index, number, number_list):
    for j in range(index):
        contiguous_sum = 0
        sum_set = set()
        for list_num in number_list[j:index]:
            sum_set.add(int(list_num))
            contiguous_sum += int(list_num)
            if contiguous_sum == number:
                return sorted(sum_set, reverse=False)
            elif contiguous_sum > number:
                break


first_wrong = find_first_wrong(25, lines)
print(f"First number without the property: {first_wrong}")

contiguous_set = find_contiguous_set(first_wrong[0], first_wrong[1], lines)
print(f"First number without the property: {contiguous_set}")

print(f"Sum of contiguous set: {contiguous_set[0] + contiguous_set[-1]}")
