import pytest
from src.actividad05 import comprobar_contraseña
@pytest.mark.parametrize(
    "input, expected",
    [
        ("password", True),
        ("pas2sword", False),
        ("pa53ssword", False),
        ("HOLA", False)
    ]
)
def test_comprobar_contraseña_params(input, expected):
    assert comprobar_contraseña(input) == expected
