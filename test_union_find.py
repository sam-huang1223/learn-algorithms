import pytest

from union_find import UF

@pytest.fixture()
def prep():
    data = UF()

@pytest.mark.usefixtures("prep")
class TestUF:
    def test_union(self):
        pass