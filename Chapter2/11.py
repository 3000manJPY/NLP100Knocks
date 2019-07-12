#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def replace_delimiter(filepath: str, pre_delimiter: str, new_delimiter: str) -> list:
    """
    ファイルのデリミタ文字を置換する関数

    Parameters
    ----------
    filepath: str
        入力ファイルパス
    pre_delimiter, new_delimiter: str
        現在/新規のデリミタ文字

    Return
    ----------
    置換後の文字列のリスト
    """
    with open(filepath, 'r') as f:
        return [line.replace(pre_delimiter, new_delimiter) for line in f]

def main():
    filepath = './hightemp.txt'

    replaced_strs = replace_delimiter(filepath, '\t', ' ')

    for el in replaced_strs:
        print(el, end = '')

if __name__ == '__main__':
    main()