import string

import pyparsing
from pyparsing import Forward, Keyword, Literal, Opt, Word

# Operators
# In precedence order

PLUS_BINARY_ADDITION = Literal("+")
MINUS_BINARY_SUBTRACTION = Literal("-")

CARET_EXPONENT = Literal("^")

ASTERISK_MULTIPLICATION = Literal("*")
SLASH_DIVISION = Literal("/")

MINUS_UNARY_NEGATIVE = Literal("-")
PLUS_UNARY_POSITIVE = Literal("+")

NUMERIC_LESS_THAN = Literal("<")
NUMERIC_MORE_THAN = Literal(">")
NUMERIC_EQUAL_TO = Literal("=")
NUMERIC_LESS_EQUAL = Literal("<=")
NUMERIC_MORE_EQUAL = Literal(">=")
NUMERIC_NOT_EQUAL = Literal("<>")

NOT_BOOLEAN_NOT = Keyword("NOT")
AND_BOOLEAN_AND = Keyword("AND")
OR_BOOLEAN_OR = Keyword("OR")

# Terms from book

# Arithmetic operator
AOP = (
    PLUS_BINARY_ADDITION
    | MINUS_BINARY_SUBTRACTION
    | ASTERISK_MULTIPLICATION
    | SLASH_DIVISION
    | CARET_EXPONENT
)

# Logical operator
LOP = NOT_BOOLEAN_NOT | AND_BOOLEAN_AND | OR_BOOLEAN_OR

NUMERIC_RELATIONAL = (
    NUMERIC_LESS_THAN
    | NUMERIC_MORE_THAN
    | NUMERIC_EQUAL_TO
    | NUMERIC_LESS_EQUAL
    | NUMERIC_MORE_EQUAL
    | NUMERIC_NOT_EQUAL
)

# Variable name
VARNAME = Word(
    init_chars=string.ascii_uppercase,
    body_chars=string.ascii_uppercase + string.digits,
    min=1,
    max=120,
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

# Atari Basic Reference Manual, Page 10, "Operator Precedence"
# https://www.atarimania.com/documents/Atari-Basic-Reference-Manual-Rev-C.pdf

DISJUNCTION = Forward()

CONJUNCTION = Forward()
DISJUNCTION <<= (DISJUNCTION + OR_BOOLEAN_OR + CONJUNCTION) | CONJUNCTION

INVERSION = Forward()
CONJUNCTION <<= (CONJUNCTION + AND_BOOLEAN_AND + DISJUNCTION) | DISJUNCTION

COMPARISON = Forward()
INVERSION <<= (NOT_BOOLEAN_NOT + INVERSION) | COMPARISON

SUM = Forward()
COMPARISON <<= (COMPARISON + NUMERIC_RELATIONAL + SUM) | SUM

TERM = Forward()
SUM <<= (
    (SUM + PLUS_BINARY_ADDITION + TERM) | (SUM + MINUS_BINARY_SUBTRACTION + TERM) | TERM
)

POWER = Forward()
TERM <<= (
    (TERM + ASTERISK_MULTIPLICATION + POWER) | (TERM + SLASH_DIVISION + POWER) | POWER
)

FACTOR = Forward()
POWER <<= (POWER + CARET_EXPONENT + FACTOR) | FACTOR

FACTOR <<= (MINUS_UNARY_NEGATIVE + AEXP) | AEXP
