from io import open
from interpreter import Interpreter

instructions = list()
with open("puzzleInput_test.txt", "r") as fp:
    instructions = [inst.rstrip() for inst in fp]

interpreter = Interpreter(0, 0, instructions)
instractions_executed = [0]
for instruction in instructions:
    interpreter.perform_instruction()
    if interpreter.get_instruction_pointer() in instractions_executed:
        break
    instractions_executed.append(interpreter.get_instruction_pointer())

print(f"Accumulator: {interpreter.get_accumulator()}")
