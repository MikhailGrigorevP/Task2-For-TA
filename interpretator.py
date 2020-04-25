import sys
from typing import List
from Parser.parser import parser


# Item of symbol table
class Variable:
    def __init__(self, var_type, var_value):
        self.type = var_type
        self.value = var_value

    def __repr__(self):
        return f'{self.type}, {self.value}'


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


# Conversion of types
class TypeConversion:
    def __init__(self):
        pass

    def converse(self, _type, var):
        if _type == var.type:
            return var
        if _type == 'boolean':
            if var.type == 'integer':
                return self.int_to_bool(var)
            if var.type == 'string':
                return self.int_to_string(var)
        if _type == 'integer':
            if var.type == 'boolean':
                return self.bool_to_int(var)
            if var.type == 'string':
                return self.bool_to_string(var)
        if _type == 'vector':
            if var.type == 'string':
                return self.vector_to_string(var)
            else:
                raise InterpreterConverseError
        else:
            raise ValueError('wrong type')

    @staticmethod
    def bool_to_int(value):
        if value.value == 'true':
            return Variable('integer', 1)
        elif value.value == 'false':
            return Variable('integer', 0)
        elif value.value == 'undefined':
            return Variable('integer', 'undefined')
        raise InterpreterValueError

    @staticmethod
    def int_to_bool(value):
        if value.value == '0':
            return Variable('boolean', 'false')
        elif isinstance(value.value, int):
            return Variable('boolean', 'true')
        raise InterpreterValueError

    @staticmethod
    def int_to_string(value):
        return Variable('string', str(value))

    @staticmethod
    def bool_to_string(value):
        return Variable('string', str(value))

    @staticmethod
    def vector_to_string(value):
        string = ''
        for char in value:
            string.join(char)
        return Variable('string', value)



# Cell of a map

class Cell:
    def __init__(self, x, y, _type, _solidity):
        self.x = x
        self.y = y
        self.type = _type
        self.solidity = _solidity

    def __repr__(self):
        return f'{self.x} {self.y} : {self.type}'


class CellType:
    type = 'cell'
    solidity = 0

    def __init__(self):
        pass

    def __repr__(self):
        return self.type


class Empty(CellType):
    type = 'EMPTY'
    solidity = 0


class Concrete(CellType):
    type = 'CONCRETE'
    solidity = 4


class Wood(CellType):
    type = 'WOOD'
    solidity = 3


class Plastic(CellType):
    type = 'PLASTIC'
    solidity = 2


class Glass(CellType):
    type = 'GLASS'
    solidity = 1


class Steel(CellType):
    type = 'STEEL'
    solidity = 5


class Exit(CellType):
    type = 'EXIT'
    solidity = 0


class Interpreter:

    def __init__(self, par, _converse=TypeConversion()):
        self.parser = par
        self.converse = _converse
        self.map = None
        self.program = None
        self.sym_table = None
        self.tree = None
        self.funcs = None
        self.error_types = {
            'no_application': 1,
            'value_redeclare': 2,
            'undeclared_value': 3,
            'index_error': 4,
            'func_call_error': 5,
            'cast': 6,
            'value': 7
        }

    def interpreter(self, map_description, program):
        self.map = map_description
        self.program = program
        self.sym_table = dict()
        # noinspection PyBroadException
        try:
            self.tree, self.funcs = self.parser.parse(program)
        except Exception:
            if 'application' not in self.funcs.keys():
                print(Error_handler(self.error_types['no_application']))
                return
        self.interpreter_tree(self.tree)
        self.interpreter_node(self.funcs['application'])

    def interpreter_tree(self, tree):
        pass

    def interpreter_node(self, node):
        # nothing
        if node is None:
            return
        # comment
        if node.type == 'comment':
            return
        # program
        if node.type == 'program':
            self.interpreter_node(node.child)
        # program - statements
        elif node.type == 'statements':
            for ch in node.child:
                self.interpreter_node(ch)

        # STATEMENTS BLOCK

        # statements -> declaration
        elif node.type == 'declaration':
            declaration_type = node.value.value
            declaration_child = node.child.child
            # if declare a group of variables
            if isinstance(declaration_child, list):
                for ch in declaration_child:
                    self.declare_variable(ch, declaration_type)
            # if declare a variables
            else:
                self.declare_variable(declaration_child, declaration_type)
        # statements -> assignment
        elif node.type == 'assignment':
            variable = node.child[0]
            if variable not in self.sym_table.keys():
                print(Error_handler(self.error_types['undeclared_value'], node))
            else:
                _type = self.sym_table[variable].type
                expression = self.interpreter_node(node.child[1])
                try:
                    self.assign(_type, variable, expression)
                except InterpreterConverseError:
                    print(Error_handler(self.error_types['cast'], node))
                except InterpreterValueError:
                    print(Error_handler(self.error_types['value'], node))
        # statements -> while
        elif node.type == 'while':
            self.op_while(node)
        # statements -> if
        elif node.type == 'if':
            self.op_if(node)
        # statements -> command -> vector
        elif node.type == 'vector':
            if node.value == 'pushback':
                expression = self.interpreter_node(node.child[1])
                self.vector_push_back(node.child[0], expression)
            if node.value == 'pushfront':
                expression = self.interpreter_node(node.child[1])
                self.vector_push_front(node.child[0], expression)
            if node.value == 'popback':
                self.vector_pop_back(node.child[0])
            if node.value == 'popfront':
                self.vector_pop_front(node.child[0])
        # statements -> command -> converting
        elif node.type == 'converting':
            expression_from = self.interpreter_node(node.value)
            expression_to = node.child.value
            if not node.child.type != "type":
                expression_to = self.interpreter_node(node.child.value).type
            if expression_to in ['integer', 'string', 'boolean']:
                return self.converse.converse(expression_to, expression_from.value)
            elif len(expression_to.split()) == 3:
                if expression_to == 'vector of integer':
                    return Variable('vector of integer', [self.converse.converse('integer', expression_from.value).value])
                elif expression_to == 'vector of boolean':
                    return Variable('vector of boolean', [self.converse.converse('boolean', expression_from.value).value])
                elif expression_to == 'vector of string':
                    return Variable('vector of string', [self.converse.converse('string', expression_from.value).value])
            elif len(expression_to.split()) == 2:
                return Variable('vector of string ' + str(expression_from.type), expression_from.value)
            else:
                raise InterpreterConverseError

        # statements -> command -> converting
        elif node.type == 'robot':
            if node.value == 'forward':
                return self.robot_forward()
            elif node.value == 'back':
                return self.robot_back()
            elif node.value == 'left':
                return self.robot_left()
            elif node.value == 'right':
                return self.robot_right()
            elif node.value == 'rotate_right':
                return self.robot_rotate_right()
            elif node.value == 'rotate_left':
                return self.robot_rotate_left()
            elif node.value == 'lms':
                return self.robot_lms()
            elif node.value == 'reflect':
                return self.robot_reflect()
            elif node.value == 'drill':
                return self.robot_drill()
        # statements -> function
        elif node.type == 'function_description':
            # TODO FUNCTION
            pass
        # statements -> call
        elif node.type == 'call':
            if node.value not in self.funcs:
                print(Error_handler(self.error_types['func_call_error'], node))
                return
            # TODO PARAMETERS - node.child
            return self.interpreter_node(self.funcs[node.value])
        # statements -> return
        elif node.type == 'return':
            return self.interpreter_node(node.value)

        # EXPRESSION BLOCK

        # expression -> math_expression
        elif node.type == 'unary_expression':
            if node.value == '-':
                return self.un_minus(node.child)
        elif node.type == 'binary_expression':
            if node.value == '+':
                return self.bin_plus(node.child[0], node.child[1])
            elif node.value == '-':
                return self.bin_minus(node.child[0], node.child[1])
            elif node.value == '>':
                return self.bin_gr(node.child[0], node.child[1])
            elif node.value == '<':
                return self.bin_ls(node.child[0], node.child[1])
            elif node.value == '=':
                return self.bin_eq(node.child[0], node.child[1])
            elif node.value == '^':
                return self.bin_not_eq(node.child[0], node.child[1])
        # expression -> const
        elif node.type == 'const':
            return self.const_val(node.value)
        # expression / variables -> variable
        elif node.type == 'variable':
            return node.value
        # variable -> indexing
        elif node.type == 'indexing':
            expression = self.interpreter_node(node.child)
            try:
                ret = self.sym_table[node.value][expression]
                return ret
            except KeyError:
                print(Error_handler(self.error_types['undeclared_value'], node))
            except IndexError:
                print(Error_handler(self.error_types['index_error'], node))
            return
        # variable -> string
        elif node.type == 'string':
            return Variable('string', node.value)

    # for declaration

    def declare_variable(self, node, _type):
        if node.type == 'variables':
            for child in node.child:
                self.declare_variable(child, _type)
        else:
            try:
                self.declare(node.type, node.value)
            except InterpreterRedeclarationError:
                print(Error_handler(self.error_types['value_redeclare'], node))
        if node.type == 'assignment':
            variable = node.child[0]
            expression = self.interpreter_node(node.child[1])
            try:
                self.assign(_type, variable, expression)
            except InterpreterConverseError:
                print(Error_handler(self.error_types['cast'], node))
            except InterpreterValueError:
                print(Error_handler(self.error_types['value'], node))

    def declare(self, _type, _value):
        if _value in self.sym_table.keys():
            raise InterpreterRedeclarationError
        if _type.split(" ")[0] != "vector":
            self.sym_table[_value] = Variable(_type, None)
        else:
            self.sym_table[_value] = [_type.split(" ")[2], []]

    def assign(self, _type, variable, expression: Variable):
        if variable not in self.sym_table.keys():
            raise InterpreterNameError
        if _type == expression.type:
            self.sym_table[variable] = expression
        else:
            raise InterpreterConverseError

    # for const
    @staticmethod
    def const_val(value):
        if value.isdigit():
            return Variable('int', int(value))
        else:
            return Variable('int', int(value, 16))

    # for math operations

    # unary minus
    def un_minus(self, _val):
        expression = self.interpreter_node(_val)
        return (-1) * self.converse.converse('integer', expression)

    # binary plus
    def bin_plus(self, _val1, _val2):
        expression1 = self.converse.converse('integer', self.interpreter_node(_val1))
        expression2 = self.converse.converse('integer', self.interpreter_node(_val2))
        return Variable('int', expression1.value + expression2.value)

    # binary minus
    def bin_minus(self, _val1, _val2):
        expression1 = self.converse.converse('integer', self.interpreter_node(_val1))
        expression2 = self.converse.converse('integer', self.interpreter_node(_val2))
        return Variable('int', expression1.value - expression2.value)

    # binary greater
    def bin_gr(self, _val1, _val2):
        expression1 = self.converse.converse('integer', self.interpreter_node(_val1))
        expression2 = self.converse.converse('integer', self.interpreter_node(_val2))
        return Variable('boolean', 'true') if expression1.value > expression2.value else Variable('boolean', 'false')

    # binary less
    def bin_ls(self, _val1, _val2):
        expression1 = self.converse.converse('integer', self.interpreter_node(_val1))
        expression2 = self.converse.converse('integer', self.interpreter_node(_val2))
        return Variable('boolean', 'true') if expression1.value < expression2.value else Variable('boolean', 'false')

    # binary equal
    def bin_eq(self, _val1, _val2):
        expression1 = self.converse.converse('integer', self.interpreter_node(_val1))
        expression2 = self.converse.converse('integer', self.interpreter_node(_val2))
        return Variable('boolean', 'true') if expression1.value == expression2.value else Variable('boolean', 'false')

    # binary not equal
    def bin_not_eq(self, _val1, _val2):
        expression1 = self.converse.converse('integer', self.interpreter_node(_val1))
        expression2 = self.converse.converse('integer', self.interpreter_node(_val2))
        return Variable('boolean', 'true') if expression1.value != expression2.value else Variable('boolean', 'false')

    # for robot

    def robot_left(self):
        pass

    def robot_right(self):
        pass

    def robot_forward(self):
        pass

    def robot_back(self):
        pass

    def robot_rotate_left(self):
        pass

    def robot_rotate_right(self):
        pass

    def robot_lms(self):
        pass

    def robot_reflect(self):
        pass

    def robot_drill(self):
        pass

    # for vector
    def vector_push_back(self, _value, val: Variable):
        if _value not in self.sym_table.keys():
            raise InterpreterNameError
        else:
            if self.sym_table[_value][0] == val.type:
                self.sym_table[_value][1].append(val.value)
            else:
                raise InterpreterConverseError

    def vector_push_front(self, _value, val: Variable):
        if _value not in self.sym_table.keys():
            raise InterpreterNameError
        else:
            if self.sym_table[_value][0] == val.type:
                self.sym_table[_value][1].insert(0, val.value)
            else:
                raise InterpreterConverseError

    def vector_pop_front(self, _value):
        if _value not in self.sym_table.keys():
            raise InterpreterNameError
        else:
            return self.sym_table[_value][1].pop(0)

    def vector_pop_back(self, _value):
        if _value not in self.sym_table.keys():
            raise InterpreterNameError
        else:
            return self.sym_table[_value][1].pop()

    # for while

    def op_while(self, vector):
        pass

    # for if

    def op_if(self, vector):
        pass
