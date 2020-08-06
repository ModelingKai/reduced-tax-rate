from __future__ import annotations

from dataclasses import dataclass


@dataclass
class 判定屋さん:

    def これって軽減税率ですか(self, item: 商品) -> bool:
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


class Testこうなったらええやん:
    def test_からあげ棒を指定して軽減税率の対象である(self):
        sut = 判定屋さん()

        item_からあげ棒 = 商品(name='からあげ棒', hinmoku=品目('食料品'))

        assert sut.これって軽減税率ですか(item_からあげ棒) is True

    def test_ストロングゼロを指定して軽減税率の対象でない(self):
        sut = 判定屋さん()

        item_ストロングゼロ = 商品(name='ストロングゼロ', hinmoku=品目('酒類'))

        assert sut.これって軽減税率ですか(item_ストロングゼロ) is False

    def test_リポビタンDを指定して軽減税率の対象でない(self):
        sut = 判定屋さん()

        item_リポビタンD = 商品(name='リポビタンD', hinmoku=品目('医薬部外品'))

        assert sut.これって軽減税率ですか(item_リポビタンD) is False
