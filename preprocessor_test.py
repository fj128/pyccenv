import pytest
from preprocessor import CompilationError, Token, phase12

def test_token():
    assert str(Token('abcd', '<in>', 1, 2)) == 'abcd'
    assert repr(Token('abcd', '<in>', 1, 2)) == ''''abcd'(in '<in>':1:2)'''

def test_phase12():
    assert phase12('a\nb', '<input>') == [Token('a', '<input>', 1, 1), Token('b', '<input>', 2, 1)]
    assert phase12('a\\\nb', '<input>') == [Token('ab', '<input>', 1, 1)]
    with pytest.raises(CompilationError, match=r'in:1:1: EOF following backslash:\na\\'):
        phase12('a\\', 'in')

