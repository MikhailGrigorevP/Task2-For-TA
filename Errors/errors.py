import sys


# Error handler
class Error_handler:
    def __init__(self, err_type, node=None):
        self.type = err_type
        self.node = node

    def __repr__(self):
        sys.stderr.write(f'Error {self.type}: ')
        if self.type == 1:
            sys.stderr.write(f'no input point\n')
            return
        elif self.type == 2:
            sys.stderr.write(f'variable "{self.node.value}" at '
                             f'{self.node.lineno}:{self.node.lexpos} is already declared\n')
        elif self.type == 3:
            sys.stderr.write(f'variable "{self.node.value}" at '
                             f'{self.node.lineno}:{self.node.lexpos} is used before declaration\n')
        elif self.type == 4:
            sys.stderr.write(f'index error "{self.node.value}" at '
                             f'{self.node.lineno}:{self.node.lexpos}\n')
        elif self.type == 5:
            sys.stderr.write(f'Unknown function call "{self.node.value}" at '
                             f'{self.node.lineno}:{self.node.lexpos}\n')
        elif self.type == 6:
            sys.stderr.write(f'failed to cast variable "{self.node.value}" at '
                             f'{self.node.lineno}:{self.node.lexpos}\n')
        elif self.type == 7:
            sys.stderr.write(f'incompatible value and type: "{self.node.value}" at'
                             f' {self.node.lineno}:{self.node.lexpos}\n')


class InterpreterNameError(Exception):
    pass


class InterpreterRedeclarationError(Exception):
    pass


class InterpreterConverseError(Exception):
    pass


class InterpreterValueError(Exception):
    pass