#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def merge_file_contents(tgt1_filepath: str, tgt2_filepath: str, delimiter: str, out_filepath: str):
    """
    2つのターゲットファイルの中身をマージする関数

    Parameters
    ----------
    tgt1_filepath, tgt2_filepath: str
        マージ元ファイルパス
    delimiter: str
        デリミタ文字
    out_filepath: str
        マージ先のファイルパス
    """
    with open(tgt1_filepath, 'r') as tgt1_file, open(tgt2_filepath, 'r') as tgt2_file, open(out_filepath, 'w') as out_file:
        for idx, (el1, el2) in enumerate(zip(tgt1_file, tgt2_file)):
            out_file.write(el1.rstrip('\n') + delimiter + el2)

def main():
    tgt1_filepath = './col1.txt'
    tgt2_filepath = './col2.txt'
    out_filepath = './merged_col.txt'

    merge_file_contents(tgt1_filepath, tgt2_filepath, '\t', out_filepath)

if __name__ == '__main__':
    main()
