#!/usr/local/bin python3
# -*- coding: utf-8 -*-

import sys

def extract_head_n(filepath: str, line_num: int) -> list:
    """
    入力ファイルの先頭から指定行数だけ抽出する関数

    Parameters
    ----------
    filepath: str
        入力ファイルパス
    line_num: int
        抽出する行数

    Return
    ----------
    先頭n行のリスト
    """
    with open(filepath, 'r') as f:
        file_content = f.readlines()
        return file_content[0:line_num]

def main():
    in_filepath = './hightemp.txt'
    n = int(sys.argv[1])

    head_n = extract_head_n(in_filepath, n)

    for el in head_n:
        print(el, end = '') 

if __name__ == '__main__':
    main()
