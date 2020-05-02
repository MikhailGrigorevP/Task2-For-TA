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
    'function': 'FUNCTION',
    'of': 'OF',
    'to': 'TO',
    'begin': 'BEGIN',
    'end': 'END',
    'do': 'DO',
    'until': 'UNTIL',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'return': 'RETURN',
    
    # robot
    'push': 'PUSH',
    'back': 'BACK',
    'pop': 'POP',
    'front': 'FRONT',
    'right': 'RIGHT',
    'left': 'LEFT',
    'forward': 'FORWARD',
    'rotate_right': 'ROTATE_RIGHT',
    'rotate_left': 'ROTATE_LEFT',
    'lms': 'LMS',
    'reflect': 'REFLECT',
    'drill': 'DRILL',
    # material
    '"GLASS"': 'GLASS',
    '"STEEL"': 'STEEL',
    '"WOOD': 'WOOD',
    '"PLASTIC"': 'PLASTIC',
    '"CONCRETE"': 'CONCRETE',
    '"EXIT"': 'EXIT',
}


class lexer(object):

    def __init__(self):
        self.lexer = lex.lex(module=self)

    tokens = ['DECIMAL',  'VARIABLE',
              'ASSIGNMENT', 'PLUS', 'MINUS',
              'LBRACKET', 'RBRACKET', 'BRACKETS',
              'DOUBLE_QUOTE', 'QUOTE',
              'LESS', 'GREATER', 'EQ', 'NOTEQ',
              'R_QBRACKET', 'L_QBRACKET',
              'CONTINUE', 'COMMA', 'COMMENT', 'NEWLINE'] + list(reserved.values())

    t_ASSIGNMENT = r'\:\='
    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_LBRACKET = r'\('
    t_RBRACKET = r'\)'
    t_BRACKETS = r'\(\)'
    t_DOUBLE_QUOTE = r'\"'
    t_QUOTE = r'\''
    t_LESS = r'\<'
    t_GREATER = r'\>'
    t_EQ = r'\='
    t_NOTEQ = r'\<\>'
    t_R_QBRACKET = r'\]'
    t_L_QBRACKET = r'\['
    t_CONTINUE = r'\.\.\.'
    t_COMMA = r'\,'
    t_COMMENT = r'\#'

    @staticmethod
    def t_VARIABLE(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value, 'VARIABLE')
        return t

    @staticmethod
    def t_DECIMAL(t):
        r'\d+'
        t.value = int(t.value)
        return t

    @staticmethod
    def t_NEWLINE(t):
        r'\n+'
        t.lexer.lineno += t.value.count('\n')
        t.lexer.linestart = t.lexer.lexpos
        return t

    @staticmethod
    def t_error(t):
        sys.stderr.write(f'Error: Illegal character: {t.value[0]} at line {t.lexer.lineno}\n')
        t.lexer.skip(1)

    t_ignore = ' \t'

    def input(self, _data):
        return self.lexer.input(_data)

    def token(self):
        return self.lexer.token()


if __name__ == '__main__':
    f = open('../Tests/fibonacci')
    data = f.read()
    f.close()
    lexer = lexer()
    lexer.input(data)
    while True:
        token = lexer.token()
        if token is None:
            break
        else:
            print(token)
