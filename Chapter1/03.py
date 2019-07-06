#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def get_char_num_list(string: str) -> list:
    """
    与えられたテキストの各単語の文字数をリスト化して返す関数

    Parameter
    ----------
    string: str
        カウントしたい文字列

    Return
    ----------
    単語数を順番に格納したリスト
    """
    split_str = string.split(' ')

    return [len(word) - word.count(',') - word.count('.') for word in split_str]

def main():
    in_str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

    cnt_list = get_char_num_list(in_str)

    print('文字列(入力): {}'.format(in_str))
    print('文字数リスト: {}'.format(cnt_list))

if __name__ == '__main__':
    main()