class Interpreter:
    def _perform_acc(self, argument):
        if argument[0] == '+':
            self.accumulator += int(argument[1:])
        if argument[0] == '-':
            self.accumulator -= int(argument[1:])
        self.instruction_pointer += 1

    def _perform_jmp(self, argument):
        if argument[0] == '+':
            self.instruction_pointer += int(argument[1:])
        if argument[0] == '-':
            self.instruction_pointer -= int(argument[1:])

    def _perform_nop(self, argument):
        self.instruction_pointer += 1

    _operations_dict = {
        'acc': _perform_acc,
        'jmp': _perform_jmp,
        'nop': _perform_nop
    }

    # Contructor
    def __init__(self, accumulator, instruction_pointer, instruction_set):
        self.accumulator = accumulator
        self.instruction_pointer = instruction_pointer
        self.instruction_set = instruction_set

    def __str__(self):
        return f"Acumulator: {self.accumulator}, Instruction pointer: {self.instruction_pointer}"

    def perform_instruction(self):
        instruction = self.instruction_set[self.instruction_pointer]
        self._operations_dict[instruction[:3]](self, instruction.split(" ")[1])

    def get_accumulator(self):
        return self.accumulator

    def get_instruction_pointer(self):
        return self.instruction_pointer
