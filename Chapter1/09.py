#!/usr/local/bin python3
# -*- coding: utf-8 -*-

import random

def get_typoglycemia_text(string: str, delimiter: str) -> str:
    """
    文字列を受け取りタイポグリセミアなテキストを生成する関数．
    (4文字以内の単語は並び替えない)

    Parameters
    ----------
    string: str
        ターゲットの文字列
    delimiter: str
        デリミタ文字

    Return
    ----------
    変換後の文字列
    """
    split_str = string.split(delimiter)

    return ' '.join([word[0] + ''.join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1] if len(word) > 4 else word for word in split_str])

def main():
    string = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
    delimiter = ' '

    conv_string = get_typoglycemia_text(string, delimiter)
  
    print('入力文字列: {}'.format(string))
    print('文字列(変換後): {}'.format(conv_string))

if __name__ == '__main__':
    main()