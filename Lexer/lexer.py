import sys

import ply.lex as lex

reserved = {
    'true': 'TRUE',
    'false': 'FALSE',
    'undefined': 'UNDEFINED',
    'boolean': 'BOOL',
    'string': 'STRING',
    'integer': 'INTEGER',
    'vector': 'VECTOR',
    'of': 'OF',
    'push': 'PUSH',
    'pop': 'POP',
    'back': 'BACK',
    'front': 'FRONT',
    'to': 'TO',
    'begin': 'BEGIN',
    'end': 'END',
    'do': 'DO',
    'until': 'UNTIL',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'function of': 'FUNCTION_OF',
    'return': 'RETURN',
    'application': 'APPLICATION',
    
    # robot
    'right': 'RIGHT',
    'left': 'LEFT',
    'forward': 'FORWARD',
    # 'back': 'BACK',
    'rotate_right': 'ROTATE_RIGHT',
    'rotate_left': 'ROTATE_LEFT',
    'lms': 'LMS',
    'reflect': 'REFLECT',
    'drill': 'DRILL',
}


class MyLexer(object):

    def __init__(self):
        self.lexer = lex.lex(module=self)

    tokens = ['INT_DEX',  'VARIABLE',
              'ASSIGMENT', 'PLUS', 'MINUS',
              'LBRACKET', 'RBRACKET',
              'DOUBLE_QUOTE', 'QUOTE',  'SPACE',
              'LESS', 'GREATER', 'EQ', 'NOTEQ',
              'R_QBRACKET', 'L_QBRACKET',
              'CONTINUE', 'COMMA', 'NEWLINE'] + list(reserved.values())

    t_ASSIGMENT = r'\:\='
    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_LBRACKET = r'\('
    t_RBRACKET = r'\)'
    t_DOUBLE_QUOTE = r'\"'
    t_QUOTE = r'\''
    t_SPACE = r'\ '
    t_LESS = r'\<'
    t_GREATER = r'\>'
    t_EQ = r'\='
    t_NOTEQ = r'\<\>'
    t_R_QBRACKET = r'\]'
    t_L_QBRACKET = r'\['
    t_CONTINUE = r'\.\.\.'
    t_COMMA = r'\,'

    def t_VARIABLE(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value, 'VARIABLE')
        return t

    def t_INT_DEX(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    def t_error(self, t):
        sys.stderr.write(f'Illegal character: {t.value[0]} at line {t.lexer.lineno}\n')
        t.lexer.skip(1)

    t_ignore = ' \t'

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()


if __name__ == '__main__':
    f = open('test.txt')
    data = f.read()
    f.close()
    lexer = MyLexer()
    lexer.input(data)
    while True:
        token = lexer.token()
        if token is None:
            break
        else:
            print(token)
