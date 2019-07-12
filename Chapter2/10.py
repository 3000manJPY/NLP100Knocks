#!/usr/local/bin python3
# -*- coding: utf-8 -*-

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

def main():
    filepath = './hightemp.txt'

    line_num = count_file_line_num(filepath)
  
    print('行数: {}'.format(line_num))

if __name__ == '__main__':
    main()