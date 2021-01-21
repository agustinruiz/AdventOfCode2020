from io import open

adapters_joltage = list()
with open("puzzleInput_test.txt", "r") as fp:
    adapters_joltage = [int(joltage) for joltage in fp]

# add charging outlet joltaje
adapters_joltage.append(0)
adapters_joltage.sort()
# add device's built-in adapter
adapters_joltage.append(adapters_joltage[len(adapters_joltage) - 1]+3)
print(adapters_joltage)


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


def find_differents_arrangements2(adapters_joltage):
    # lista que ira almacenando la cantidad de combinaciones que implica cada conector si se puede sacar o no,
    # inicializa con uno ya que la lista completa es una combinacion posible
    combinations_list = [1]
    # Comienzo a recorrer desde el primer elemento hasta el ultimo
    for index in range(1, len(adapters_joltage)):
        # Por defecto la cantidad de combinaciones que implica sacar ese elemento es cero
        combinaciones = 0
        # voy a analizar los tres elementos anteriores a ver si se pueden sacar
        for index2 in range(0 if index < 3 else index-3, index):
            # si la diferencia entre uno de los tres elementos anteriores y el actual es de tres la cantidad de combinaciones posibles se incrementa
            if adapters_joltage[index2] + 3 >= adapters_joltage[index]:
                # las combinaciones se incrementan sumando las combinaciones que agrega el anterior.
                # si hay un solo elemento que cumple el numero de combinaciones se mantiene
                # pero si hay mas de uno la combinaciones se suman
                combinaciones += combinations_list[index2]
        combinations_list.append(combinaciones)
        print(f"combinations_list: {combinations_list}")
    return combinations_list[-1]


print(
    f"Number of arrangements: {find_differents_arrangements2(adapters_joltage)}")
