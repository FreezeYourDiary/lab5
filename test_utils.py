import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)])
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected ", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected


@pytest.mark.parametrize("x", [-100, 120.5, 1515])
def test_zakres(x):
    with pytest.raises(ValueError, match="out of range"):
        utils.float_to_binary(x)


def test_correct_conversion():
    assert utils.float_to_binary(0.0) == "0000000000"
    assert utils.float_to_binary(4) == "0010000000"
    assert utils.float_to_binary(0.5) == "0000010000"


@pytest.mark.parametrize("value", [1, 3.0, 15.0, 0.0])
def test_is_natural(value):
    binary = utils.float_to_binary(value)
    assert binary[-5:] == "00000"
