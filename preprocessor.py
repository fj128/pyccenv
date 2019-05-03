import re
from typing import Iterable


class CompilationError(Exception):
    def __init__(self, message, token):
        super().__init__(f'{token.format_location()}: {message}:\n{token}')


class Token(str):
    file : str
    line : int
    column : int

    def __new__(cls, value, file, line, column):
        obj = str.__new__(cls, value)
        obj.file = file
        obj.line = line
        obj.column = column
        return obj

    def __eq__(self, other):
        return (str.__eq__(self, other)
                and self.file == other.file
                and self.line == other.line
                and self.column == other.column)

    def format_location(self):
        return f'{self.file}:{self.line}:{self.column}'

    def __repr__(self):
        return f'{str.__repr__(self)}(in {self.format_location()})'


def phase12(input: str, filename: str):
    '''conversion to "source character set" done before
    no trigraphs
    split to physical, then join logical lines'''
    # physical
    lines = [Token(s, filename, l + 1, 1) for l, s in enumerate(re.split(r'\n', input))]
    # join with newlines
    # (preserving accurate line information is left as an exercise to the reader)
    it = iter(lines)
    lines = []
    while True:
        s = next(it, None)
        if s is None:
            break
        while s.endswith('\\'):
            s2 = next(it, None)
            if s2 is None:
                raise CompilationError('EOF following backslash', s)
            s = Token(s[:-1] + s2, s.file, s.line, s.column)
        lines.append(s)
    return lines


def phase3(input: Iterable[Token]):
    '''split lines into preprocessing tokens'''


