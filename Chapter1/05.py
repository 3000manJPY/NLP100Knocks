#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def get_char_ngram(string: str, n: int) -> list:
    """
    与えられたテキストの文字n-gramを返す関数

    Parameters
    ----------
    string: str
        ターゲットの文字列
    n: int
        n-gramのn

    Return
    ----------
    文字n-gramのリスト
    """
    return [string[i:i+n] for i in range(len(string)-n+1)]

def get_word_ngram(string: str, n: int) -> list:
    """
    与えられたテキストの単語n-gramを返す関数

    Parameters
    ----------
    string: str
        ターゲットの文字列
    n: int
        n-gramのn

    Return
    ----------
    単語n-gramのリスト
    """
    split_str = string.split(' ')

    return [' '.join(split_str[i:i+n]) for i in range(len(split_str)-n+1)]

def main():
    in_str = 'I am an NLPer'

    word_bigram = get_word_ngram(in_str, 2)
    char_bigram = get_char_ngram(in_str, 2)

    print('文字列(入力): {}'.format(in_str))
    print('単語バイグラム: {}'.format(word_bigram))
    print('文字バイグラム: {}'.format(char_bigram))

if __name__ == '__main__':
    main()