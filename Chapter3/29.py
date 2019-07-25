#!/usr/local/bin python3
# -*- coding: utf-8 -*-

import gzip
import json
import re
import requests

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
    basic_info_text = re.search('^\{\{基礎情報.*?$(.*?)^\}\}$', text, flags=(re.MULTILINE | re.DOTALL)).group(1)
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

def get_national_flag(img_filename: str) -> str:
    """
    渡されたファイル名の画像をwikiにrequestして取得する関数

    Parameter
    ----------
    img_filename: str
        画像ファイル名

    Return
    ----------
    img_link:
        画像へのリンク
    """
    url = 'https://www.mediawiki.org/w/api.php' + '?' + 'action=query' + '&' + 'format=json' \
          + '&' + 'titles=File:' + img_filename + '&' + 'prop=imageinfo' + '&' + 'iiprop=url'
    response = requests.get(url, headers={'User-Agent': 'NLP100Knock_Python(@3000manJPY)'})

    return response.json()['query']['pages']['-1']['imageinfo'][0]['url']

def remove_external_link(basic_info: dict) -> dict:
    """
    基本情報から外部リンクマークアップを取り除く関数

    Parameter
    ---------
    basic_info: dict
        基本情報

    Return
    ----------
    basic_info_wo_external_link: str
        外部リンクマークアップが除去された基本情報
    """
    basic_info_wo_external_link = {}
    pattern1 = re.compile(r'\[https??.+?\]')
    pattern2 = re.compile(r'\[https??://.+?\s(.+?)\]')

    for k, v in basic_info.items():
        basic_info_wo_external_link[k] = re.sub(pattern1, r'', re.sub(pattern2, r'\1', v))

    return basic_info_wo_external_link

def remove_file(basic_info: dict) -> dict:
    """
    基本情報からファイルマークアップを取り除く関数

    Parameter
    ----------
    basic_info: dict
        基本情報

    Return
    ----------
    basic_info_wo_file: dict
        ファイルマークアップが除去された基本情報
    """
    basic_info_wo_file = {}

    for k, v in basic_info.items():
        basic_info_wo_file[k] = re.sub(r'\[\[(File|ファイル):.+?\|.+?\|(.+?)\]\]', r'\2', v)

    return basic_info_wo_file

def remove_html_tag(basic_info: dict) -> dict:
    """
    基本情報からhtmlタグを取り除く関数

    Parameter
    ----------
    basic_info: dict
        基本情報

    Return
    ----------
    basic_info_wo_html_tag: dict
        htmlタグが除去された基本情報
    """
    basic_info_wo_html_tag = {}

    for k, v in basic_info.items():
        basic_info_wo_html_tag[k] = re.sub(r'<(.+?)>', r'', v)

    return basic_info_wo_html_tag

def remove_italic_and_bold(basic_info: dict) -> dict:
    """
    基本情報から太字と斜体を取り除く関数

    Parameter
    ----------
    basic_info: dict
        基本情報

    Return
    ----------
    basic_info_wo_italic_bold: dict
        強調が除去された基本情報
    """
    basic_info_wo_italic_bold = {}

    for k, v in basic_info.items():
        basic_info_wo_italic_bold[k] = re.sub(r'(\'{2,5})(.*?)(\'{2,5})', r'\2', v)

    return basic_info_wo_italic_bold

def remove_internal_link(basic_info: dict) -> dict:
    """
    基本情報から内部リンクマークアップを取り除く関数

    Parameter
    ----------
    basic_info: dict
        基本情報

    Return
    ----------
    basic_info_wo_internal_link: dict
        内部リンクマークアップが除去された基本情報
    """
    basic_info_wo_internal_link = {}
    pattern1 = re.compile(r'\[\[([^|]+?)\]\]')
    pattern2 = re.compile(r'\[\[([^:]+?)\|(.+?)\]\]')

    for k, v in basic_info.items():
        basic_info_wo_internal_link[k] = re.sub(pattern2, r'\2', re.sub(pattern1, r'\1', v))

    return basic_info_wo_internal_link

def remove_lang(basic_info: dict) -> dict:
    """
    基本情報から言語マークアップを取り除く関数

    Parameter
    ----------
    basic_info: dict
        基本情報

    Return
    ----------
    basic_info_wo_lang: dict
        言語マークアップが除去された基本情報
    """
    basic_info_wo_lang = {}

    for k, v in basic_info.items():
        basic_info_wo_lang[k] = re.sub(r'{{lang\|.+?\|(.+?)}}', r'\1', v)

    return basic_info_wo_lang

def remove_markup(basic_info: dict) -> dict:
    """
    基本情報からマークアップを取り除く関数

    Parameter
    ----------
    basic_info: dict
        基本情報

    Return
    ----------
    basic_info_wo_markup: dict
        マークアップが取り除かれた基本情報
    """
    basic_info_wo_markup = {}

    # 太字と斜体
    basic_info_wo_markup = remove_italic_and_bold(basic_info)
    # 内部リンクマークアップ
    basic_info_wo_markup = remove_internal_link(basic_info_wo_markup)
    # htmlタグ
    basic_info_wo_markup = remove_html_tag(basic_info_wo_markup)
    # 外部リンクマークアップ
    basic_info_wo_markup = remove_external_link(basic_info_wo_markup)
    # 言語マークアップ
    basic_info_wo_markup = remove_lang(basic_info_wo_markup)
    # ファイルマークアップ
    basic_info_wo_markup = remove_file(basic_info_wo_markup)

    return basic_info_wo_markup

def main():
    in_filepath = './jawiki-country.json.gz'
    out_filepath = './UK.txt'
    key_title = 'イギリス'

    text = extract_text_from_wiki_gzip(in_filepath, key_title)
    basic_info = extract_basic_info(text)
    basic_info_wo_markup = remove_markup(basic_info)
    img_link = get_national_flag(basic_info_wo_markup['国旗画像'])
    print(img_link)

if __name__ == '__main__':
    main()