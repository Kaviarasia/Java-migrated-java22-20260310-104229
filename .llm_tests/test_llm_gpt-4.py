import pytest

@pytest.fixture
def sample_value():
    return 42

def test_dummy(sample_value):
    assert sample_value == 42
