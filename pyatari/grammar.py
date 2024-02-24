import string

import pyparsing
from pyparsing import Char, Keyword, Opt, Word

PLUS_BINARY_ADDITION = Char("+")
MINUS_BINARY_SUBTRACTION = Char("-")
ASTERISK_MULTIPLICATION = Char("*")
SLASH_DIVISION = Char("/")
CARET_EXPONENT = Char("^")

# Arithmetic operator
AOP = (
    PLUS_BINARY_ADDITION
    | MINUS_BINARY_SUBTRACTION
    | ASTERISK_MULTIPLICATION
    | SLASH_DIVISION
    | CARET_EXPONENT
)

NOT_BOOLEAN_NOT = Keyword("NOT")
AND_BOOLEAN_AND = Keyword("AND")
OR_BOOLEAN_OR = Keyword("OR")

# Logical operator
LOP = NOT_BOOLEAN_NOT | AND_BOOLEAN_AND | OR_BOOLEAN_OR

# Variable name
VARNAME = Word(
    string.ascii_uppercase, string.ascii_uppercase + string.digits, min=1, max=120
)
# Arithmetic variable
AVAR = VARNAME
# String variable
SVAR = VARNAME + "$"
# Matrix variable
MVAR = VARNAME
# Variable
VAR = AVAR | SVAR | MVAR

LINENO = Word(string.digits)

CONSTANT = Word(string.digits) + Opt("." + Opt(Word(string.digits)))
STRING = pyparsing.QuotedString()

# Arithmetic expression
AEXP = AVAR | CONSTANT
