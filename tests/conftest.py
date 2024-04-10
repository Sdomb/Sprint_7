import pytest
from methods import Methods


@pytest.fixture(scope='function')
def methods():
    return Methods()
