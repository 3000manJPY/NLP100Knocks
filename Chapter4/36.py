#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def word_count(morph_text: list, order_type: bool) -> list:
    """
    形態素解析結果のリストから単語とその頻度を算出して返す関数

    Parameters
    ----------
    morph_text: list
        形態素解析結果のリスト
    order_type: bool
        昇順か降順のフラグ(T: 降順，F: 昇順)

    Return
    ----------
    word_count_list: list[tuple]
        連接名詞の集合
    """
    word_count_list = {}

    for sentence in morph_text:
        for morph in sentence:
            if morph['surface'] in word_count_list:
                word_count_list[morph['surface']] += 1
            else:
                word_count_list[morph['surface']] = 1

    return sorted(word_count_list.items(), key = lambda x: x[1], reverse = order_type)

def load_mecab_data(filename: str) -> list:
    """
    mecabの形態素解析の出力をパースする関数

    Parameter
    ----------
    filename: str
        形態素解析結果を格納したファイル

    Return
    ----------
    morph_text: str
        パースされたデータ
    """
    morph_text = []

    with open(filename, 'r') as f:
        sentence = []
        for line in f:
            if line.rstrip('\n') == 'EOS':
                if bool(sentence):
                    morph_text.append(sentence)
                    sentence = []
            else:
                split_t = line.split('\t')
                split_c = split_t[1].split(',')
                sentence.append({'surface': split_t[0], 'base': split_c[6], 'pos': split_c[0], 'pos1': split_c[1]})

    return morph_text

def main():
    in_filepath = './neko.txt.mecab'
    morph_text = load_mecab_data(in_filepath)
    word_count_list = word_count(morph_text, True)
    # 全部
    print(word_count_list)
    print('----------')
    # 取れた数
    print(len(word_count_list))
    print('----------')
    # 先頭20個
    print(word_count_list[0:20])

if __name__ == '__main__':
    main()