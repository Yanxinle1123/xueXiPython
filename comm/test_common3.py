import pytest

from comm.common import delete


@pytest.mark.parameterize("value1,value2,expected", [
    ('hello', 'e', 'hllo'),
    ('world', 'o', 'wrld'),
    ('delete', 'd', 'elete'),
    ('except', 't', 'excep'),
    ('python', 'y', 'pthon'),
])
def test_delete(value1, value2, expected):
    assert delete(value1, value2) == expected
