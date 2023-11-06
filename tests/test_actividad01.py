import pytest
from src.actividad01 import años_cumplidos
@pytest.mark.parametrize(
    "input_edad, expected",
    [
        (3, "1\n2\n3\n"),
        (4, "1\n2\n3\n4\n"),
        (2, "1\n2\n"),
        (6, "1\n2\n3\n4\n5\n6\n")
    ]
)
def test_años_complidos_params(input_edad, expected):
    assert años_cumplidos(input_edad) == expected
