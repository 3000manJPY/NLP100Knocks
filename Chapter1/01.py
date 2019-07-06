#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def extract_odd_chars(string: str) -> str:
    """
    奇数番目の文字だけを抽出して返す関数

    Parameter
    ----------
    string: str
        抽出対象の文字列

    Return
    ----------
    抽出された文字列
    """
    return string[::2]

def main():
    in_str = 'パタトクカシーー'

    extracted_str = extract_odd_chars(in_str)
    
    print('文字列(入力): {}'.format(in_str))
    print('文字列(抽出): {}'.format(extracted_str))

if __name__ == '__main__':
    main()