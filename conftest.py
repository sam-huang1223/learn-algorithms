import pytest
#import sys
#import os
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # allows for import from parent directory
from union_find import UF


@pytest.fixture()
def setupUF():
    yield UF(10)

