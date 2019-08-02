#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def extract_compound_noun(morph_text: list) -> set:
    """
    形態素解析結果のリストから名詞の連接を抽出する関数

    Parameter
    ----------
    morph_text: list
        形態素解析結果のリスト

    Return
    ----------
    compound_nouns: set
        連接名詞の集合
    """
    compound_nouns = []
    compound_noun = ''

    for sentence in morph_text:
        for morph in sentence:
            if morph['pos'] == '名詞':
                compound_noun += morph['surface']
            else:
                if compound_noun != '':
                    compound_nouns.append(compound_noun)
                    compound_noun = ''

    # 最後にもし残っていたら
    if compound_noun != '':
        compound_nouns.append(compound_noun)

    return set(compound_nouns)

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
    compound_nouns = extract_compound_noun(morph_text)
    # 全部
    print(compound_nouns)
    print('----------')
    # 取れた数
    print(len(compound_nouns))
    print('----------')
    # 先頭20個
    print(list(compound_nouns)[0:20])

if __name__ == '__main__':
    main()