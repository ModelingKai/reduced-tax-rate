from src.dummy import Dummy


class TestDummy:
    def test_ダミー(self):
        assert Dummy().sum(1, 1) == 2
