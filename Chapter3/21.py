#!/usr/local/bin python3
# -*- coding: utf-8 -*-

import gzip
import json
import re

def extract_category_lines(text: str) -> list:
    """
    カテゴリーの行を記事本文テキストから抽出する関数

    Parameter
    ----------
    text: str
        wikipediaの記事本文

    Return
    ----------
    category_lines: str
        カテゴリの行のリスト
    """
    category_lines = []
    text_split = text.split('\n')

    for line in text_split:
        if 'Category:' in line:
            category_lines.append(line)

    return category_lines

def extract_text_from_wiki_gzip(in_filepath: str, key_title: str) -> str:
    """
    titleをkeyに記事本文を抽出する関数

    Parameter
    ----------
    in_filepath, out_filepath: str
        入力/出力ファイルパス
    key_title: str
        検索タイトル

    Return
    ----------
    該当のテキスト（存在しなければ''）
    """

    with gzip.open(in_filepath, "rt", "utf-8") as in_file:
        for line in in_file:
            data = json.loads(line)
            if data['title'] == key_title:
                return data['text']
                
    return ''

def main():
    in_filepath = './jawiki-country.json.gz'
    out_filepath = './UK.txt'
    key_title = 'イギリス'

    text = extract_text_from_wiki_gzip(in_filepath, key_title)
    category_lines = extract_category_lines(text)
    print(' / '.join(category_lines))

if __name__ == '__main__':
    main()