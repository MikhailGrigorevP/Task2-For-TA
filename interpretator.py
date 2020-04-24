from __future__ import annotations
import sys
from typing import List


class Element:
    def __init__(self, elem_type, elem_value):
        self.type = elem_type
        self.value = elem_value

    def __repr__(self):
        return f'{self.type}, {self.value}'


class Error:
    def __init__(self, err_type, node):
        self.type = err_type
        self.node = node

    def __repr__(self):
        sys.stderr.write(f'Error {self.type}: ')
        if self.type == 1:
            sys.stderr.write(f'no input point\n')
            return
        elif self.type == 2:
            sys.stderr.write(f'variable "{ self.node.value}" at '
                             f'{ self.node.lineno}:{ self.node.lexpos} is already declared\n')
        elif self.type == 3:
            sys.stderr.write(f'variable "{ self.node.value}" at '
                             f'{ self.node.lineno}:{ self.node.lexpos} is used before declaration\n')
        elif self.type == 4:
            sys.stderr.write(f'index error "{ self.node.value}" at '
                             f'{ self.node.lineno}:{ self.node.lexpos}\n')
        elif self.type == 5:
            sys.stderr.write(f'Unknown function call "{ self.node.value}" at '
                             f'{ self.node.lineno}:{ self.node.lexpos}\n')


class Interpreter:
    error = {
        'no_application': 1,
        'value_redeclare': 2,
        'undeclared_value': 3,
        'index_error': 4,
        'func_call_error': 5
    }

    def __init__(self, parser):
        self.parser = parser

