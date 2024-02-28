import string

import pyparsing
from pyparsing import Char, Forward, Keyword, Opt, Word

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
STRING = pyparsing.QuotedString(quote_char='"')

# Arithmetic expression
AEXP = AVAR | CONSTANT

DISJUNCTION = Forward()

CONJUNCTION = Forward()
DISJUNCTION <<= (DISJUNCTION + OR_BOOLEAN_OR + CONJUNCTION) | CONJUNCTION

INVERSION = Forward()
CONJUNCTION <<= (CONJUNCTION + AND_BOOLEAN_AND + DISJUNCTION) | DISJUNCTION

SUM = Forward()
INVERSION <<= (NOT_BOOLEAN_NOT + INVERSION) | SUM

TERM = Forward()
SUM <<= ((SUM + PLUS_BINARY_ADDITION + TERM) | (SUM + MINUS_BINARY_SUBTRACTION + TERM) | TERM)

POWER = Forward()
TERM <<= ((TERM + ASTERISK_MULTIPLICATION + POWER) | (TERM + SLASH_DIVISION + POWER) | POWER)

FACTOR = Forward()
POWER <<= (POWER + CARET_EXPONENT + FACTOR) | FACTOR

MINUS_UNARY_NEGATIVE = Char("-")

FACTOR <<= (MINUS_UNARY_NEGATIVE + AEXP) | AEXP
