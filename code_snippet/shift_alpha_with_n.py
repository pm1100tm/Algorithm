def shift_alpha_with_n(char: str, shift: int) -> str:
    return chr((ord(char) + shift - ord('a')) % 26 + ord('a'))


if __name__ == '__main__':
    assert shift_alpha_with_n('a', 1) == 'b'
    assert shift_alpha_with_n('a', 26) == 'a'
    assert shift_alpha_with_n('z', 1) == 'a'
    assert shift_alpha_with_n('z', 2) == 'b'
