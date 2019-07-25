#!/usr/local/bin python3
# -*- coding: utf-8 -*-

import gzip
import json
import re

def extract_mediafiles(text: str) -> list:
    """
    記事データからメディアファイルを抽出する関数

    Parameter
    ----------
    text: str
        wikipedia記事

    Return
    ----------
    mediafiles: list
        メディアファイル名のリスト
    """
    mediafiles = []
    text_split = text.split('\n')

    for line in text_split:
        m = re.search(r'(File|ファイル):(.+?)\|', line)
        if m:
            mediafiles.append(m.group(2))

    return mediafiles

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
    mediafiles = extract_mediafiles(text)
    for el in mediafiles:
        print(el)

if __name__ == '__main__':
    main()
