#!/usr/local/bin python3
# -*- coding: utf-8 -*-

import sys

def count_file_line_num(filepath: str) -> int:
    """
    渡されたファイルの行数をカウントして返す関数

    Parameter
    ----------
    filepath: str
        ファイルパス

    Return
    ----------
    ファイルの行数
    """
    with open(filepath, 'r') as f:
        return sum(1 for line in f)

def split_file_into_n(in_filepath: str, out_filepath: str, split_num: int):
    """
    入力ファイルを指定数で分割する関数

    Parameters
    ----------
    in_filepath: str
        入力ファイルパス
    out_filepath: str
        出力ファイルのパス
    split_num: int
        抽出する行数
    """
    origin_line_num = count_file_line_num(in_filepath)
    new_line_num = int(origin_line_num / split_num)
    remainder = origin_line_num % split_num
    
    with open(in_filepath, 'r') as in_file:
        file_content = in_file.readlines()
    
    for idx in range(split_num):
        with open(out_filepath + '{:02}'.format(idx), 'w') as out_file:
            if idx < remainder:
                out_file.write(''.join(file_content[((new_line_num + 1) * idx):((new_line_num + 1) * (idx + 1))]))
            else:
                out_file.write(''.join(file_content[((new_line_num * idx) + remainder):((new_line_num * (idx + 1)) + remainder)]))

def main():
    in_filepath = './hightemp.txt'
    out_filepath = './hightemp_split'
    n = int(sys.argv[1])

    split_file_into_n(in_filepath, out_filepath, n)

if __name__ == '__main__':
    main()
