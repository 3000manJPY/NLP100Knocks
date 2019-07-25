#!/usr/local/bin python3
# -*- coding: utf-8 -*-

import gzip
import json
import re

def extract_sections(text: str) -> list:
    """
    記事データからセクション名とその深さの対を返す関数

    Parameter
    ----------
    text: str
        wikipedia記事

    Return
    ----------
    section_names: list
        セクション名と深さの辞書を格納するリスト
    """
    section_names = []
    text_split = text.split('\n')

    for line in text_split:
        m = re.search(r'^(=+)(.+?)=+?$', line)
        if m:
            section_names.append({m.group(2): int(len(m.group(1))) - 1})

    return section_names

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
    section_names = extract_sections(text)
    for el in section_names:
        print(el)

if __name__ == '__main__':
    main()
