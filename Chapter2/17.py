#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def extract_differences_in_column_n(filepath: str, delimiter: str, col_num: int) -> list:
    """
    入力ファイルの指定カラムの異なり文字列の集合を返す関数

    Parameters
    ----------
    filepath: str
        入力ファイルパス
    delimiter: str
        デリミタ文字
    col_num: int
        指定カラム

    Return
    ----------
    differences: list
        指定カラムの異なり文字列の集合
    """
    differences = []

    with open(filepath, 'r') as f:
        for line in f:
            line_split = line.split(delimiter)
            line_split[-1] = line_split[-1].rstrip('\n')
            if not line_split[col_num-1] in differences:
                differences.append(line_split[col_num-1])

    return sorted(differences)

def main():
    in_filepath = './hightemp.txt'

    differences = extract_differences_in_column_n(in_filepath, '\t', 1)
    
    for el in differences:
        print(el)

if __name__ == '__main__':
    main()
