import codecs
from enum import IntEnum


def make_decoding_table(european: bool = False) -> str:
    # making an encoding that preserves inverse characters
    # (e.g. by prefixing each one with an escape sequence like \d)
    # would require a full custom Codec implementation
    if european:
        table = [c[2] if c[2] else c[1] for c in ATASCII]
    else:
        table = [c[1] for c in ATASCII]
    table.extend(table)

    table[0x9B] = "\n"

    return "".join(table)


# this is somewhat undocumented, see here for example:
# https://github.com/python/cpython/blob/main/Lib/encodings/cp1252.py
# see also here:
# https://github.com/python/cpython/blob/main/Lib/codecs.py
# https://docs.python.org/3/library/codecs.html
decoding_table = make_decoding_table()
encoding_table = codecs.charmap_build(decoding_table)


class Codec(codecs.Codec):
    def encode(self, input, errors="strict"):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors="strict"):
        return codecs.charmap_decode(input, errors, decoding_table)


class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(
        name="atascii",
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


class ControlChar(IntEnum):
    ESCAPE = 0x1B
    CURSOR_UP = 0x1C
    CURSOR_DOWN = 0x1D
    CURSOR_LEFT = 0x1E
    CURSOR_RIGHT = 0x1F
    CLEAR_SCREEN = 0x7D
    DELETE = 0x7E
    TAB = 0x7F
    # only control character without a printable version
    END_OF_LINE = 0x9B
    DELETE_LINE = 0x9C
    INSERT_LINE = 0x9D
    CLEAR_TAB_STOP = 0x9E
    SET_TAB_STOP = 0x9F
    BUZZER = 0xFD
    DELETE_CHARACTER = 0xFE
    INSERT_CHARACTER = 0xFF


# code points, normal character, european character
ATASCII = (
    (0x00, "♥", "á"),
    (0x01, "├", "ù"),
    (0x02, "🮇", "Ñ"),
    (0x03, "┘", "É"),
    (0x04, "┤", "ç"),
    (0x05, "┐", "ô"),
    (0x06, "╱", "ò"),
    (0x07, "╲", "ì"),
    (0x08, "◢", "£"),
    (0x09, "▗", "ï"),
    (0x0A, "◣", "ü"),
    (0x0B, "▝", "ä"),
    (0x0C, "▘", "Ö"),
    (0x0D, "🮂", "ú"),
    (0x0E, "▂", "ó"),
    (0x0F, "▖", "ö"),
    (0x10, "♣", "Ü"),
    (0x11, "┌", "â"),
    (0x12, "─", "û"),
    (0x13, "┼", "î"),
    (0x14, "•", "é"),
    (0x15, "▄", "è"),
    (0x16, "▎", "ñ"),
    (0x17, "┬", "ê"),
    (0x18, "┴", "å"),
    (0x19, "▌", "à"),
    (0x1A, "└", "Å"),
    (0x1B, "␛", ""),
    (0x1C, "↑", ""),
    (0x1D, "↓", ""),
    (0x1E, "←", ""),
    (0x1F, "→" ""),
    (0x20, " " ""),
    (0x21, "!" ""),
    (0x22, '"' ""),
    (0x23, "#" ""),
    (0x24, "$" ""),
    (0x25, "%" ""),
    (0x26, "&" ""),
    (0x27, "'" ""),
    (0x28, "(" ""),
    (0x29, ")" ""),
    (0x2A, "*" ""),
    (0x2B, "+" ""),
    (0x2C, "," ""),
    (0x2D, "-" ""),
    (0x2E, "." ""),
    (0x2F, "/" ""),
    (0x30, "0" ""),
    (0x31, "1" ""),
    (0x32, "2" ""),
    (0x33, "3" ""),
    (0x34, "4" ""),
    (0x35, "5" ""),
    (0x36, "6" ""),
    (0x37, "7" ""),
    (0x38, "8" ""),
    (0x39, "9" ""),
    (0x3A, ":" ""),
    (0x3B, ";" ""),
    (0x3C, "<" ""),
    (0x3D, "=" ""),
    (0x3E, ">" ""),
    (0x3F, "?" ""),
    (0x40, "@" ""),
    (0x41, "A" ""),
    (0x42, "B" ""),
    (0x43, "C" ""),
    (0x44, "D" ""),
    (0x45, "E" ""),
    (0x46, "F" ""),
    (0x47, "G" ""),
    (0x48, "H" ""),
    (0x49, "I" ""),
    (0x4A, "J" ""),
    (0x4B, "K" ""),
    (0x4C, "L" ""),
    (0x4D, "M" ""),
    (0x4E, "N" ""),
    (0x4F, "O" ""),
    (0x50, "P" ""),
    (0x51, "Q" ""),
    (0x52, "R" ""),
    (0x53, "S" ""),
    (0x54, "T" ""),
    (0x55, "U" ""),
    (0x56, "V" ""),
    (0x57, "W" ""),
    (0x58, "X" ""),
    (0x59, "Y" ""),
    (0x5A, "Z" ""),
    (0x5B, "[" ""),
    (0x5C, "\\" ""),
    (0x5D, "]" ""),
    (0x5E, "^" ""),
    (0x5F, "_" ""),
    (0x60, "♦" "¡"),
    (0x61, "a" ""),
    (0x62, "b" ""),
    (0x63, "c" ""),
    (0x64, "d" ""),
    (0x65, "e" ""),
    (0x66, "f" ""),
    (0x67, "g" ""),
    (0x68, "h" ""),
    (0x69, "i" ""),
    (0x6A, "j" ""),
    (0x6B, "k" ""),
    (0x6C, "l" ""),
    (0x6D, "m" ""),
    (0x6E, "n" ""),
    (0x6F, "o" ""),
    (0x70, "p" ""),
    (0x71, "q" ""),
    (0x72, "r" ""),
    (0x73, "s" ""),
    (0x74, "t" ""),
    (0x75, "u" ""),
    (0x76, "v" ""),
    (0x77, "w" ""),
    (0x78, "x" ""),
    (0x79, "y" ""),
    (0x7A, "z" ""),
    (0x7B, "♠" "Ä"),
    (0x7C, "|" ""),
    (0x7D, "🢰" ""),
    (0x7E, "◀" ""),
    (0x7F, "▶" ""),
)
