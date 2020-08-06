from __future__ import annotations

from dataclasses import dataclass


@dataclass
class 判定屋さん:

    def これって軽減税率ですか(self, hinmoku: 品目) -> bool:
        pass


@dataclass
class 品目:
    name: str


@dataclass
class 判定屋さん:

    def これって軽減税率ですか(self, item: 商品) -> bool:
        return True


@dataclass
class 品目:
    name: str


@dataclass
class 商品:
    name: str
    hinmoku: 品目


class Testこうなったらええやん:
    def test_なにかの商品を指定して軽減税率の対象かどうかを判定できる(self):
        sut = 判定屋さん()

        item_からあげ棒 = 商品(name='からあげ棒', hinmoku=品目('食料品'))

        assert sut.これって軽減税率ですか(item_からあげ棒)


@dataclass
class 商品:
    name: str
    hinmoku: 品目


class Testこうなったらええやん:
    def test_なにかの商品を指定して軽減税率の対象かどうかを判定できる(self):
        sut = 判定屋さん()

        item_からあげ棒 = 商品(name='からあげ棒', hinmoku=品目('食料品'))

        assert sut.これって軽減税率ですか(item_からあげ棒)
