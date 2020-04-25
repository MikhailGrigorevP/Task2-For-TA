from __future__ import annotations
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
        if _type == 'integer':
            if var.type == 'boolean':
                return self.bool_to_int(var)
        else:
            raise ValueError('wrong type')

    @staticmethod
    def bool_to_int(value):
        if value.value == 'true':
            return Variable('integer', 1)
        elif value.value == 'false':
            return Variable('integer', 0)
        elif value.value == 'undefined':
            return Variable('int', 'undefined')
        raise ValueError('wrong type')

    @staticmethod
    def int_to_bool(value):
        if value.value == '0':
            return Variable('bool', 'false')
        elif isinstance(value.value, int):
            return Variable('bool', 'true')
        raise ValueError('wrong type')


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

    def __init__(self, par):
        self.parser = par
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
            'func_call_error': 5
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
            declaration_type = node.value
            declaration_child = node.child.child
            # if declare a group of variables
            if isinstance(declaration_child, list):
                for ch in declaration_child:
                    self.declare_variable(ch, declaration_type)
            # if declare a variables
            else:
                self.declare_variable(declaration_child, declaration_type)
        # statements -> assignment
        # TODO ASSIGNMENT
        # statements -> while
        elif node.type == 'while':
            self.op_while(node)
        # statements -> if
        elif node.type == 'if':
            self.op_if(node)
        # statements -> command -> vector
        elif node.type == 'vector':
            if node.value == 'pushback':
                self.vector_push_back(node.child[0], node.child[1])
            if node.value == 'pushfront':
                self.vector_push_front(node.child[0], node.child[1])
            if node.value == 'popback':
                self.vector_pop_back(node.child[0])
            if node.value == 'popfront':
                self.vector_pop_front(node.child[0])
        # statements -> command -> converting
        elif node.type == 'converting':
            # TODO converting
            pass
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
        # TODO RETURN

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

    # for declaration

    def declare_variable(self, _child, _type):
        pass

    # for const

    def const_val(self, _value):
        pass

    # for math operations

    def un_minus(self, _val):
        pass

    def bin_plus(self, _val1, _val2):
        pass

    def bin_minus(self, _val1, _val2):
        pass

    def bin_gr(self, _val1, _val2):
        pass

    def bin_ls(self, _val1, _val2):
        pass

    def bin_eq(self, _val1, _val2):
        pass

    def bin_not_eq(self, _val1, _val2):
        pass

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

    def vector_push_back(self, vector, val):
        pass

    def vector_push_front(self, vector, val):
        pass

    def vector_pop_front(self, vector):
        pass

    def vector_pop_back(self, vector):
        pass

    # for while

    def op_while(self, vector):
        pass

    # for if

    def op_if(self, vector):
        pass
