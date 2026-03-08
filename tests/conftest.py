import pytest

from clients.fake_store_client import FakeStoreClient


@pytest.fixture
def fake_store_client():
    return FakeStoreClient()