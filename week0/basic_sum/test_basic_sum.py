import pytest
from main import Solution


@pytest.mark.parametrize("a,b,expect", [(1, 2, 3), (-1, -2, -3)])
def test_basic_sum(a, b, expect):
    s = Solution()

    result = s.basic_sum(a,b)

    assert result == expect
