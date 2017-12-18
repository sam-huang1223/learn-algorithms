import pytest

# TODO write testing suite for testing UF_percolate with the files BEFORE refactoring

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
    print(setupUF.data)
    print(setupUF.tree_size)
    