#!/usr/local/bin python3
# -*- coding: utf-8 -*-

import gzip
import json
import re

def extract_basic_info(text: str) -> list:
    """
    記事データから基礎情報を抽出する関数

    Parameter
    ----------
    text: str
        wikipedia記事

    Return
    ----------
    basic_info: list
        メディアファイル名のリスト
    """
    pre_idx = ''
    basic_info = {}
    basic_info_text = re.search(r'^\{\{基礎情報.*?$(.*?)^\}\}$', text, flags=(re.MULTILINE | re.DOTALL)).group(1)
    splited_text = [line for line in basic_info_text.split('\n') if line != '']

    for line in splited_text:
        if line[0] == '|':
            m = re.search('^\|(.+?)\s=\s(.+?)$', line)
            basic_info[m.group(1)] = m.group(2)
            pre_idx = m.group(1)
        else:
            basic_info[pre_idx] += line.rstrip('\n')

    return basic_info

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
    basic_info = extract_basic_info(text)
    for k, v in basic_info.items():
        print('{}: {}'.format(k, v))

if __name__ == '__main__':
    main()
