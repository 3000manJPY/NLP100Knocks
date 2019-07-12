#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def sort_lines_with_n(filepath: str, delimiter: str, col_num: int, reverse: bool) -> list:
    """
    入力ファイルの指定カラムでソートする関数

    Parameters
    ----------
    filepath: str
        入力ファイルパス
    delimiter: str
        デリミタ文字
    col_num: int
        指定カラム
    reverse: bool
        逆順にするか否か

    Return
    ----------
    指定カラムの異なり文字列の集合
    """
    origin = []

    with open(filepath, 'r') as f:
        for line in f:
            line_split = line.split(delimiter)
            line_split[-1] = line_split[-1].rstrip('\n')
            origin.append(line_split)

    return sorted(origin, key = lambda x: x[col_num-1], reverse = reverse)

def main():
    in_filepath = './hightemp.txt'

    sorted_lines = sort_lines_with_n(in_filepath, '\t', 3, False)
    
    for line in sorted_lines:
        print('\t'.join(line))

if __name__ == '__main__':
    main()
