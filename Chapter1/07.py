#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def get_text(x: int, y: str, z: float) -> str:
    """
    x,y,zを受け取って「x時のyはz」という文字列を返す関数

    Parameters
    ----------
    x: int
        時間(？)
    y: str
        zの単位(？)
    z: float
        yの具体的数値(？)

    Return
    ----------
    「x時のyはz」という文字列
    """
    return str(x) + '時の' + y + 'は' + str(z)

def main():
    x = 12
    y = '気温'
    z = 22.4

    text = get_text(x, y, z)
  
    print('x = {}, y = {}, z = {}'.format(x, y, z))
    print('取得文字列: {}'.format(text))

if __name__ == '__main__':
    main()