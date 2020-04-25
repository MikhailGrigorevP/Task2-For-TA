from __future__ import annotations
import ply.yacc as yacc
from ply.lex import LexError
import sys
from typing import List, Dict, Optional

# outer classes
from Lexer.lexer import lexer
from Tree.syntaxTree import node


class parser(object):
    tokens = lexer.tokens

    def __init__(self):
        self.ok = True
        self.lexer = lexer()
        self.parser = yacc.yacc(module=self)
        self._functions: Dict[str, node] = dict()

    def parse(self, s) -> List:
        try:
            res = self.parser.parse(s)
            return res, self._functions
        except LexError:
            sys.stderr.write(f'Illegal token {s}\n')

    @staticmethod
    def p_application(p):
        """application : statements"""
        p[0] = node('program', ch=p[1])

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
            p[0] = node('return', val=p[2])
        else:
            p[0] = p[1]

    @staticmethod
    def p_statements(p):
        """statements : statements statement
                      | statement"""
        if len(p) == 2:
            p[0] = node('statements', ch=p[1])
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
    def p_declaration(p):
        """declaration : type variables"""
        p[0] = node('declaration', val=p[1], ch=p[2])

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
            p[0] = p[1]
        else:
            p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

    @staticmethod
    def p_variables(p):
        """variables : variable COMMA variables
                | assignment COMMA variables
                | variable
                | assignment"""
        if len(p) == 4:
            p[0] = node('variables', ch=[p[1], p[3]])
        else:
            p[0] = node('variables', ch=p[1])

    @staticmethod
    def p_assignment(p):
        """assignment : variable ASSIGNMENT expression"""
        p[0] = node('assignment', ch=[p[1], p[3]])

    @staticmethod
    def p_variable(p):
        """variable : VARIABLE L_QBRACKET expression R_QBRACKET
                    | VARIABLE"""
        if len(p) == 2:
            p[0] = node('variable', p[1])
        else:
            p[0] = node('indexing', p[1], ch=p[3])

    @staticmethod
    def p_expression(p):
        """expression : variable
                      | const
                      | qstring
                      | math_expression
                      | call"""
        p[0] = p[1]

    @staticmethod
    def p_qstring(p):
        """qstring : DOUBLE_QUOTE string DOUBLE_QUOTE
                   | QUOTE string QUOTE"""
        p[0] = node('string', p[2])

    @staticmethod
    def p_string(p):
        """string : string VARIABLE
                   | VARIABLE"""
        if len(p) == 3:
            p[0] = p[1] + ' ' + p[2]
        else:
            p[0] = p[1]

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
        """math_expression : expression PLUS expression
                           | expression MINUS expression
                           | MINUS expression
                           | expression LESS expression
                           | expression GREATER expression
                           | expression EQ expression
                           | expression NOTEQ expression"""
        if len(p) == 3:
            p[0] = node('unary_expression', p[1], ch=p[2])
        else:
            p[0] = node('binary_expression', p[2], ch=[p[1], p[3]])

    @staticmethod
    def p_while(p):
        """while : DO statements_group UNTIL expression"""
        p[0] = node('while', ch=[p[2], p[4]])

    @staticmethod
    def p_if(p):
        """if : IF expression THEN statements_group
              | IF expression THEN statements_group ELSE statements_group"""
        if len(p) == 7:
            p[0] = node('if', ch={'condition': p[2], 'body': p[4], 'else': p[6]})
        else:
            p[0] = node('if', ch={'condition': p[2], 'body': p[4]})

    def p_function(self, p):
        """function : FUNCTION OF type VARIABLE LBRACKET parameters RBRACKET statements_group
                    | FUNCTION OF type VARIABLE BRACKETS statements_group"""
        if len(p) == 9:
            self._functions[p[3]] = node('function', ch={'parameters': p[6], 'body': p[8]})
            p[0] = node('function_description', val=p[3])
        else:
            self._functions[p[3]] = node('function', ch={'body': p[6]})
            p[0] = node('function_description', val=p[3])

    @staticmethod
    def p_command(p):
        """command : vector_command
                   | robot_command
                   | converting_command"""
        p[0] = p[1]

    @staticmethod
    def p_converting_command(p):
        """converting_command : expression TO type
                              | expression TO expression"""
        p[0] = node('converting', p[1], ch=p[3])

    @staticmethod
    def p_vector_command(p):
        """vector_command : VARIABLE PUSH BACK expression
                          | VARIABLE POP BACK
                          | VARIABLE PUSH FRONT expression
                          | VARIABLE POP FRONT"""
        if len(p) == 5:
            p[0] = node('vector', p[1] + ' ' + p[2] + ' ' + p[3], ch=p[4])
        else:
            p[0] = node('vector', p[1] + ' ' + p[2] + ' ' + p[3])

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
        p[0] = node('robot', p[1])

    @staticmethod
    def p_call(p):
        """call : VARIABLE LBRACKET parameters RBRACKET
                | VARIABLE BRACKETS"""
        if len(p) == 5:
            p[0] = node('call', p[1], ch=p[3])
        else:
            p[0] = node('call', p[1])

    @staticmethod
    def p_empty(p):
        """empty : """
        pass

    @staticmethod
    def p_parameters(p):
        """parameters : parameters COMMA parameter
                      | parameter
                      | parameters CONTINUE"""
        if len(p) == 2:
            p[0] = node('parameters', ch=p[1])
        elif len(p) == 3:
            p[0] = node('parameters', ch=[p[1], p[2]])
        else:
            p[0] = node('parameters', ch=[p[1], p[3]])

    @staticmethod
    def p_parameter(p):
        """parameter : expression
                     | VARIABLE EQ expression"""
        if len(p) == 2:
            p[0] = node('parameter', p[1])
        else:
            p[0] = node('parameter', p[1], ch=p[3])

    def p_error(self, p):
        print(f'Syntax error at {p}')
        self.ok = False

    def get_f(self):
        return self._functions


if __name__ == '__main__':
    correct = False
    while not correct:
        print("Input type? (console, file)")
        inputType = input()
        correct = True
        if inputType == "console":
            text = sys.stdin.read()
        elif inputType == "file":
            f = open("../Tests For Parser/test.txt")
            text = f.read()
            f.close()
            print(f'Your file:\n {text}')
        else:
            print("I think, you're wrong :)")
            correct = False

    parser = parser()
    tree, func_table = parser.parse(text)
    tree.print()
