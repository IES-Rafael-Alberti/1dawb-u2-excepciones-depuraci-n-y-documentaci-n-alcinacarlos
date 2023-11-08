import pytest
from src.actividad02 import impares
@pytest.mark.parametrize(
    "input_edad, expected",
    [
        (4, "1, 3"),
        (5, "1, 3, 5"),
        (10, "1, 3, 5, 7, 9"),
        (20, "1, 3, 5, 7, 9, 11, 13, 15, 17, 19")
    ]
)
def test_impares_params(input_edad, expected):
    assert impares(input_edad) == expected
