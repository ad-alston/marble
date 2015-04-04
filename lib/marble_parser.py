#************************************************
# marble_parser.py
#
# A parser for the marble language.
# Aubrey Alston 2015
#************************************************

# Use the lexer defined by in marble_lexer.py
import marble_lexer

# Utilizing the PLY LALR parser generator.
import yacc

# ----TOKEN DECLARATION AND PRECEDENCE----

# Use the tokens from marble_lexer
tokens = marble_lexer.tokens

# Operator precedence
precedence = (
               ('left','PLUS','MINUS'),
               ('left','TIMES','DIVIDE')
)

# ----GRAMMAR PRODUCTIONS----

def p_integer(p):
    '''integer : INTEGER'''
    p[0] = ("INTEGER", p[1])

# ----INITIALIZE PARSER----

yacc_parser = yacc.yacc()

def parse(data, debug=0):
    yacc_parser.error = 0
    parsed = yacc_parser.parse(data, debug=debug)
    if yacc_parser.error:
        return -1
    return parsed