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
    pass


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

        # statements -> while
        # statements -> if
        # statements -> command
        # statements -> function
        # statements -> call
        # statements -> return

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

