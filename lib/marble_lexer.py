#************************************************
# marble_lexer.py
#
# A lexer for the marble language.
# Aubrey Alston 2015
#************************************************

# Using PLY lex
import lex

# ----DELINEATION OF KEYWORDS AND TOKENS----

tokens = (
    # Data tokens
    'INTEGER','DECIMAL','CHARACTER', 'STRING',

    # Expression tokens
    'LPAREN', 'RPAREN',

    # Operation tokens 
    'PLUS','MINUS','DIVIDE', 'TIMES', 

    'NEWLINE'
)

# ----REGULAR EXPRESSION PATTERNS---

# Regular expression patterns for basic 
# constants (integer, decimal, character)
t_INTEGER    = r'[\-]?[0-9]+'
t_DECIMAL    = r'[\-]?[0-9]+\.[0-9]*'
t_CHARACTER  = r'(\'[^\']\')'
t_STRING     = r'(\"[^\"]*\")'

# Regular expression patterns for arithmetic
# operators.
t_PLUS       = r'(\+)'
t_MINUS	     = r'(\-)'
t_TIMES      = r'(\*)'
t_DIVIDE     = r'(\/)'

t_ignore = ' \t'

# Regular expression patterns for multi-use
# tokens.
t_LPAREN  = r'\('
t_RPAREN = r'\)'

def t_NEWLINE(t):       # When a \n is found,
    r'\n'               # increment the line
    t.lexer.lineno +=1  # number of the lexer.
    return t            # This way, line count
                        # and errors can be
                        # reported precisely.

# ----ERROR HANDLING----

# If an error is found, attempt to recover by
# skipping the invalid character.

def t_error(t):
    t.lexer.skip(1)

# Lex the input.
lexer = lex.lex()