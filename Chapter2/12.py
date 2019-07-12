#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def extract_column(in_filepath: str, out_filepath: str, delimiter: str, col_num: int):
    """
    入力ファイルの指定カラムだけ出力ファイルに保存する関数

    Parameters
    ----------
    in_filepath, out_filepath: str
        入力/出力ファイルパス
    delimiter: str
        デリミタ文字
    col_num: int
        抽出したいカラムの番号
    """
    with open(in_filepath, 'r') as in_file, open(out_filepath, 'w') as out_file:
        for line in in_file:
            line_split = line.split(delimiter)
            line_split[-1] = line_split[-1].rstrip('\n')
            out_file.write(line_split[col_num-1] + '\n')

def main():
    in_filepath = './hightemp.txt'

    out_filepath = './col1.txt'
    extract_column(in_filepath, out_filepath, '\t', 1)

    out_filepath = './col2.txt'
    extract_column(in_filepath, out_filepath, '\t', 2)

if __name__ == '__main__':
    main()
