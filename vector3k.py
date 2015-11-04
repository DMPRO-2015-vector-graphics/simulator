from mmu import MMU
from core import Core

class VECTOR3K:
    self.program = []
    self.scene = []
    self.fb = []

    def write_program(self, program):
        self.program = program

    def execute_instruction(self, instruction):
        raise NotImplementedError

    def execute_program(self):
        for instruction in program:
            execute_instruction(instruction)
