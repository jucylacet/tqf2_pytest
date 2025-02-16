import pytest
from calculadora import Calculadora

def test_adicao():
    calc = Calculadora()
    assert calc.adicao(3, 2) == 5
    assert calc.adicao(-1, -1) == -2

def test_subtracao():
    calc = Calculadora()
    assert calc.subtracao(10, 5) == 5
    assert calc.subtracao(0, 7) == -7

def test_multiplicacao():
    calc = Calculadora()
    assert calc.multiplicacao(4, 3) == 12
    assert calc.multiplicacao(-2, 6) == -12

def test_divisao():
    calc = Calculadora()
    assert calc.divisao(10, 2) == 5
    assert calc.divisao(7, 2) == 3.5
    with pytest.raises(ValueError, match="Erro: Divisão por zero não é permitida."):
        calc.divisao(5, 0)

def test_fatorial():
    calc = Calculadora()
    assert calc.fatorial(5) == 120
    assert calc.fatorial(0) == 1
    with pytest.raises(ValueError, match="Erro: O fatorial só é definido para números inteiros não negativos."):
        calc.fatorial(-3)

def test_potencia():
    calc = Calculadora()
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(5, 0) == 1
    assert calc.potencia(4, -2) == 0.0625