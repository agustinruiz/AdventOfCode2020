from io import open


def findTwoEntriesSum(numbers, summation):
    for index, number in enumerate(numbers):
        for number2 in numbers[index+1:]:
            if (number + number2) == summation:
                return number * number2


def findThreeEntriesSum(numbers, summation):
    list_len = len(numbers)
    for index in range(0, list_len):
        for index2 in range(index+1, list_len):
            for index3 in range(index2+1, list_len):
                if (numbers[index] + numbers[index2] + numbers[index3]) == summation:
                    return numbers[index] * numbers[index2] * numbers[index3]


with open("day1input.txt", "r") as fp:
    numbers = [int(line.rstrip()) for line in fp]

print(
    f"The multiplication of two entries that sum 2020 is: {findTwoEntriesSum(numbers,2020)}")

print(
    f"The multiplication of three entries that sum 2020 is: {findThreeEntriesSum(numbers,2020)}")
