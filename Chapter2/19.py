#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def sort_elements_in_column_n(filepath: str, delimiter: str, col_num: int) -> list:
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
    elements = {}

    with open(filepath, 'r') as f:
        for line in f:
            line_split = line.split(delimiter)
            line_split[-1] = line_split[-1].rstrip('\n')
            if line_split[col_num-1] not in elements:
                elements[line_split[col_num-1]] = 1
            else:
                elements[line_split[col_num-1]] += 1

    return sorted(elements.items(), key = lambda x: x[1], reverse = True)

def main():
    in_filepath = './hightemp.txt'

    sorted_elements = sort_elements_in_column_n(in_filepath, '\t', 1)
    
    for el in sorted_elements:
        print('      {} {}'.format(el[1], el[0]))

if __name__ == '__main__':
    main()
