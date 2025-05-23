import pytest
from calculator import sumar, restar, multiplicar, dividir, obtener_operacion

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 5) == -5
    assert restar(-2, -2) == 0

def test_multiplicar():
    assert multiplicar(4, 3) == 12
    assert multiplicar(-2, 3) == -6
    assert multiplicar(0, 10) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(-6, 3) == -2
    assert dividir(0, 1) == 0
    assert dividir(5, 0) == "Error: División por cero"

@pytest.mark.parametrize("opcion, esperado", [
    ("1", ("Suma", sumar)),
    ("2", ("Resta", restar)),
    ("3", ("Multiplicación", multiplicar)),
    ("4", ("División", dividir)),
    ("5", (None, None)),
    ("x", (None, None)),
])
def test_obtener_operacion(opcion, esperado):
    nombre, funcion = obtener_operacion(opcion)
    esperado_nombre, esperado_funcion = esperado
    assert nombre == esperado_nombre
    assert funcion == esperado_funcion