import pytest_datadir_ng
import pytest

from union_find import Percolation


class TestUnionFind:
    @staticmethod
    def test_union_find(setupUF):
        setupUF.union(4, 6)
        setupUF.union(3, 7)
        setupUF.union(3, 9)
        setupUF.union(9, 1)
        assert setupUF.connected(1, 3)
        setupUF.union(9, 2)
        assert not setupUF.connected(2, 4)
        setupUF.union(7, 6)
        assert setupUF.connected(4, 2)

    @staticmethod
    @pytest.mark.parametrize("inputName", [('input4_fails'), ('input4_succeeds'), ('input6_succeeds')])
    def test_percolation(datadir, inputName):
        result = Percolation('test_algorithms/TestUnionFind/test_percolation/{}.txt'.format(inputName))
        assert result.connected(result.data[0], result.data[-1]) == result.succeeds, "Percolation result does not match file input"

