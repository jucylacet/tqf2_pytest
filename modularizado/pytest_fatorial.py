import pytest
from fatorial import fatorial

def test_fatorial_positivo():
    assert fatorial(5) == 120

def test_fatorial_zero():
    assert fatorial(0) == 1

def test_fatorial_maior_que_zero():
    assert fatorial(5) > 0

def test_fatorial_nao_negativo():
    assert not fatorial(5) < 0

# ... outros casos de teste