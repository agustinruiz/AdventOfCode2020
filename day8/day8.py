from io import open
from interpreter import Interpreter

instructions = list()
with open("puzzleInput.txt", "r") as fp:
    instructions = [inst.rstrip() for inst in fp]


def perform_execution(interpreter):
    instractions_executed = [0]
    for _ in instructions:
        #        print(interpreter)
        if interpreter.perform_instruction():
            if interpreter.get_instruction_pointer() in instractions_executed:
                return False
            instractions_executed.append(interpreter.get_instruction_pointer())
        else:
            return True


interpreter = Interpreter(0, 0, instructions)
for index, _ in enumerate(instructions):
    if interpreter.change_instruction(index):
        #        print(instructions)
        # that change didnt work so returning to the previous value
        if not perform_execution(interpreter):
            interpreter.change_instruction(index)
            interpreter.reset_counters()
        else:
            break

print(f"Accumulator: {interpreter.get_accumulator()}")
