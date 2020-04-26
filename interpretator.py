import sys
from Parser.parser import parser
from Robot import map
from Robot.robot import robot
from Errors.errors import Error_handler
from Errors.errors import InterpreterNameError
from Errors.errors import InterpreterConverseError
from Errors.errors import InterpreterValueError
from Errors.errors import InterpreterRedeclarationError


# Item of symbol table
class Variable:
    def __init__(self, var_type='integer', var_value=None):
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


class Interpreter:

    def __init__(self, _parser=parser(), _converse=TypeConversion()):
        self.parser = _parser
        self.converse = _converse
        # DELETE ME
        self.sym_table = [dict()]
        self.scope = 0
        self.map = None
        self.program = None
        self.tree = None
        self.funcs = None
        self.robot = None
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
        self.sym_table = [dict()]
        # noinspection PyBroadException
        try:
            self.tree, self.funcs = self.parser.parse(program)
        except Exception:
            if 'application' not in self.funcs.keys():
                print(Error_handler(self.error_types['no_application']))
                return
        self.interpreter_tree(self.tree)
        self.interpreter_node(self.funcs['application'])

    def interpreter_tree(self, _tree):
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
            variable = node.child[0].value
            if variable not in self.sym_table[self.scope].keys():
                print(Error_handler(self.error_types['undeclared_value'], node))
            else:
                _type = self.sym_table[self.scope][variable].type
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
            if node.child.type != "type":
                expression_to = self.interpreter_node(node.child.value).type
            if expression_to in ['integer', 'string', 'boolean']:
                return self.converse.converse(expression_to, expression_from)
            elif len(expression_to.split()) == 3:
                if expression_to == 'vector of integer':
                    return Variable('vector of integer',
                                    [self.converse.converse('integer', expression_from).value])
                elif expression_to == 'vector of boolean':
                    return Variable('vector of boolean',
                                    [self.converse.converse('boolean', expression_from).value])
                elif expression_to == 'vector of string':
                    return Variable('vector of string', [self.converse.converse('string', expression_from).value])
            elif len(expression_to.split()) == 2:
                return Variable('vector of string ' + str(expression_from.type), expression_from)
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
            pass
        # statements -> call
        elif node.type == 'call':
            return self.function_call(node)
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
            elif node.value == '<>':
                return self.bin_not_eq(node.child[0], node.child[1])
        # expression -> const
        elif node.type == 'const':
            return self.const_val(node.value)
        # expression / variables -> variable
        elif node.type == 'variable':
            var = node.value
            if var not in self.sym_table[self.scope].keys():
                print(Error_handler(self.error_types['undeclared_value'], node))
                return
            return self.sym_table[self.scope][var]
        # variable -> indexing
        elif node.type == 'indexing':
            try:
                var = node.value
                index = self.converse.converse('integer', self.interpreter_node(node.child))
                if index == len(self.sym_table[self.scope][var][1]):
                    self.sym_table[self.scope][var].append(Variable())
                elif index > len(self.sym_table[self.scope][var][1]):
                    print(Error_handler(self.error_types['index_error'], node))
                    return
                return self.sym_table[self.scope][var][1][index]
            except InterpreterConverseError:
                print(Error_handler(self.error_types['cast'], node))
            except InterpreterValueError:
                print(Error_handler(self.error_types['value'], node))
            except InterpreterNameError:
                print(Error_handler(self.error_types['undeclared_value'], node))
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
                if node.type == 'assignment':
                    self.declare(_type, node.child[0].value)
                else:
                    self.declare(_type, node.value)
            except InterpreterRedeclarationError:
                print(Error_handler(self.error_types['value_redeclare'], node))
        if node.type == 'assignment':
            variable = node.child[0].value
            expression = self.interpreter_node(node.child[1])
            try:
                self.assign(_type, variable, expression)
            except InterpreterConverseError:
                print(Error_handler(self.error_types['cast'], node))
            except InterpreterValueError:
                print(Error_handler(self.error_types['value'], node))

    def declare(self, _type, _value):
        if _value in self.sym_table[self.scope].keys():
            raise InterpreterRedeclarationError
        if _type.split(" ")[0] != "vector":
            self.sym_table[self.scope][_value] = Variable(_type, None)
        else:
            self.sym_table[_value] = [_type.split(" ")[2], []]

    def assign(self, _type, variable, expression: Variable):
        if variable not in self.sym_table[self.scope].keys():
            raise InterpreterNameError
        if _type == expression.type:
            self.sym_table[self.scope][variable] = expression
        else:
            raise InterpreterConverseError

    # for const
    @staticmethod
    def const_val(value):
        if (str(value)).isdigit():
            return Variable('integer', int(value))
        elif value in ['true', 'false', 'undefined']:
            return Variable('boolean', value)
        else:
            return Variable('string', value)

    # for math operations

    # unary minus
    def un_minus(self, _val):
        expression = self.interpreter_node(_val)
        curr = self.converse.converse('integer', expression)
        curr.value *= -1
        return curr

    # binary plus
    def bin_plus(self, _val1, _val2):
        expression1 = self.converse.converse('integer', self.interpreter_node(_val1))
        expression2 = self.converse.converse('integer', self.interpreter_node(_val2))
        return Variable('integer', expression1.value + expression2.value)

    # binary minus
    def bin_minus(self, _val1, _val2):
        expression1 = self.converse.converse('integer', self.interpreter_node(_val1))
        expression2 = self.converse.converse('integer', self.interpreter_node(_val2))
        return Variable('integer', expression1.value - expression2.value)

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
        return self.robot.lms()

    def robot_reflect(self):
        return self.robot.reflect()

    def robot_drill(self):
        return self.robot.drill()

    # for vector
    def vector_push_back(self, _value, val: Variable):
        if _value not in self.sym_table[self.scope].keys():
            raise InterpreterNameError
        else:
            if self.sym_table[_value][0] == val.type:
                self.sym_table[self.scope][_value][1].append(val.value)
            else:
                raise InterpreterConverseError

    def vector_push_front(self, _value, val: Variable):
        if _value not in self.sym_table[self.scope].keys():
            raise InterpreterNameError
        else:
            if self.sym_table[_value][0] == val.type:
                self.sym_table[self.scope][_value][1].insert(0, val.value)
            else:
                raise InterpreterConverseError

    def vector_pop_front(self, _value):
        if _value not in self.sym_table[self.scope].keys():
            raise InterpreterNameError
        else:
            return self.sym_table[self.scope][_value][1].pop(0)

    def vector_pop_back(self, _value):
        if _value not in self.sym_table[self.scope].keys():
            raise InterpreterNameError
        else:
            return self.sym_table[self.scope][_value][1].pop()

    # for while

    def op_while(self, node):
        try:
            while self.converse.converse('boolean', self.interpreter_node(node.child['condition'])).value == 'true':
                self.interpreter_node(node.child['body'])
        except InterpreterConverseError:
            print(Error_handler(self.error_types['cast'], node))
        except InterpreterValueError:
            print(Error_handler(self.error_types['value'], node))
        except InterpreterNameError:
            print(Error_handler(self.error_types['undeclared_value'], node))

    # for if

    def op_if(self, node):
        try:
            condition = self.interpreter_node(node.child['condition'])
            condition = self.converse.converse('boolean', condition).value
            if condition == 'true':
                self.interpreter_node(node.child['body'])
            elif condition == 'false':
                if 'else' in node.child:
                    self.interpreter_node(node.child['else'])
        except InterpreterConverseError:
            print(Error_handler(self.error_types['cast'], node))
        except InterpreterValueError:
            print(Error_handler(self.error_types['value'], node))
        except InterpreterNameError:
            print(Error_handler(self.error_types['undeclared_value'], node))

    # for functions

    def function_call(self, node):
        func_name = node.value
        if not node.child.empty():
            func_param = self.interpreter_node(node.child)
        else:
            func_param = None
        if func_name not in self.funcs.keys() and func_name not in self.sym_table[self.scope].keys():
            print(Error_handler(self.error_types['undeclared_value'], node))
            return
        self.scope += 1
        self.sym_table.append(dict())
        func_subtree = self.funcs[func_name] or self.sym_table[self.scope - 1][func_name]
        self.sym_table[self.scope][func_subtree.child['parameters'].value] = func_param
        self.interpreter_node(func_subtree.children['body'])
        self.scope -= 1
        self.sym_table.pop()


if __name__ == '__main__':
    correct = False
    text = None
    while not correct:
        print("Input type? (console, file)")
        inputType = input()
        correct = True
        if inputType == "console":
            text = sys.stdin.read()
        elif inputType == "file":
            f = open("Tests For Parser/interpretator")
            text = f.read()
            f.close()
            print(f'Your file:\n {text}')
        else:
            print("I think, you're wrong :)")
            correct = False

    parser = parser()
    tree, func_table = parser.parse(text)
    interpreter = Interpreter()
    interpreter.interpreter_node(tree)
    print(f'Symbols table:\n')
    for sym_table in interpreter.sym_table:
        for keys, values in sym_table.items():
            if isinstance(values, Variable):
                print(values.type, keys, '=', values.value)
            else:
                print(values[0], keys, ':', values[1:])
