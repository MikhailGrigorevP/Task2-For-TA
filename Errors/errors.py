import sys
import Tree.syntaxTree


# Error handler
class Error_handler:
    def __init__(self):
        self.type = None
        self.node = None

    def call(self, err_type, node=None):
        self.type = err_type
        self.node = node
        sys.stderr.write(f'Error {self.type}: ')
        if self.type == 1:
            sys.stderr.write(f'no input point\n')
            return
        elif self.type == 2:
            if node.type == 'assignment':
                sys.stderr.write(f'variable "{self.node.child[0].value}" at '
                                 f'{self.node.child[0].lineno}:{self.node.child[0].lexpos} is already declared\n')
            else:
                sys.stderr.write(f'variable "{self.node.value}" at '
                                 f'{self.node.lineno}:{self.node.lexpos} is already declared\n')
        elif self.type == 3:
            if node.type == 'assignment':
                sys.stderr.write(f'variable "{self.node.child[0].value}" at '
                                 f'{self.node.child[0].lineno}:{self.node.child[0].lexpos} is used before declaration\n')
            else:
                sys.stderr.write(f'variable "{self.node.value}" at '
                                 f'{self.node.lineno}:{self.node.lexpos} is used before declaration\n')
        elif self.type == 4:
            if node.type == 'assignment':
                sys.stderr.write(f'index error "{self.node.child[0].value}" at '
                             f'{self.node.child[0].lineno}:{self.node.child[0].lexpos}\n')
            else:
                sys.stderr.write(f'index error "{self.node.value}" at '
                             f'{self.node.lineno}:{self.node.lexpos}\n')
        elif self.type == 5:
            sys.stderr.write(f'Unknown function call "{self.node.value}" at '
                             f'{self.node.lineno}:{self.node.lexpos}\n')
        elif self.type == 6:
            if node.type == 'assignment':
                sys.stderr.write(f'wrong type variable "{self.node.child[0].value}" at '
                                 f'{self.node.child[0].lineno}:{self.node.child[0].lexpos}\n')
            else:
                sys.stderr.write(f'failed to converse variable "{self.node.value}" at '
                                 f'{self.node.lineno}:{self.node.lexpos}\n')
        elif self.type == 7:
            if node.type == 'assignment':
                sys.stderr.write(f'incompatible value and type: "{self.node.child[0].value}" at'
                             f' {self.node.child[0].lineno}:{self.node.child[0].lexpos}\n')
            else:
                sys.stderr.write(f'incompatible value and type: "{self.node.value}" at'
                             f' {self.node.lineno}:{self.node.lexpos}\n')


class InterpreterNameError(Exception):
    pass


class InterpreterIndexError(Exception):
    pass


class InterpreterRedeclarationError(Exception):
    pass


class InterpreterConverseError(Exception):
    pass


class InterpreterValueError(Exception):
    pass
