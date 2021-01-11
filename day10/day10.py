from io import open

adapters_joltage = list()
with open("puzzleInput_test.txt", "r") as fp:
    adapters_joltage = [int(joltage) for joltage in fp]

adapters_joltage.sort()


def find_differences_list(adapters_joltage):
    differences = []
    # El primer adaptavor va conectado a un jolt de 0 => la diferencia es el calor del 1er adaptador
    differences.append(adapters_joltage[0])
    for index, joltage in enumerate(adapters_joltage):
        if index == len(adapters_joltage) - 1:
            break
        differences.append(adapters_joltage[index+1]-joltage)
    # El adaptador interno de tu dispositivo tiene 3 joults de diferencia con el ultimo (el mas alto)
    differences.append(3)
    return differences


differences = find_differences_list(adapters_joltage)

print(f"Count of 1 difference: {differences.count(1)}")
print(f"Count of 2 difference: {differences.count(2)}")
print(f"Count of 3 difference: {differences.count(3)}")

print(
    f"Multiplication of 1 and 3: {differences.count(1)*differences.count(3)}")
