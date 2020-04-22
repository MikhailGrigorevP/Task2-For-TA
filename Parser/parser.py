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
        self.acc = True
        self.lexer = lexer()
        self.parser = yacc.yacc(module=self)
        self._functions: Dict[str, node] = dict()

    def parse(self, s) -> List:
        try:
            res = self.parser.parse(s)
            return res, self._functions
        except LexError:
            sys.stderr.write(f'Illegal token {s}\n')

    def check_program(self, prog: str) -> bool:
        self.parser.parse(prog)
        return self.acc

    def p_program(self, p):
        'program : stmt_list'
        p[0] = node('program', ch=p[1])

    def p_stmt_list(self, p):
        '''stmt_list : VARIABLE NEWLINE'''
        if len(p) == 2:
            p[0] = node('stmt_list', ch=p[1])

    def p_error(self, p):
        print(f'Syntax error at {p}')
        self.acc = False


if __name__ == '__main__':
    f = open("test.txt")
    txt = f.read()
    f.close()

    parser = parser()
    #txt = sys.stdin.read()
    print(f'INPUT: {txt}')
    tree, func_table = parser.parse(txt)
    # tree = parser.parser.parse(txt, debug=True)
    tree.print()
    # print(funcs)
