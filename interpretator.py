import sys
import copy
from Parser.parser import parser
from Tree.syntaxTree import node as Node
from Robot.robot import Robot, Cell, cells
from Errors.errors import Error_handler
from Errors.errors import InterpreterNameError
from Errors.errors import InterpreterConverseError
from Errors.errors import InterpreterValueError
from Errors.errors import InterpreterRedeclarationError
from Errors.errors import InterpreterIndexError
from Errors.errors import InterpreterApplicationCall


# Item of symbol table
class Variable:
    def __init__(self, var_type='integer', var_value=None):
        self.type = var_type
        if self.type == 'boolean':
            if var_value == "false":
                self.value = False
            elif var_value == "true":
                self.value = bool(True)
            else:
                self.value = var_value
        else:
            self.value = var_value

    def __repr__(self):
        return f'{self.type}, {self.value}'


# Conversion of types
class TypeConversion:
    def __init__(self):
        pass

    def converse(self, _type, var):
        try:
            if _type == var.type:
                return var
            if _type == 'boolean':
                if var.type == 'integer':
                    return self.int_to_bool(var)
                if var.type == 'string':
                    return self.string_to_bool(var)
            if _type == 'integer':
                if var.type == 'boolean':
                    return self.bool_to_int(var)
                if var.type == 'string':
                    return self.string_to_int(var)
            if _type == 'string':
                if var.type == 'vector':
                    return self.vector_to_string(var)
                if var.type == 'boolean':
                    return self.bool_to_string(var)
                if var.type == 'integer':
                    return self.int_to_string(var)
            else:
                raise InterpreterValueError('wrong type')
        except ValueError:
            raise InterpreterValueError('wrong type')
        except InterpreterValueError:
            raise InterpreterValueError('wrong type')

    @staticmethod
    def bool_to_int(value):
        if value.value == 'True':
            return Variable('integer', 1)
        elif value.value == 'False':
            return Variable('integer', 0)
        elif value.value == 'undefined':
            return Variable('integer', 'undefined')
        raise InterpreterValueError

    @staticmethod
    def int_to_bool(value):
        if int(value.value) == 0:
            return Variable('boolean', False)
        elif isinstance(value.value, int):
            return Variable('boolean', True)
        raise InterpreterValueError

    @staticmethod
    def string_to_bool(value):
        if value.value.lower() == "false":
            return Variable('boolean', bool(value.value))
        if value.value.lower() == "true":
            return Variable('boolean', bool(value.value))
        else:
            raise InterpreterValueError

    @staticmethod
    def string_to_int(value):
        if value.value.isdigit():
            return Variable('integer', int(value.value))
        else:
            raise InterpreterValueError

    @staticmethod
    def int_to_string(value):
        return Variable('string', str(value.value))

    @staticmethod
    def bool_to_string(value):
        return Variable('string', str(value.value))

    @staticmethod
    def vector_to_string(value):
        string = ''
        for char in value.value:
            string.join(char)
        return Variable('string', value.value)


class Interpreter:

    def __init__(self, _parser=parser(), _converse=TypeConversion()):
        self.parser = _parser
        self.converse = _converse
        # DELETE ME
        self.sym_table = [dict()]
        self.scope = 0
        self.program = None
        self.fatal_error = False
        self.find_exit = False
        self.tree = None
        self.funcs = None
        self.robot = None
        self.error = Error_handler()
        self.error_types = {
            'UnexpectedError': 0,
            'NoInputPoint': 1,
            'RedeclarationError': 2,
            'UndeclaredError': 3,
            'IndexError': 4,
            'FuncCallError': 5,
            'ConserveError': 6,
            'ValueError': 7,
            'ApplicationCall': 8,
            'WrongParameters': 9,
            'Recursion': 10,
            'TypeError': 11
        }

    def interpreter(self, _robot=None, program=None):
        self.robot = _robot
        self.program = program
        self.sym_table = [dict()]
        self.tree, self.funcs, _correctness = self.parser.parse(self.program)
        if _correctness:
            if 'application' not in self.funcs.keys():
                self.error.call(self.error_types['NoInputPoint'])
                return
            self.interpreter_tree(self.tree)
            try:
                self.interpreter_node(self.funcs['application'].child['body'])
            except RecursionError:
                sys.stderr.write(f'RecursionError: function calls itself too many times\n')
                sys.stderr.write("========= Program has finished with fatal error =========\n")
        else:
            sys.stderr.write(f'Can\'t intemperate incorrect input file\n')

    @staticmethod
    def interpreter_tree(_tree):
        print("Program tree:\n")
        _tree.print()
        print("\n")

    def interpreter_node(self, node):
        # log robot
        # if 'free' in self.sym_table[self.scope]:
        # #    print("stack_x:", self.sym_table[self.scope]['stack_x'])
        # #    print("stack_y:", self.sym_table[self.scope]['stack_y'])
        # #    print("stack_t:", self.sym_table[self.scope]['stack_t'])
        # #    print("size:", self.sym_table[self.scope]['st'])
        # #    print("vm:", self.sym_table[self.scope]['vm'])
        # #    print(self.robot.lms(), self.sym_table[self.scope]['turn'], self.sym_table[self.scope]['numOfTurns'])
        # #    print(self.robot.lms(), "-", self.sym_table[self.scope]['free'].value)
        #     print("real:", self.robot.turn, self.robot.x, self.robot.y)
        #     print("drill:", self.robot.power)
        #     print("x,y:", self.sym_table[self.scope]['turn'].value, self.sym_table[self.scope]['x'].value,
        #           self.sym_table[self.scope]['y'].value)
        #
        # if self.sym_table[self.scope]['x'].value == 17 and self.robot.power == 0 and self.sym_table[self.scope][
        # 'y'].value == 17 and self.robot.power == 0: print("Fs") nothing
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
            try:
                for ch in node.child:
                    try:
                        self.interpreter_node(ch)
                        if self.fatal_error:
                            raise RecursionError from None
                    except RecursionError:
                        raise RecursionError from None
                    if self.fatal_error:
                        break
            except RecursionError:
                raise RecursionError from None

        elif node.type == 'error':
            self.error.call(self.error_types['UnexpectedError'], node)

        # STATEMENTS BLOCK

        # statements -> declaration
        elif node.type == 'declaration':
            self.sym_table[self.scope]['#result'] = "error"
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
            if node.child[0].type == 'indexing':
                try:
                    var = node.child[0].value
                    indexes = []
                    children = node.child[0].child
                    while children.type == 'indexing':
                        if isinstance(children.child, list):
                            indexes.append(children.child[0])
                            children = children.child[1]
                        else:
                            indexes.append(children.child)
                            children = children.child
                    for i in range(len(indexes)):
                        indexes[i] = self.converse.converse('integer', self.interpreter_node(indexes[i])).value
                    current_var = self.sym_table[self.scope][var][1]
                    fullPath = len(indexes)
                    p = 0
                    for index in indexes:
                        p += 1
                        if index == len(current_var):
                            current_var.append(Variable())
                        elif index > len(current_var):
                            self.error.call(self.error_types['IndexError'], node)
                        else:
                            expression = self.interpreter_node(node.child[1])
                            if isinstance(expression, list):
                                current_var[index] = expression
                                self.sym_table[self.scope]['#result'] = expression
                            elif not isinstance(expression, Variable):
                                current_var[index] = expression
                                self.sym_table[self.scope]['#result'] = expression
                            else:
                                if p == fullPath:
                                    current_var[index] = expression.value
                                    self.sym_table[self.scope]['#result'] = expression.value
                                else:
                                    current_var = current_var[index]
                    return
                except InterpreterConverseError:
                    self.error.call(self.error_types['ConserveError'], node)
                except InterpreterValueError:
                    self.error.call(self.error_types['ValueError'], node)
                except InterpreterNameError:
                    self.error.call(self.error_types['UndeclaredError'], node)
                except RecursionError:
                    raise RecursionError from None
            else:
                variable = node.child[0].value
            if variable not in self.sym_table[self.scope].keys():
                self.error.call(self.error_types['UndeclaredError'], node)
            else:
                if isinstance(self.sym_table[self.scope][variable], list):
                    _type = self.sym_table[self.scope][variable][0]
                else:
                    _type = self.sym_table[self.scope][variable].type
                if node.child[1].type == "indexing":
                    node.child[1].type = "get_indexing"
                try:
                    expression = self.interpreter_node(node.child[1])
                except InterpreterConverseError:
                    self.error.call(self.error_types['ConserveError'], node)
                    return
                except InterpreterValueError:
                    self.error.call(self.error_types['ValueError'], node)
                    return
                try:
                    self.assign(_type, variable, expression)
                    self.sym_table[self.scope]['#result'] = expression
                except InterpreterNameError:
                    self.error.call(self.error_types['UndeclaredError'], node)
                except InterpreterConverseError:
                    self.error.call(self.error_types['ConserveError'], node)
                except InterpreterValueError:
                    self.error.call(self.error_types['ValueError'], node)
                except RecursionError:
                    raise RecursionError from None
        # statements -> while
        elif node.type == 'while':
            self.op_while(node)
            self.sym_table[self.scope]['#result'] = "error"
        # statements -> if
        elif node.type == 'if':
            self.op_if(node)
            self.sym_table[self.scope]['#result'] = "error"
        # statements -> command -> vector
        elif node.type == 'vector':
            if node.value == 'pushback':
                try:
                    expression = self.interpreter_node(node.child[1])
                    if isinstance(expression, list) and len(expression) > 1:
                        expression = Variable(expression[0], expression[1])
                    elif isinstance(expression, list):
                        _type = self.sym_table[self.scope][node.child[1].value][0].split()[2]
                        expression = Variable(_type, expression[0])
                    if node.child[0].type == 'indexing':
                        var = self.interpreter_node(node.child[0])
                        if isinstance(var, list) and isinstance(var[0], list) and len(var[0]) == 0:
                            var[0].append(expression.value)
                        else:
                            self.vector_push_back_2(var, expression)
                            self.sym_table[self.scope]['#result'] = expression.value
                    else:
                        self.vector_push_back(node.child[0], expression)
                except InterpreterConverseError:
                    self.error.call(self.error_types['ConserveError'], node)
                except InterpreterValueError:
                    self.error.call(self.error_types['ValueError'], node)
                except InterpreterNameError:
                    self.error.call(self.error_types['UndeclaredError'], node)
                except InterpreterIndexError:
                    self.error.call(self.error_types['IndexError'], node)
            if node.value == 'pushfront':
                try:
                    expression = self.interpreter_node(node.child[1])
                    if node.child[0].type == 'indexing':
                        var = self.interpreter_node(node.child[0])
                        self.vector_push_front_2(var, expression)
                        self.sym_table[self.scope]['#result'] = expression.value
                    else:
                        self.vector_push_front(node.child[0], expression)
                except InterpreterConverseError:
                    self.error.call(self.error_types['ConserveError'], node)
                except InterpreterValueError:
                    self.error.call(self.error_types['ValueError'], node)
                except InterpreterNameError:
                    self.error.call(self.error_types['UndeclaredError'], node)
                except InterpreterIndexError:
                    self.error.call(self.error_types['IndexError'], node)
            if node.value == 'popback':
                try:
                    if node.child.type == 'indexing':
                        var = self.interpreter_node(node.child)
                        return self.vector_pop_back_2(var)
                    else:
                        return self.vector_pop_back(node.child)
                except InterpreterConverseError:
                    self.error.call(self.error_types['ConserveError'], node)
                except InterpreterValueError:
                    self.error.call(self.error_types['ValueError'], node)
                except InterpreterNameError:
                    self.error.call(self.error_types['UndeclaredError'], node)
                except InterpreterIndexError:
                    self.error.call(self.error_types['IndexError'], node)
            if node.value == 'popfront':
                try:
                    if node.child.type == 'indexing':
                        var = self.interpreter_node(node.child)
                        return self.vector_pop_front_2(var)
                    else:
                        return self.vector_pop_front(node.child)
                except InterpreterConverseError:
                    self.error.call(self.error_types['ConserveError'], node)
                except InterpreterValueError:
                    self.error.call(self.error_types['ValueError'], node)
                except InterpreterNameError:
                    self.error.call(self.error_types['UndeclaredError'], node)
                except InterpreterIndexError:
                    self.error.call(self.error_types['IndexError'], node)
        # statements -> command -> converting
        elif node.type == 'converting':
            expression_from = self.interpreter_node(node.value)
            if isinstance(node.child, int):
                size = node.child
                vector = [expression_from.value]
                if size > 1:
                    for i in range(size):
                        vector = [vector]
                if expression_from.type == 'string':
                    return ['vector of string', vector, node.child]
                elif expression_from.type == 'boolean':
                    return ['vector of boolean', vector, node.child]
                elif expression_from.type == 'integer':
                    return ['vector of integer', vector, node.child]
                else:
                    raise InterpreterConverseError
            expression_to = node.child.value
            if node.child.type != "type":
                if node.child.type == "string":
                    expression_to = 'string'
                elif node.child.type == "integer":
                    expression_to = 'integer'
                elif node.child.type == "boolean":
                    expression_to = 'boolean'
                else:
                    expression_to = self.interpreter_node(node.child.value).type
            if expression_to in ['integer', 'string', 'boolean']:
                return self.converse.converse(expression_to, expression_from)
            elif len(expression_to.split()) == 4:
                if expression_to == 'vector of type integer':
                    return ['vector of integer',
                            [self.converse.converse('integer', expression_from).value], 1]
                elif expression_to == 'vector of type boolean':
                    return ['vector of boolean',
                            [self.converse.converse('boolean', expression_from).value], 1]
                elif expression_to == 'vector of type string':
                    return ['vector of string', [self.converse.converse('string', expression_from).value], 1]
            else:
                raise InterpreterConverseError

        # statements -> command -> robot
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
            self.sym_table[self.scope]['#result'] = "error"
        # statements -> function
        elif node.type == 'function_description':
            pass
        # statements -> call
        elif node.type == 'call':
            try:
                return self.function_call(node)
            except InterpreterApplicationCall:
                self.error.call(self.error_types['ApplicationCall'], node)
                return None
            except RecursionError:
                raise RecursionError from None
        # statements -> return
        elif node.type == 'return':
            self.sym_table[self.scope]['#result'] = self.interpreter_node(node.value)

        # EXPRESSION BLOCK

        # expression -> math_expression
        elif node.type == 'binary_expression':
            try:
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
                elif node.value == '<>':
                    return self.bin_not_eq(node.child[0], node.child[1])
            except TypeError:
                self.error.call(self.error_types['TypeError'], node)
        # expression -> const
        elif node.type == 'const':
            return self.const_val(node.value)
        # expression / variables -> variable
        elif node.type == 'variable':
            var = node.value
            if var not in self.sym_table[self.scope].keys():
                self.error.call(self.error_types['UndeclaredError'], node)
                return
            return self.sym_table[self.scope][var]
        # variable -> indexing
        elif node.type == 'get_indexing':
            try:
                var = node.value
                indexes = []
                children = node.child
                while children.type == 'indexing':
                    if isinstance(children.child, list):
                        indexes.append(children.child[0])
                        children = children.child[1]
                    else:
                        indexes.append(children.child)
                        children = children.child
                for i in range(len(indexes)):
                    indexes[i] = self.converse.converse('integer', self.interpreter_node(indexes[i])).value
                current_type = self.sym_table[self.scope][var][0].split(" ")[2]
                current_var = self.sym_table[self.scope][var][1]
                full_size = self.sym_table[self.scope][var][2]
                for index in indexes:
                    if index == len(current_var):
                        current_var.append(Variable())
                    elif index > len(current_var):
                        raise InterpreterIndexError
                    if isinstance(current_var[index], list):
                        if len(current_var[index]) == 0:
                            return current_var
                    current_var = current_var[index]
                if len(indexes) == full_size:
                    if isinstance(current_var, list):
                        return Variable(current_type, current_var[0])
                    else:
                        return Variable(current_type, current_var)
                else:
                    return Variable(current_type, current_var)
            except InterpreterConverseError:
                raise InterpreterConverseError
            except InterpreterValueError:
                raise InterpreterValueError
            except InterpreterNameError:
                raise InterpreterNameError
            except InterpreterIndexError:
                raise InterpreterIndexError
            except IndexError:
                raise InterpreterIndexError
        elif node.type == 'indexing':
            try:
                var = node.value
                indexes = []
                children = node.child
                while children.type == 'indexing':
                    if isinstance(children.child, list):
                        indexes.append(children.child[0])
                        children = children.child[1]
                    else:
                        indexes.append(children.child)
                        children = children.child
                for i in range(len(indexes)):
                    indexes[i] = self.converse.converse('integer', self.interpreter_node(indexes[i])).value
                current_var = self.sym_table[self.scope][var][1]
                full_size = self.sym_table[self.scope][var][2]
                for index in indexes:
                    if index == len(current_var):
                        current_var.append(Variable())
                    elif index > len(current_var):
                        self.error.call(self.error_types['IndexError'], node)
                    if isinstance(current_var[index], list):
                        if len(current_var[index]) == 0:
                            return current_var
                    current_var = current_var[index]
                if len(indexes) == full_size:
                    return current_var
                else:
                    return current_var
            except InterpreterConverseError:
                self.error.call(self.error_types['ConserveError'], node)
            except InterpreterValueError:
                self.error.call(self.error_types['ValueError'], node)
            except InterpreterNameError:
                self.error.call(self.error_types['UndeclaredError'], node)
            except IndexError:
                self.error.call(self.error_types['IndexError'], node)
        # variable -> string
        elif node.type == 'string':
            return Variable('string', str(node.value))

    # for declaration

    def declare_variable(self, node, _type):
        if node.type == 'variables':
            if isinstance(node.child, list):
                for child in node.child:
                    self.declare_variable(child, _type)
            else:
                node = node.child
                try:
                    if node.type == 'assignment':
                        self.declare(_type, node.child[0].value)
                    else:
                        self.declare(_type, node.value)
                except InterpreterRedeclarationError:
                    self.error.call(self.error_types['RedeclarationError'], node)
                    return
        else:
            try:
                if node.type == 'assignment':
                    self.declare(_type, node.child[0].value)
                else:
                    self.declare(_type, node.value)
            except InterpreterRedeclarationError:
                self.error.call(self.error_types['RedeclarationError'], node)
        if node.type == 'assignment':
            variable = node.child[0].value
            if node.child[1].type == "indexing":
                node.child[1].type = "get_indexing"
            try:
                expression = self.interpreter_node(node.child[1])
            except InterpreterConverseError:
                self.error.call(self.error_types['ConserveError'], node)
                return
            except InterpreterValueError:
                self.error.call(self.error_types['ValueError'], node)
                return
            except InterpreterIndexError:
                self.error.call(self.error_types['IndexError'], node)
                return
            try:
                self.assign(_type, variable, expression)
                self.sym_table[self.scope]['#result'] = expression
            except InterpreterConverseError:
                self.error.call(self.error_types['ConserveError'], node)
            except InterpreterValueError:
                self.error.call(self.error_types['ValueError'], node)
            except InterpreterIndexError:
                self.error.call(self.error_types['IndexError'], node)
            except InterpreterNameError:
                self.error.call(self.error_types['UndeclaredError'], node)

    def declare(self, _type, _value):
        if _value in self.sym_table[self.scope].keys():
            raise InterpreterRedeclarationError
        if _type in ['integer', 'boolean', 'string']:
            self.sym_table[self.scope][_value] = Variable(_type, None)
        else:
            mega_type = _type.split(" ")
            last_elem = len(mega_type) - 1
            size = (len(mega_type) - 1) // 3
            vector = []
            if size > 1:
                for i in range(size):
                    vector = [vector]
            self.sym_table[self.scope][_value] = \
                [_type.split(" ")[0] + ' ' + _type.split(" ")[1] + ' ' + _type.split(" ")[last_elem], vector, size]

    def assign(self, _type, variable, expression: Variable):
        try:
            if expression is None:
                return
            if variable not in self.sym_table[self.scope].keys():
                raise InterpreterNameError
            if isinstance(expression, list):
                if _type == expression[0]:
                    self.sym_table[self.scope][variable] = expression.copy()
                else:
                    raise InterpreterConverseError
            elif _type == expression.type:
                self.sym_table[self.scope][variable] = expression
            else:
                raise InterpreterConverseError
        except RecursionError:
            raise RecursionError from None

    # for const
    @staticmethod
    def const_val(value):
        if (str(value)).isdigit():
            return Variable('integer', int(value))
        elif value in ['true', 'false', True, False, 'undefined']:
            return Variable('boolean', value)
        else:
            return Variable('string', value)

    # for math operations

    # binary plus
    def bin_plus(self, _val1, _val2):
        if _val1.type == "indexing":
            _val1.type = "get_indexing"
        if _val2.type == "indexing":
            _val2.type = "get_indexing"
        if isinstance(_val1, Node):
            _val1 = self.interpreter_node(_val1)
            _val2 = self.interpreter_node(_val2)
            if isinstance(_val1, Variable) and isinstance(_val2, Variable):
                if _val1.type == _val2.type == "integer":
                    return Variable('integer', _val1.value + _val2.value)
                elif _val1.type == _val2.type == "boolean":
                    return Variable('boolean', bool(_val1.value) or bool(_val2.value))
                elif _val1.type == _val2.type == "string":
                    return Variable('string', _val1.value + _val2.value)
            else:
                _val = copy.deepcopy(_val1)
                for i in range(len(_val[1])):
                    _val[1][i] = self.bin_plus(_val1[1][i], _val2[1][i])
                return _val
        else:
            if isinstance(_val1, list):
                _val = copy.deepcopy(_val1)
                for i in range(len(_val)):
                    _val[i] = self.bin_plus(_val1[i], _val2[i])
                return _val
            if isinstance(_val1, int):
                return _val1 + _val2
            elif isinstance(_val1, bool):
                return _val1 or _val2
            elif isinstance(_val1, str):
                return _val1 + _val2
            return _val1

    # binary minus
    def bin_minus(self, _val1, _val2):
        if _val1.type == "indexing":
            _val1.type = "get_indexing"
        if _val2.type == "indexing":
            _val2.type = "get_indexing"
        if isinstance(_val1, Node):
            _val1 = self.interpreter_node(_val1)
            _val2 = self.interpreter_node(_val2)
            if isinstance(_val1, Variable) and isinstance(_val2, Variable):
                if _val1.type == _val2.type == "integer":
                    return Variable('integer', _val1.value - _val2.value)
                elif _val1.type == _val2.type == "boolean":
                    return Variable('boolean', bool(_val1.value) ^ bool(_val2.value))
                elif _val1.type == _val2.type == "string":
                    return Variable('string', "".join(_val1.value.rsplit(_val2.value)))
            else:
                _val = copy.deepcopy(_val1)
                for i in range(len(_val[1])):
                    _val[1][i] = self.bin_minus(_val1[1][i], _val2[1][i])
                return _val
        else:
            if isinstance(_val1, list):
                _val = copy.deepcopy(_val1)
                for i in range(len(_val1)):
                    _val[i] = self.bin_minus(_val1[i], _val2[i])
                return _val
            if isinstance(_val1, int):
                return _val1 - _val2
            elif isinstance(_val1, bool):
                return _val1 ^ _val2
            elif isinstance(_val1, str):
                return "".join(_val1.value.rsplit(_val2.value))
            return _val1

    # binary greater
    def bin_gr(self, _val1, _val2):
        if _val1.type == "indexing":
            _val1.type = "get_indexing"
        if _val2.type == "indexing":
            _val2.type = "get_indexing"
        expression1 = self.interpreter_node(_val1)
        expression2 = self.interpreter_node(_val2)
        if isinstance(expression1, Variable) and isinstance(expression2, Variable):
            return Variable('boolean', True) if expression1.value > expression2.value else Variable('boolean', False)
        elif isinstance(expression1, list) and isinstance(expression2, list):
            return Variable('boolean', True) if expression1[1] > expression2[1] else Variable('boolean', False)
        else:
            return Variable('boolean', True) if expression1 > expression2 else Variable('boolean', False)

    # binary less
    def bin_ls(self, _val1, _val2):
        if _val1.type == "indexing":
            _val1.type = "get_indexing"
        if _val2.type == "indexing":
            _val2.type = "get_indexing"
        expression1 = self.interpreter_node(_val1)
        expression2 = self.interpreter_node(_val2)
        if isinstance(expression1, Variable) and isinstance(expression2, Variable):
            return Variable('boolean', True) if expression1.value < expression2.value else Variable('boolean', False)
        elif isinstance(expression1, list) and isinstance(expression2, list):
            return Variable('boolean', True) if expression1[1] < expression2[1] else Variable('boolean', False)
        else:
            return Variable('boolean', True) if expression1 > expression2 else Variable('boolean', False)

    # binary equal
    def bin_eq(self, _val1, _val2):
        if _val1.type == "indexing":
            _val1.type = "get_indexing"
        if _val2.type == "indexing":
            _val2.type = "get_indexing"
        expression1 = self.interpreter_node(_val1)
        expression2 = self.interpreter_node(_val2)
        if isinstance(expression1, Variable) and isinstance(expression2, Variable):
            return Variable('boolean', True) if expression1.value == expression2.value else Variable('boolean', False)
        elif isinstance(expression1, list) and isinstance(expression2, list):
            return Variable('boolean', True) if expression1[1] == expression2[1] else Variable('boolean', False)
        else:
            return Variable('boolean', True) if expression1 == expression2 else Variable('boolean', False)

    # binary not equal
    def bin_not_eq(self, _val1, _val2):
        if _val1.type == "indexing":
            _val1.type = "get_indexing"
        if _val2.type == "indexing":
            _val2.type = "get_indexing"
        expression1 = self.interpreter_node(_val1)
        expression2 = self.interpreter_node(_val2)
        if isinstance(expression1, Variable) and isinstance(expression2, Variable):
            return Variable('boolean', True) if expression1.value != expression2.value else Variable('boolean', False)
        elif isinstance(expression1, list) and isinstance(expression2, list):
            return Variable('boolean', True) if expression1[1] != expression2[1] else Variable('boolean', False)
        else:
            return Variable('boolean', True) if expression1 != expression2 else Variable('boolean', False)

    # for robot

    def robot_left(self):
        return self.robot.left()

    def robot_right(self):
        return self.robot.right()

    def robot_forward(self):
        return self.robot.forward()

    def robot_back(self):
        return self.robot.back()

    def robot_rotate_left(self):
        return self.robot.rotate_left()

    def robot_rotate_right(self):
        return self.robot.rotate_right()

    def robot_lms(self):
        result = self.robot.lms()
        return Variable('integer', result)

    def robot_reflect(self):
        result = self.robot.reflect()
        if result == 'EXIT':
            self.find_exit = True
        return Variable("string", result)

    def robot_drill(self):
        return Variable("integer", self.robot.drill())

    # for vector
    def vector_push_back(self, _value, val: Variable):
        _value = _value.value
        if _value not in self.sym_table[self.scope].keys():
            raise InterpreterNameError
        else:
            if self.sym_table[self.scope][_value][2] != 1:
                if isinstance(val.value, list):
                    self.sym_table[self.scope][_value][1].append([val.value.copy()])
                else:
                    self.sym_table[self.scope][_value][1].append([val.value])
            elif val.type in self.sym_table[self.scope][_value][0].split(" "):
                self.sym_table[self.scope][_value][1].append(val.value)
            else:
                raise InterpreterConverseError

    @staticmethod
    def vector_push_back_2(_value, val: Variable):
        try:
            if not isinstance(_value, Variable):
                if isinstance(val.value, list):
                    _value.append(val.value.copy())
                else:
                    _value.append(val.value)
        except AttributeError:
            raise InterpreterIndexError

    def vector_push_front(self, _value, val: Variable):
        _value = _value.value
        if _value not in self.sym_table[self.scope].keys():
            raise InterpreterNameError
        else:
            if self.sym_table[self.scope][_value][2] != 1:
                self.sym_table[self.scope][_value][1].insert(0, [val.value])
            elif val.type in self.sym_table[self.scope][_value][0].split(" "):
                self.sym_table[self.scope][_value][1].insert(0, val.value)
            else:
                raise InterpreterConverseError

    @staticmethod
    def vector_push_front_2(_value, val: Variable):
        try:
            if not isinstance(_value, Variable):
                if isinstance(val.value, list):
                    _value.insert(0, val.value.copy())
                else:
                    _value.append(val.value)
        except AttributeError:
            raise InterpreterIndexError

    def vector_pop_front(self, _value):
        _value = _value.value
        if self.sym_table[self.scope][_value][2] != 1:
            raise InterpreterNameError
        elif _value not in self.sym_table[self.scope].keys():
            raise InterpreterNameError
        else:
            return Variable(self.sym_table[self.scope][_value][0].split(" ")[2],
                            self.sym_table[self.scope][_value][1].pop(0))

    @staticmethod
    def vector_pop_front_2(_value):
        return _value.pop(0)

    def vector_pop_back(self, _value):
        _value = _value.value
        if self.sym_table[self.scope][_value][2] != 1:
            raise InterpreterNameError
        elif _value not in self.sym_table[self.scope].keys():
            raise InterpreterNameError
        else:
            return Variable(self.sym_table[self.scope][_value][0].split(" ")[2],
                            self.sym_table[self.scope][_value][1].pop())

    @staticmethod
    def vector_pop_back_2(_value):
        return _value.pop()

    # for while

    def op_while(self, node):
        try:
            while self.converse.converse('boolean', self.interpreter_node(node.child['condition'])).value:
                self.interpreter_node(node.child['body'])
        except InterpreterConverseError:
            self.error.call(self.error_types['ConserveError'], node)
        except InterpreterValueError:
            self.error.call(self.error_types['ValueError'], node)
        except InterpreterNameError:
            self.error.call(self.error_types['UndeclaredError'], node)
        except IndexError:
            self.error.call(self.error_types['UndeclaredError'], node)

    # for if

    def op_if(self, node):
        try:
            condition = self.interpreter_node(node.child['condition'])
            condition = self.converse.converse('boolean', condition).value
            if condition:
                self.interpreter_node(node.child['body'])
            elif not condition:
                if 'else' in node.child:
                    self.interpreter_node(node.child['else'])
        except InterpreterConverseError:
            self.error.call(self.error_types['ConserveError'], node)
        except InterpreterValueError:
            self.error.call(self.error_types['ValueError'], node)
        except InterpreterNameError:
            self.error.call(self.error_types['UndeclaredError'], node)
        except IndexError:
            self.error.call(self.error_types['UndeclaredError'], node)

    # for functions

    def function_call(self, node):
        func_name = node.value
        param = node.child
        func_param = None
        try:
            while isinstance(param, Node):
                if func_param is None:
                    func_param = []
                if len(param.child) > 1:
                    func_param.append(self.interpreter_node(param.child[1].value))
                elif len(param.child) == 0:
                    break
                else:
                    func_param.append(self.interpreter_node(param.child[0].value))
                param = param.child[0]
                if not isinstance(param.child, list):
                    func_param.append(self.interpreter_node(param.value))
                    func_param.reverse()
                    break
        except InterpreterConverseError:
            self.error.call(self.error_types['ConserveError'], node)
            return None
        except InterpreterValueError:
            self.error.call(self.error_types['ValueError'], node)
            return None
        except InterpreterNameError:
            self.error.call(self.error_types['UndeclaredError'], node)
            return None
        except IndexError:
            self.error.call(self.error_types['UndeclaredError'], node)
        if func_name not in self.funcs.keys() and func_name not in self.sym_table[self.scope].keys():
            self.error.call(self.error_types['FuncCallError'], node)
            return None
        if func_name == 'application':
            raise InterpreterApplicationCall
        self.scope += 1
        self.sym_table.append(dict())
        if '#func' not in self.sym_table[0].keys():
            self.sym_table[0]['#func'] = 1
        else:
            self.sym_table[0]['#func'] += 1
        if self.sym_table[0]['#func'] > 1000:
            raise RecursionError from None
        func_subtree = self.funcs[func_name] or self.sym_table[self.scope - 1][func_name]
        get = func_subtree.child['parameters']
        func_get = None
        while isinstance(get, Node):
            if func_get is None:
                func_get = []
            if len(get.child) > 1:
                try:
                    func_get.append([get.child[1].value, self.interpreter_node(get.child[1].child).value])
                except AttributeError:
                    self.error.call(self.error_types['WrongParameters'], node)
                    return None
            get = get.child[0]
            if isinstance(get.child, Node):
                try:
                    func_get.append([get.value, self.interpreter_node(get.child).value])
                except AttributeError:
                    self.error.call(self.error_types['WrongParameters'], node)
                    return None
                func_get.reverse()
                break
        if func_param:
            func_param.reverse()
            try:
                for i in range(len(func_get)):
                    if i < len(func_param):
                        self.sym_table[self.scope][func_get[i][0]] = func_param[i]
                    else:
                        self.sym_table[self.scope][func_get[i][0]] = func_get[i][1]
            except TypeError:
                self.error.call(self.error_types['WrongParameters'], node)
                self.scope -= 1
                return None
        if func_param and len(func_get) < len(func_param):
            self.error.call(self.error_types['WrongParameters'], node)
            self.scope -= 1
            return None
        result = None
        try:
            self.interpreter_node(func_subtree.child['body'])
            if '#result' in self.sym_table[self.scope].keys():
                result = self.sym_table[self.scope]['#result']
        except RecursionError:
            raise RecursionError from None
        except InterpreterApplicationCall:
            self.error.call(self.error_types['ApplicationCall'], node)
        except InterpreterConverseError:
            self.error.call(self.error_types['ConserveError'], node)
        except InterpreterValueError:
            self.error.call(self.error_types['ValueError'], node)
        except InterpreterNameError:
            self.error.call(self.error_types['UndeclaredError'], node)
        except IndexError:
            self.error.call(self.error_types['UndeclaredError'], node)
        self.sym_table[0]['#func'] -= 1
        self.scope -= 1
        self.sym_table.pop()
        return result


def create_robot(descriptor):
    # Text file description
    # First line - ROBOT (0;0) is left-up corner
    # > Y X TURN POWER
    # Second line - MAP SIZE
    # > N M
    # Next lines - correct_map
    # ' ' - empty
    # c - 'CONCRETE'
    # w - 'WOOD'
    # p -'PLASTIC'
    # g - 'GLASS'
    # s - 'STEEL'
    # e - 'EXIT'

    with open(descriptor) as file:
        _text = file.readlines()
    robot_info = _text.pop(0).rstrip().split(" ")
    map_size = _text.pop(0).rstrip().split(" ")

    # robot set
    x = int(robot_info[0])
    y = int(robot_info[1])
    turn = int(robot_info[2])
    power = int(robot_info[3])
    _map = [0] * int(map_size[0])

    for i in range(int(map_size[0])):
        _map[i] = [0] * int((map_size[1]))
    for i in range(int(map_size[0])):
        for j in range(int(map_size[1])):
            _map[i][j] = Cell("EMPTY")
    pos = 0
    while len(_text) > 0:
        line = list(_text.pop(0).rstrip())
        line = [Cell(cells[i]) for i in line]
        _map[pos] = line
        pos += 1

    return Robot(x=x, y=y, turn=turn, power=power, _map=_map)


if __name__ == '__main__':
    correct = False
    text = None
    isRobot = False
    while not correct:
        print("Input type? (console, file, robot)")
        inputType = input()
        correct = True
        if inputType == "console":
            text = sys.stdin.read()
        elif inputType == "file":
            with open("Tests/vectorsTestErrors") as f:
                text = f.read()
            f.close()
            print(f'Your file:\n {text}')
        elif inputType == "robot":
            isRobot = True
            with open("Tests/PathFinders/VirtualMap") as f:
                text = f.read()
            f.close()
            print(f'Your file:\n {text}')

        else:
            print("I think, you're wrong :)")
            correct = False

    # prepare
    parser = parser()
    tree, func_table, correctness = parser.parse(text)
    robot = create_robot("Tests/Maps/correct_map")
    if correctness:

        interpreter = Interpreter()
        interpreter.interpreter(program=text, _robot=robot)
        print(f'Symbols table:\n')
        for sym_table in interpreter.sym_table:
            for keys, values in sym_table.items():
                if keys == "#result":
                    continue
                if isinstance(values, Variable):
                    print(values.type, keys, '=', values.value)
                else:
                    if not isinstance(values, int):
                        print(values[0], keys, ':', values[1], 'dim:', values[2])
        if isRobot:
            if interpreter.find_exit:
                print("\n\n========== END HAS BEEN FOUND ==========\n\n")
            else:
                print("\n\n========== END HAS NOT BEEN FOUND ==========\n\n")
            print('\nRobot:', interpreter.robot, '\n\nMap:')
            print()
            print('\nEnded:', interpreter.robot.show())
        print('\nerrors:')
    else:
        sys.stderr.write(f'Can\'t interpretate incorrect input file\n')
