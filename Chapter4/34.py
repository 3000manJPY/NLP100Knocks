#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def extract_noun_phrase_with_no(morph_text: list) -> set:
    """
    形態素解析結果のリストから「AのB」という形の名詞句を抽出する関数

    Parameter
    ----------
    morph_text: list
        形態素解析結果のリスト

    Return
    ----------
    noun_phrases: set
        「AのB」という形の句の集合
    """
    noun_phrases = []

    for sentence in morph_text:
        for idx, morph in enumerate(sentence):
            try:
                if morph['pos'] == '名詞' and sentence[idx+1]['surface'] == 'の' and sentence[idx+2]['pos'] == '名詞':
                    noun_phrases.append(morph['surface'] + sentence[idx+1]['surface'] + sentence[idx+2]['surface'])
            except IndexError:
                pass

    return set(noun_phrases)

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
    noun_phrases = extract_noun_phrase_with_no(morph_text)
    # 全部
    print(noun_phrases)
    print('----------')
    # 取れた数
    print(len(noun_phrases))
    print('----------')
    # 先頭20個
    print(list(noun_phrases)[0:20])

if __name__ == '__main__':
    main()