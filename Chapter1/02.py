#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def joint_alt_str(string1: str, string2: str) -> str:
    """
    入力された2つの文字列を交互に結合して1つの文字列にする関数

    Parameters
    ----------
    string1, string2: str
        結合したい文字列

    Return
    ----------
    join_str: str
        結合後の文字列
    """
    join_str = ''
    
    for c1, c2 in zip(string1, string2):
        join_str += c1 + c2

    return join_str

def main():
    str1 = 'パトカー'
    str2 = 'タクシー'

    join_str = joint_alt_str(str1, str2)

    print('文字列(入力): {}，{}'.format(str1, str2))
    print('文字列(結合): {}'.format(join_str))

if __name__ == '__main__':
    main()