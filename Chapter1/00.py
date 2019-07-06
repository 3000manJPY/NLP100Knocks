#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def reverse_str(string: str) -> str:
    """
    受け取った文字列を逆順にして返す

    Parameter
    ----------
    string: str
        逆順にしたい文字列

    Return
    ----------
    逆順になった文字列
    """
    return string[::-1]

def main():
    in_str = 'stressed'

    rev_str = reverse_str(in_str)
  
    print('文字列(入力): {}'.format(in_str))
    print('文字列(逆順): {}'.format(rev_str))

if __name__ == '__main__':
    main()