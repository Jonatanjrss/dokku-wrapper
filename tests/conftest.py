import pytest
from dokku_wrapper.dokku import Dokku


@pytest.fixture
def dokku():
    return Dokku()
