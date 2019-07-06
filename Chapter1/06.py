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

def get_difference_list(list1: list, list2: list) -> list:
    """
    2つのリストの差集合を返すリスト

    Parameters
    ----------
    list1, list2: list
        list型の集合(ここでは文字bigram)

    Return
    ----------
    list1とlist2の差集合
    """
    return list(set(list1) - set(list2))

def get_intersection_list(list1: list, list2: list) -> list:
    """
    2つのリストの積集合を返すリスト

    Parameters
    ----------
    list1, list2: list
        list型の集合(ここでは文字bigram)

    Return
    ----------
    list1とlist2の積集合
    """
    return list(set(list1) & set(list2))

def get_union_list(list1: list, list2: list) -> list:
    """
    2つのリストの和集合を返すリスト

    Parameters
    ----------
    list1, list2: list
        list型の集合(ここでは文字bigram)

    Return
    ----------
    list1とlist2の和集合
    """
    return list(set(list1) | set(list2))

def is_element(element: str, target_list: list) -> bool:
    """
    ある文字列が文字列リストの要素か否かを返す関数

    Parameters
    ----------
    target_list: list
        ターゲットの文字列リスト
    element: str
        検索文字列

    Return
    ----------
    存在すればTrue，それ以外はFalse
    """
    return True if element in target_list else False

def main():
    str1 = 'paraparaparadise'
    str2 = 'paragraph'

    str1_char_bigram = get_char_ngram(str1, 2)
    str2_char_bigram = get_char_ngram(str2, 2)
    
    bigram_union = get_union_list(str1_char_bigram, str2_char_bigram)
    bigram_intersection = get_intersection_list(str1_char_bigram, str2_char_bigram)
    bigram_difference = get_difference_list(str1_char_bigram, str2_char_bigram)

    print('文字列(入力): {}，{}'.format(str1, str2))
    print('str1文字バイグラム: {}'.format(str1_char_bigram))
    print('str2文字バイグラム: {}'.format(str2_char_bigram))
    print('和集合: {}'.format(bigram_union))
    print('積集合: {}'.format(bigram_intersection))
    print('差集合: {}'.format(bigram_difference))
    print('str1に\'se\'？: {}'.format(is_element('se', str1_char_bigram)))
    print('str2に\'se\'？: {}'.format(is_element('se', str2_char_bigram)))

if __name__ == '__main__':
    main()