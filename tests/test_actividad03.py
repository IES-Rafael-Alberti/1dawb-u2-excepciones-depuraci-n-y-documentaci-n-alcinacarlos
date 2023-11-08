import pytest
from src.actividad03 import cuenta_atras
@pytest.mark.parametrize(
    "input, expected",
    [
        (4, "4, 3, 2, 1, 0"),
        (10, "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
        (12, "12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
        (2, "2, 1, 0")
    ]
)
def test_cuenta_atras_params(input, expected):
    assert cuenta_atras(input) == expected
