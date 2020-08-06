from __future__ import annotations

from dataclasses import dataclass


@dataclass
class 軽減税率制度:

    def is_軽減税率対象の商品(self, item: 商品) -> bool:
        if item.hinmoku == 品目('酒類'):
            return False
        if item.hinmoku == 品目('食料品'):
            return True

        # あてはまらなかったら、軽減税率対象外
        return False


@dataclass
class 品目:
    name: str


@dataclass
class 商品:
    name: str
    hinmoku: 品目


class Test軽減税率制度:
    """
    ここにTODOリスト書く？
    - 食料品と酒類以外のやつはどうするか
        - 飲料品の判定をする
    
    """

    class Test軽減税率の対象の商品かを調べる:
        def test_からあげ棒は軽減税率の対象である(self):
            item_からあげ棒 = 商品(name='からあげ棒', hinmoku=品目('食料品'))

            assert 軽減税率制度().is_軽減税率対象の商品(item_からあげ棒) is True

        def test_ストロングゼロは軽減税率の対象でない(self):
            item_ストロングゼロ = 商品(name='ストロングゼロ', hinmoku=品目('酒類'))

            assert 軽減税率制度().is_軽減税率対象の商品(item_ストロングゼロ) is False

        def test_リポビタンDは軽減税率の対象でない(self):
            item_リポビタンD = 商品(name='リポビタンD', hinmoku=品目('医薬部外品'))

            assert 軽減税率制度().is_軽減税率対象の商品(item_リポビタンD) is False
