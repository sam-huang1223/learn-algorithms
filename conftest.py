import pytest
from .union_find import UF

@pytest.fixture()
def setupUF():
    yield UF(10)