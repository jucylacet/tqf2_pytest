import math

class Calculadora:
    def adicao(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Erro: Divisão por zero não é permitida.")
        return a / b

    def fatorial(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Erro: O fatorial só é definido para números inteiros não negativos.")
        return math.factorial(n)

    def potencia(self, base, expoente):
        return base ** expoente
