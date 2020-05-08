import ply.yacc as yacc
from ply.lex import LexError
import sys
from typing import List, Dict, Tuple, Any

# outer classes
from Lexer.lexer import lexer
from Tree.syntaxTree import node


class parser(object):
    tokens = lexer.tokens
    precedence = lexer.precedence

    def __init__(self):
        self.ok = True
        self.lexer = lexer()
        self.parser = yacc.yacc(module=self)
        self._functions: Dict[str, node] = dict()

    def parse(self, s):
        try:
            res = self.parser.parse(s)
            return res, self._functions, self.ok
        except LexError:
            sys.stderr.write(f'Illegal token {s}\n')

    @staticmethod
    def p_program(p):
        """program : statements"""
        p[0] = node('program', ch=p[1], no=p.lineno(1), pos=p.lexpos(1))

    @staticmethod
    def p_statements_group(p):
        """statements_group : BEGIN statements END
                            | inner_statement"""
        if len(p) == 4:
            p[0] = p[2]
        else:
            p[0] = p[1]

    @staticmethod
    def p_inner_statement(p):
        """inner_statement : declaration
                     | assignment
                     | while
                     | if
                     | command
                     | function
                     | call
                     | RETURN expression
                     | empty"""

        if len(p) == 3:
            p[0] = node('return', val=p[2], no=p.lineno(1), pos=p.lexpos(1))
        else:
            p[0] = p[1]

    @staticmethod
    def p_statements(p):
        """statements : statements statement
                      | statement"""
        if len(p) == 2:
            p[0] = node('statements', ch=[p[1]])
        else:
            p[0] = node('statements', ch=[p[1], p[2]])

    @staticmethod
    def p_statement(p):
        """statement : declaration NEWLINE
                     | comment NEWLINE
                     | assignment NEWLINE
                     | while NEWLINE
                     | if NEWLINE
                     | command NEWLINE
                     | function NEWLINE
                     | call NEWLINE
                     | RETURN expression NEWLINE
                     | empty NEWLINE"""

        if len(p) == 4:
            p[0] = node('return', val=p[2])
        else:
            p[0] = p[1]

    @staticmethod
    def p_statement_error_no_nl(p):
        """statement : error"""
        p[0] = node('error', val="Wrong syntax", no=p.lineno(1), pos=p.lexpos(1))
        sys.stderr.write(f'>>> Wrong syntax\n')

    @staticmethod
    def p_declaration(p):
        """declaration : type variables"""
        p[0] = node('declaration', val=p[1], ch=p[2], no=p.lineno(2), pos=p.lexpos(2))

    @staticmethod
    def p_declaration_error(p):
        """declaration : type error"""
        p[0] = node('declaration', val=p[1], ch=p[2], no=p.lineno(2), pos=p.lexpos(2))
        sys.stderr.write(f'>>> Wrong name of declared value\n')

    @staticmethod
    def p_comment(p):
        """comment : COMMENT any"""
        p[0] = node('comment', val=p[2])

    @staticmethod
    def p_any(p):
        """any : any VARIABLE
               | VARIABLE"""
        if len(p) == 3:
            p[0] = str(p[1]) + ' ' + str(p[2])
        else:
            p[0] = p[1]

    @staticmethod
    def p_type(p):
        """type : INTEGER
                | STRING
                | BOOL
                | VECTOR OF type
        """
        if len(p) == 2:
            p[0] = node('type', val=p[1], ch=[], no=p.lineno(1), pos=p.lexpos(1))
        else:
            p[0] = node('type', val=str(p[1]) + ' ' + str(p[2]) + ' ' + str(p[3]), ch=[], no=p.lineno(1),
                        pos=p.lexpos(1))

    @staticmethod
    def p_variables(p):
        """variables : variable COMMA variables
                | assignment COMMA variables
                | variable
                | assignment"""
        if len(p) == 4:
            p[0] = node('variables', ch=[p[1], p[3]], no=p.lineno(1), pos=p.lexpos(1))
        else:
            p[0] = node('variables', ch=p[1], no=p.lineno(1), pos=p.lexpos(1))

    @staticmethod
    def p_assignment(p):
        """assignment : variable ASSIGNMENT expression"""
        p[0] = node('assignment', ch=[p[1], p[3]], no=p.lineno(1), pos=p.lexpos(1))

    @staticmethod
    def p_assignment_err(p):
        """assignment : variable ASSIGNMENT error"""
        p[0] = node('error', val="Wrong assignment", no=p.lineno(1), pos=p.lexpos(1))
        sys.stderr.write(f'>>> Wrong assignment\n')

    @staticmethod
    def p_variable(p):
        """variable : VARIABLE indexing
                    | VARIABLE"""
        if len(p) == 2:
            p[0] = node('variable', p[1], no=p.lineno(1), pos=p.lexpos(1))
        else:
            p[0] = node('indexing', p[1], ch=p[2], no=p.lineno(2), pos=p.lexpos(2))

    @staticmethod
    def p_indexing(p):
        """indexing : L_QBRACKET expression R_QBRACKET indexing
                    | L_QBRACKET expression R_QBRACKET"""
        if len(p) == 5:
            p[0] = node('indexing', ch=[p[2], p[4]], no=p.lineno(2), pos=p.lexpos(2))
        else:
            p[0] = node('indexing', ch=p[2], no=p.lineno(2), pos=p.lexpos(2))

    @staticmethod
    def p_expression(p):
        """expression : variable
                      | const
                      | qstring
                      | math_expression
                      | robot_command
                      | converting_command
                      | vector_pop
                      | call"""
        p[0] = p[1]

    @staticmethod
    def p_qstring(p):
        """qstring : DOUBLE_QUOTE string DOUBLE_QUOTE
                   | QUOTE string QUOTE"""
        p[0] = node('string', p[2])

    @staticmethod
    def p_string(p):
        """string : VARIABLE string
                   | DECIMAL string
                   | FALSE string
                   | TRUE string
                   | FALSE
                   | TRUE
                   | DECIMAL
                   | VARIABLE"""
        if len(p) == 3:
            var = ''.join(p[1])
            var = var + ' '
            var = var.join(str(p[2]))
            p[0] = var
        else:
            p[0] = str(p[1])

    @staticmethod
    def p_const(p):
        """const : TRUE
                 | FALSE
                 | UNDEFINED
                 | DECIMAL
                 | EXIT
                 | WOOD
                 | STEEL
                 | GLASS
                 | CONCRETE
                 | PLASTIC"""
        p[0] = node('const', val=p[1])

    @staticmethod
    def p_math_expression(p):
        """math_expression : expression LESS expression
                           | expression GREATER expression
                           | expression EQ expression
                           | expression NOTEQ expression
                           | expression PLUS expression
                           | expression MINUS expression"""
        p[0] = node('binary_expression', p[2], ch=[p[1], p[3]], no=p.lineno(1), pos=p.lexpos(1))

    @staticmethod
    def p_while(p):
        """while : DO statements_group UNTIL expression"""
        p[0] = node('while', ch={'condition': p[4], 'body': p[2]}, no=p.lineno(2), pos=p.lexpos(1))

    @staticmethod
    def p_while_err(p):
        """while : DO error"""
        p[0] = node('error', val="Wrong while", no=p.lineno(2), pos=p.lexpos(2))
        sys.stderr.write(f'>>> Wrong while\n')

    @staticmethod
    def p_if(p):
        """if : IF expression THEN statements_group """
        p[0] = node('if', ch={'condition': p[2], 'body': p[4]}, no=p.lineno(2), pos=p.lexpos(2))

    @staticmethod
    def p_if_else(p):
        """if : IF expression THEN statements_group ELSE statements_group"""
        p[0] = node('if', ch={'condition': p[2], 'body': p[4], 'else': p[6]}, no=p.lineno(2), pos=p.lexpos(2))

    @staticmethod
    def p_if_err(p):
        """if : IF error"""
        p[0] = node('error', val="Wrong while", no=p.lineno(2), pos=p.lexpos(2))
        sys.stderr.write(f'>>> Wrong if\n')

    def p_function(self, p):
        """function : FUNCTION OF type VARIABLE LBRACKET parameters RBRACKET statements_group
                    | FUNCTION OF type VARIABLE BRACKETS statements_group"""
        if len(p) == 9:
            self._functions[p[4]] = node('function', ch={'type': p[3], 'parameters': p[6], 'body': p[8]})
            p[0] = node('function_description', val=p[4], no=p.lineno(1), pos=p.lexpos(1))
        else:
            self._functions[p[4]] = node('function', ch={'type': p[3], 'body': p[6], 'parameters': None})
            p[0] = node('function_description', val=p[4], no=p.lineno(1), pos=p.lexpos(1))

    def p_function_continue(self, p):
        """function : FUNCTION OF type VARIABLE LBRACKET parameters CONTINUE RBRACKET statements_group
                    | FUNCTION OF type VARIABLE LBRACKET CONTINUE RBRACKET statements_group"""
        if len(p) == 10:
            self._functions[p[4]] = node('function',
                                         ch={'type': p[3], 'parameters': p[6], 'body': p[9], 'continue': True})
            p[0] = node('function_description', val=p[4], no=p.lineno(1), pos=p.lexpos(1))
        else:
            self._functions[p[4]] = node('function',
                                         ch={'type': p[3], 'body': p[8], 'continue': True, 'parameters': None})
            p[0] = node('function_description', val=p[4], no=p.lineno(1), pos=p.lexpos(1))

    @staticmethod
    def p_function_err(p):
        """function : FUNCTION error"""
        p[0] = node('error', val="Wrong function name", no=p.lineno(2), pos=p.lexpos(2))
        sys.stderr.write(f'>>> Wrong function name\n')

    @staticmethod
    def p_command(p):
        """command : vector_command
                   | robot_command"""
        p[0] = p[1]

    @staticmethod
    def p_command_error(p):
        """command : vector_command error
                   | robot_command error"""
        p[0] = node('error', val="Wrong command instruction", no=p.lineno(2), pos=p.lexpos(2))
        sys.stderr.write(f'>>> Wrong command instruction\n')

    @staticmethod
    def p_converting_command(p):
        """converting_command : expression TO type
                              | expression TO expression
                              | expression TO vector_of"""
        p[0] = node('converting', p[1], ch=p[3], no=p.lineno(1), pos=p.lexpos(1))

    @staticmethod
    def p_vector_of(p):
        """vector_of : VECTOR OF vector_of
                    | VECTOR"""
        if len(p) == 2:
            p[0] = 1
        else:
            p[0] = 1 + p[3]

    @staticmethod
    def p_vector_command(p):
        """vector_command : variable PUSH BACK expression
                          | variable PUSH FRONT expression"""
        p[0] = node('vector', p[2] + p[3], ch=[p[1], p[4]], no=p.lineno(1), pos=p.lexpos(1))

    @staticmethod
    def p_vector_command_err(p):
        """vector_command : variable PUSH BACK error
                          | variable PUSH FRONT error"""
        p[0] = node('error', val="Wrong pushing expression", no=p.lineno(1), pos=p.lexpos(1))
        sys.stderr.write(f'>>> Wrong pushing expression\n')

    @staticmethod
    def p_vector_command_pop(p):
        """vector_pop : variable POP BACK
                      | variable POP FRONT"""
        p[0] = node('vector', p[2] + p[3], ch=p[1], no=p.lineno(1), pos=p.lexpos(1))

    @staticmethod
    def p_robot_command(p):
        """robot_command : LEFT
                    | RIGHT
                    | FORWARD
                    | BACK
                    | ROTATE_RIGHT
                    | ROTATE_LEFT
                    | LMS
                    | REFLECT
                    | DRILL"""
        p[0] = node('robot', p[1], no=p.lineno(1), pos=p.lexpos(1))

    @staticmethod
    def p_call(p):
        """call : VARIABLE LBRACKET parameters RBRACKET
                | VARIABLE BRACKETS"""
        if len(p) == 5:
            p[0] = node('call', p[1], ch=p[3], no=p.lineno(1), pos=p.lexpos(1))
        else:
            p[0] = node('call', p[1], ch=[], no=p.lineno(1), pos=p.lexpos(1))

    @staticmethod
    def p_call_err(p):
        """call : VARIABLE LBRACKET error RBRACKET"""
        p[0] = node('error', val="Function call error", no=p.lineno(1), pos=p.lexpos(1))
        sys.stderr.write(f'>>> Function call error\n')

    @staticmethod
    def p_empty(p):
        """empty : """
        pass

    @staticmethod
    def p_parameters(p):
        """parameters : parameters COMMA parameter
                      | parameter"""
        if len(p) == 2:
            p[0] = node('parameters', ch=[p[1]], no=p.lineno(1), pos=p.lexpos(1))
        elif len(p) == 4:
            p[0] = node('parameters', ch=[p[1], p[3]], no=p.lineno(1), pos=p.lexpos(1))

    @staticmethod
    def p_parameter(p):
        """parameter : expression
                     | VARIABLE EQ expression"""
        if len(p) == 2:
            p[0] = node('parameter', p[1], no=p.lineno(1), pos=p.lexpos(1))
        else:
            p[0] = node('parameter', p[1], ch=p[3], no=p.lineno(1), pos=p.lexpos(1))

    def p_error(self, p):
        try:
            sys.stderr.write(f'Syntax error at {p.lineno} line\n')
        except:
            sys.stderr.write(f'Syntax error\n')
        self.ok = False

    def get_f(self):
        return self._functions


if __name__ == '__main__':
    text = None
    correct = False
    while not correct:
        print("Input type? (console, file)")
        inputType = input()
        correct = True
        if inputType == "console":
            text = sys.stdin.read()
        elif inputType == "file":
            f = open("../Tests/Math/bubbleSorting")
            text = f.read()
            f.close()
            print(f'Your file:\n {text}')
        else:
            print("I think, you're wrong :)")
            correct = False

    parser = parser()
    tree, func_table, correctness = parser.parse(text)
    if not correctness:
        sys.stderr.write(f'Can\'t interpretate incorrect algorithm\n')
    tree.print()
    print(func_table)
