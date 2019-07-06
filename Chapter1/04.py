#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def get_initials(string: str, uni_list: list) -> list:
    """
    与えられたテキストの頭文字を指定文字数分取得し，mapping付きで返す関数
    (idx_listで指定されたものは1文字，それ以外は全て2文字)

    Parameters
    ----------
    string: str
        ターゲットの文字列
    idx_list: list
        一文字だけ取り出す単語のインデックス
    
    Return
    ----------
    initial_list: dict
        頭文字と単語番号を保有する辞書
    """
    split_str = string.split(' ')
    idx_list = [val - 1 for val in uni_list]
    initial_list = {}

    for i, word in enumerate(split_str):
        if i in idx_list:
            num_of_char = 1
        else:
            num_of_char = 2

        initial_list[word[0:num_of_char]] = i + 1

    return initial_list

def main():
    in_str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    uni_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    initial_list = get_initials(in_str, uni_list)

    print('文字列(入力): {}'.format(in_str))
    print('インデックスのリスト: {}'.format(uni_list))
    print('頭文字リスト: {}'.format(initial_list))

if __name__ == '__main__':
    main()