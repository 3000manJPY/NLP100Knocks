#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def cipher(string: str) -> str:
    """
    文字列を受け取り，英語小文字のみを暗号/復号化する関数

    Parameter
    ----------
    string: str
        暗号/復号化対象の文字列

    Return
    ----------
    暗号/復号後の文字列
    """
    return ''.join(chr(219 - ord(c)) if c.islower() else c for c in string)

def main():
    string = "I couldn't imagine how my program would work when I was writing it."

    enc_string = cipher(string)
    dec_string = cipher(enc_string)
  
    print('入力文字列: {}'.format(string))
    print('文字列(暗号化後): {}'.format(enc_string))
    print('文字列(復号化後): {}'.format(dec_string))

if __name__ == '__main__':
    main()