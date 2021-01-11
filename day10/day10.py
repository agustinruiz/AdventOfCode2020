from io import open

adapters_joltage = list()
with open("puzzleInput.txt", "r") as fp:
    adapters_joltage = [int(joltage) for joltage in fp]

# add charging outlet joltaje
adapters_joltage.append(0)
adapters_joltage.sort()
# add device's built-in adapter
adapters_joltage.append(adapters_joltage[len(adapters_joltage) - 1]+3)


def find_differences_list(adapters_joltage):
    differences = []
    for index, joltage in enumerate(adapters_joltage):
        if index == len(adapters_joltage) - 1:
            break
        differences.append(adapters_joltage[index+1]-joltage)
    return differences


differences = find_differences_list(adapters_joltage)

print(f"Count of 1 difference: {differences.count(1)}")
print(f"Count of 2 difference: {differences.count(2)}")
print(f"Count of 3 difference: {differences.count(3)}")

print(
    f"Multiplication of 1 and 3: {differences.count(1)*differences.count(3)}")
