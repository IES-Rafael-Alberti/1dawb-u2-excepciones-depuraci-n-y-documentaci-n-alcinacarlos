import pytest
from src.actividad04 import comprobar_entero
@pytest.mark.parametrize(
    "input, expected",
    [
        ("4", 4),
        ("7", 7),
        ("25", 25),
        ("hola", None)
    ]
)
def test_comprobar_entero_params(input, expected):
    assert comprobar_entero(input) == expected
