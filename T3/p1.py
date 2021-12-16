import sys
import math
import io
import os
import random


def es_potencia(n):
    """
    Argumentos :
        n: int - n >= 1
    Retorna :
        bool - True si existen numeros naturales a y b tales que n = (a**b),
        donde a >= 2 y b >= 2. En caso contrario retorna False.
    """
    if n <= 3:
        return False
    else:
        k = 2
        lim = 4
        while lim <= n:
            if tiene_raiz_entera(n, k):
                return True
            k = k + 1
            lim = lim * 2
        return False


def tiene_raiz_entera(n, k):
    """
    Argumentos :
        n: int - n >= 1
        k: int - k >= 2
    Retorna :
        bool - True si existe numero natural a tal que n = (a**k),
        donde a >= 2. En caso contrario retorna False.
    """
    if n <= 3:
        return False
    else:
        a = 1
        while math.pow(a, k) < n:
            a = 2 * a
        return tiene_raiz_entera_intervalo(n, k, a // 2, a)


def tiene_raiz_entera_intervalo(n, k, i, j):
    """
    Argumentos :
        n: int - n >= 1
        k: int - k >= 2
        i: int - i >= 0
        j: int - j >= 0
    Retorna :
        bool - True si existe numero natural a tal que n = (a**k),
        donde i <= a <= j. En caso contrario retorna False.
    """
    while i <= j:
        if i == j:
            return n == math.pow(i, k)
        else:
            p = (i + j) // 2
            val = math.pow(p, k)
            if n == val:
                return True
            elif val < n:
                i = p + 1
            else:
                j = p - 1
    return False


def test_primalidad(n, k, check_es_potencia):
    """
    Argumentos :
        n: int - n >= 1
        k: int - k >= 1
    Retorna :
        bool - True si n es un numero primo, y False en caso contrario.
        La probabilidad de error del test es menor o igual a 2**(-k),
        y esta basado en el test de primalidad de Solovay–Strassen
    """
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        if check_es_potencia:
            if es_potencia(n):
                return False

        neg = 0
        for i in range(1, k + 1):
            a = random.randint(2, n - 1)

            if math.gcd(a, n) > 1:
                return False

            else:
                b = pow(a, (n-1)//2, mod=n)
                if b == n - 1:
                    neg = neg + 1
                elif b != 1:
                    return False
        if neg > 0:
            return True
        else:
            return False


def find_prime(lower_bound, upper_bound):
    if lower_bound == 1 and upper_bound != 1:
        return 2
    if lower_bound == 2 or lower_bound == 3:
        return lower_bound

    found_prime = -1
    start = lower_bound

    if lower_bound % 2 == 0:
        start = lower_bound + 1

    memory_ = set()

    for iteration in range(16000):
        number = random.randint(start, upper_bound)
        if number not in memory_:
            if test_primalidad(number, 35, False):
                memory_.add(number)
                # print("found", number)
                if test_primalidad(number, 35, True):
                    # print("yup its prime", number)
                    found_prime = number
                    break

    return found_prime


"""
https://es.m.wikipedia.org/wiki/Teorema_de_los_n%C3%BAmeros_primos
"""

# a, b = list(map(int, sys.stdin.readline().strip().split()))
range_input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
a, b = list(map(int, range_input().decode().strip().split()))
result = find_prime(a, b)
sys.stdout.write(str(result))

